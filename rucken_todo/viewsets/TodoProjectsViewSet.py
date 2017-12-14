from __future__ import unicode_literals

from numbers import Number

from django.db.models import Q

from . import BaseWithUsersViewSet
from ..serializers import TodoProjectSerializer
from ..serializers import TodoStatusSerializer


class TodoProjectsViewSet(BaseWithUsersViewSet):
    @staticmethod
    def create_status(data, project):
        if not isinstance(data, Number):
            if data is not None:
                data['id'] = int(data['id']) if data['id'] and int(data['id']) > 0 else None
                if data['id'] is not None:
                    status = TodoStatusSerializer.Meta.model.objects.get(pk=data['id'])
                else:
                    statuses = list(TodoStatusSerializer.Meta.model.objects.filter(
                        Q(name__iexact=data['name'], project=project)
                    ))
                    if len(statuses):
                        status = statuses[0]
                    else:
                        status = None
                    if status is None or status.id is None:
                        serializer = TodoStatusSerializer(status)
                        data['project'] = project
                        try:
                            status = serializer.create(data)
                        except:
                            return None
                return status.id
            else:
                return data
        return data

    model = TodoProjectSerializer.Meta.model
    serializer_class = TodoProjectSerializer
    queryset = TodoProjectSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(
                (Q(title__icontains=q) | Q(description__icontains=q))
            )
        return qs

    def create(self, request, *args, **kwargs):
        if 'statuses' not in request.data:
            statuses = []
        else:
            statuses = request.data.pop('statuses')
        result = super(TodoProjectsViewSet, self).create(request, *args, **kwargs)
        project = TodoProjectSerializer.Meta.model.objects.get(pk=result.data['todo_project']['id'])
        project.todostatus_set.all().exclude(id__in=map(TodoProjectsViewSet.create_status, statuses,
                                                        [project for x in range(0, len(statuses))])).delete()
        return self.to_response(project)

    def update(self, request, *args, **kwargs):
        if 'statuses' not in request.data:
            statuses = []
        else:
            statuses = request.data.pop('statuses')
        result = super(TodoProjectsViewSet, self).update(request, *args, **kwargs)
        project = TodoProjectSerializer.Meta.model.objects.get(pk=result.data['todo_project']['id'])
        project.todostatus_set.all().exclude(id__in=map(TodoProjectsViewSet.create_status, statuses,
                                                        [project for x in range(0, len(statuses))])).delete()
        return self.to_response(project)
