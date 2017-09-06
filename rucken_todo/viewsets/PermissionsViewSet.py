from __future__ import unicode_literals

from ..serializers import PermissionSerializer
from . import BaseViewSet
from django.db.models import Q


class PermissionsViewSet(BaseViewSet):
    model = PermissionSerializer.Meta.model
    serializer_class = PermissionSerializer
    queryset = PermissionSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(
                (Q(codename__icontains=q) | Q(name__icontains=q)) &
                (Q(content_type__app_label='auth') | Q(content_type__app_label='rucken_todo'))
            )
        else:
            qs = qs.filter(
                (Q(content_type__app_label='auth') | Q(content_type__app_label='rucken_todo'))
            )
        return qs
