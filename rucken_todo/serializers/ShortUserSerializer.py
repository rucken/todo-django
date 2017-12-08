from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicRelationField
)

from .ShortGroupSerializer import ShortGroupSerializer
from .UserSerializer import UserSerializer
from ..models import User


class ShortUserSerializer(UserSerializer):
    groups = DynamicRelationField(ShortGroupSerializer, many=True, embed=True)

    def to_representation(self, instance):
        data = super(ShortUserSerializer, self).to_representation(instance)
        if 'password' in data:
            del data['password']
        return data

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'date_of_birth')
        read_only_fields = ('id', 'email', 'is_superuser', 'is_staff', 'is_active',
                            'last_login', 'date_joined', 'groups')
