from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
import json
from deepdiff import DeepDiff
from .models.TodoProject import TodoProject
from .models.TodoChange import TodoChange
from .models.TodoTask import TodoTask
from .models.TodoStatus import TodoStatus
from .models.User import User
from .serializers.ShortTodoTaskSerializer import ShortTodoTaskSerializer
from .serializers.ShortTodoProjectSerializer import ShortTodoProjectSerializer
from .serializers.ShortTodoStatusSerializer import ShortTodoStatusSerializer
from .serializers.ShortUserSerializer import ShortUserSerializer


def get_data_and_request(obj):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    data = None

    if obj._meta.label_lower == TodoProject._meta.label_lower:
        data = ShortTodoProjectSerializer(
            obj
        ).data
    if obj._meta.label_lower == TodoTask._meta.label_lower:
        data = ShortTodoTaskSerializer(
            obj
        ).data
    if obj._meta.label_lower == TodoStatus._meta.label_lower:
        data = ShortTodoStatusSerializer(
            obj
        ).data
    if obj._meta.label_lower == User._meta.label_lower:
        data = ShortUserSerializer(
            obj
        ).data
    if 'id' in data:
        del data['id']
    if 'created_at' in data:
        del data['created_at']
    if 'updated_at' in data:
        del data['updated_at']
    return request, data


@receiver(pre_save, sender=TodoStatus)
@receiver(pre_save, sender=TodoProject)
@receiver(pre_save, sender=TodoTask)
@receiver(pre_save, sender=User)
def pre_save_entity(sender, instance, raw, using, update_fields, **kwargs):
    if instance.pk is not None:
        request, old_data = get_data_and_request(sender.objects.get(pk=instance.pk))
        request, new_data = get_data_and_request(instance)
        try:
            if instance._meta.label_lower == TodoProject._meta.label_lower:
                obj_parent = instance
            else:
                if request.resolver_match.url_name == 'todo_projects-detail':
                    obj_parent = TodoProject.objects.get(pk=request.resolver_match.kwargs['pk'])
                else:
                    obj_parent = instance.project
        except:
            obj_parent = None
        diff_data = DeepDiff(old_data, new_data)
        if len(diff_data) > 0:
            TodoChange.objects.create(
                project=obj_parent,
                content_type=ContentType.objects.get(model=sender._meta.model_name),
                action='change',
                data_id=instance.pk,
                data=diff_data.json,
                user=request.user
            )


@receiver(post_save, sender=TodoStatus)
@receiver(post_save, sender=TodoProject)
@receiver(post_save, sender=TodoTask)
@receiver(post_save, sender=User)
def post_save_entity(sender, instance, raw, created, using, update_fields, **kwargs):
    if created:
        request, new_data = get_data_and_request(instance)
        try:
            if instance._meta.label_lower == TodoProject._meta.label_lower:
                obj_parent = instance
            else:
                if request.resolver_match.url_name == 'todo_projects-detail':
                    obj_parent = TodoProject.objects.get(pk=request.resolver_match.kwargs['pk'])
                else:
                    obj_parent = instance.project
        except:
            obj_parent = None
        TodoChange.objects.create(
            project=obj_parent,
            content_type=ContentType.objects.get(model=sender._meta.model_name),
            action='add',
            data_id=instance.pk,
            data=json.dumps(new_data),
            user=request.user
        )


@receiver(post_delete, sender=TodoStatus)
@receiver(post_delete, sender=TodoProject)
@receiver(post_delete, sender=TodoTask)
@receiver(post_delete, sender=User)
def post_delete_entity(sender, instance, using, **kwargs):
    request, data = get_data_and_request(instance)
    try:
        if instance._meta.label_lower == TodoProject._meta.label_lower:
            obj_parent = instance
        else:
            if request.resolver_match.url_name == 'todo_projects-detail':
                obj_parent = TodoProject.objects.get(pk=request.resolver_match.kwargs['pk'])
            else:
                obj_parent = instance.project
    except:
        obj_parent = None
    TodoChange.objects.create(
        project=obj_parent,
        content_type=ContentType.objects.get(model=sender._meta.model_name),
        action='delete',
        data_id=instance.pk,
        data=json.dumps(data),
        user=request.user
    )
