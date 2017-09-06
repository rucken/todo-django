from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer
)
from django.contrib.contenttypes.models import ContentType


class ContentTypeSerializer(DynamicModelSerializer):

    def to_internal_value(self, data):
        if 'name' in data and data['name']:
            data['model'] = data['name']
        instance = super(ContentTypeSerializer, self).to_internal_value(data)
        return instance

    def to_representation(self, instance):
        data = super(ContentTypeSerializer, self).to_representation(instance)
        if 'model' in data and data['model']:
            data['title'] = data['model']
            data['name'] = data['model']
            del data['model']
        return data

    class Meta:
        model = ContentType
        fields = ('id', 'model')
        read_only_fields = ()
