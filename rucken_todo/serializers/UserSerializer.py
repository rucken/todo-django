from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer,
    DynamicRelationField
)

from .GroupSerializer import GroupSerializer
from ..models import User


class UserSerializer(DynamicModelSerializer):
    groups = DynamicRelationField(GroupSerializer, many=True, embed=True)

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data['password'] = None
        return data

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'password',
            'last_login', 'date_joined', 'groups', 'date_of_birth')
        read_only_fields = (
            'last_login', 'date_joined',
            'is_superuser', 'is_staff', 'is_active'  # hard readonly
        )

    def create(self, validated_data):
        for field in self.Meta.read_only_fields:
            validated_data.pop(field, None)
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        if groups is not None:
            instance.groups = groups
        return instance

    def update(self, instance, validated_data):
        for field in self.Meta.read_only_fields:
            validated_data.pop(field, None)
        for attr, value in validated_data.items():
            if attr == 'password':
                if value is not None:
                    instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
