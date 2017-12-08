from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer,
    DynamicRelationField
)
from django.contrib.auth.models import Group
from .PermissionSerializer import PermissionSerializer


class GroupSerializer(DynamicModelSerializer):
    permissions = DynamicRelationField(PermissionSerializer, many=True, embed=True)

    def to_representation(self, instance):
        data = super(GroupSerializer, self).to_representation(instance)
        if 'name' in data and data['name']:
            data['title'] = data['name']
            data['name'] = data['name']
        return data

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')
