from __future__ import unicode_literals

from ..serializers import GroupSerializer
from . import BaseViewSet
from django.db.models import Q


class GroupsViewSet(BaseViewSet):
    model = GroupSerializer.Meta.model
    serializer_class = GroupSerializer
    queryset = GroupSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(Q(name__icontains=q))
        return qs
