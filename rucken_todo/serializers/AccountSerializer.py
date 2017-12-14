from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicRelationField
)

from .ShortGroupSerializer import ShortGroupSerializer
from .UserSerializer import UserSerializer
from ..models import User


class AccountSerializer(UserSerializer):
    """
    Serializer class used to update user profile
    """

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

    groups = DynamicRelationField(ShortGroupSerializer, many=True, embed=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',
            'password', 'last_login', 'date_joined', 'groups', 'date_of_birth')
        read_only_fields = (
            'id', 'email', 'is_superuser', 'is_staff',
            'is_active', 'last_login', 'date_joined', 'groups'
        )
