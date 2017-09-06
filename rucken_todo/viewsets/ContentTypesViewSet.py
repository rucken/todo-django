from __future__ import unicode_literals

from ..serializers import ContentTypeSerializer
from . import BaseViewSet
from django.db.models import Q


class ContentTypesViewSet(BaseViewSet):
    model = ContentTypeSerializer.Meta.model
    serializer_class = ContentTypeSerializer
    queryset = ContentTypeSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(
                (Q(model__icontains=q) | Q(app_label__icontains=q)) &
                (Q(app_label='auth') | Q(app_label='rucken_todo') | Q(app_label=''))
            )
        else:
            qs = qs.filter(
                (Q(app_label='auth') | Q(app_label='rucken_todo') | Q(app_label=''))
            )
        return qs
