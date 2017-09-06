from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer,
    DynamicRelationField
)
from django.contrib.auth.models import Permission

from ContentTypeSerializer import ContentTypeSerializer


class PermissionSerializer(DynamicModelSerializer):
    content_type = DynamicRelationField(ContentTypeSerializer, embed=True)

    def to_internal_value(self, data):
        if 'name' in data and data['name']:
            data['codename'] = data['name']
        if 'title' in data and data['title']:
            data['name'] = data['title']
        instance = super(PermissionSerializer, self).to_internal_value(data)
        return instance

    def to_representation(self, instance):
        data = super(PermissionSerializer, self).to_representation(instance)
        if 'name' in data and data['name']:
            data['title'] = data['name']
        if 'codename' in data and data['codename']:
            data['name'] = data['codename']
            del data['codename']
        return data

    class Meta:
        model = Permission
        fields = ('id', 'content_type', 'name', 'codename')
