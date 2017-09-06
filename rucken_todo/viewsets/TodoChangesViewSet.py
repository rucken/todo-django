from __future__ import unicode_literals

from ..serializers import TodoChangeSerializer
from ..models.TodoProject import TodoProject
from ..models.TodoTask import TodoTask
from ..models.TodoStatus import TodoStatus
# from ..models.User import User
from . import BaseViewSet
from django.db.models import Q


class TodoChangesViewSet(BaseViewSet):
    model = TodoChangeSerializer.Meta.model
    serializer_class = TodoChangeSerializer
    queryset = TodoChangeSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(
                (Q(old_data__icontains=q) | Q(new_data__icontains=q) | Q(action__icontains=q)) &
                (Q(content_type__name=TodoProject._meta.model_name))
            )
        else:
            qs = qs.filter(
                (
                    # Q(content_type__model=User._meta.model_name) |
                    Q(content_type__model=TodoProject._meta.model_name) |
                    Q(content_type__model=TodoTask._meta.model_name) |
                    Q(content_type__model=TodoStatus._meta.model_name)
                ) &
                (
                    Q(project__users__id=self.request.user.pk)
                )
            )
        return qs

    def list(self, request, *args, **kwargs):
        project_id = self.request.query_params.get('project')
        if project_id:
            request.query_params.add('filter{project}', project_id)
        else:
            request.query_params.add('filter{project}', -1)
        content_type_id = self.request.query_params.get('content_ype')
        if content_type_id:
            request.query_params.add('filter{content_type}', content_type_id)
        user_id = self.request.query_params.get('user')
        if user_id:
            request.query_params.add('filter{user}', user_id)

        return super(TodoChangesViewSet, self).list(request, *args, **kwargs)
