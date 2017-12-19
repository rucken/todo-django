from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicRelationField,
    DynamicModelSerializer)
from rest_framework_jwt.compat import PasswordField

from .ShortGroupSerializer import ShortGroupSerializer
from .UserSerializer import UserSerializer
from ..models import User


class AccountSerializer(DynamicModelSerializer):
    """
    Serializer class used to update user profile
    """

    def __init__(self, *args, **kwargs):
        super(AccountSerializer, self).__init__(*args, **kwargs)

    groups = DynamicRelationField(ShortGroupSerializer, many=True, embed=True)

    def to_representation(self, instance):
        data = super(AccountSerializer, self).to_representation(instance)
        data['password'] = None
        return data

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',
            'password', 'last_login', 'date_joined', 'groups', 'date_of_birth')
        read_only_fields = (
            'id', 'email', 'is_superuser', 'is_staff',
            'is_active', 'last_login', 'date_joined', 'groups'
        )

    def update(self, instance, validated_data):
        validated_data = validated_data.copy()
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