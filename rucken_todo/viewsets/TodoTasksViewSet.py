from __future__ import unicode_literals

from ..serializers import TodoTaskSerializer
from . import BaseViewSet
from django.db.models import Q


class TodoTasksViewSet(BaseViewSet):
    model = TodoTaskSerializer.Meta.model
    serializer_class = TodoTaskSerializer
    queryset = TodoTaskSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(
                (Q(title__icontains=q) | Q(description__icontains=q))
            )
        return qs

    def list(self, request, *args, **kwargs):
        project_id = self.request.query_params.get('project')
        if project_id:
            request.query_params.add('filter{project}', project_id)
        else:
            request.query_params.add('filter{project}', -1)

        return super(TodoTasksViewSet, self).list(request, *args, **kwargs)
