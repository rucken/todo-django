from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer,
    DynamicRelationField
)

from ..models import TodoProject
from ShortUserSerializer import ShortUserSerializer
from ShortTodoStatusSerializer import ShortTodoStatusSerializer


class TodoProjectSerializer(DynamicModelSerializer):
    users = DynamicRelationField(ShortUserSerializer, many=True, embed=True)
    statuses = DynamicRelationField(ShortTodoStatusSerializer, source='todostatus_set', many=True,
                                    embed=True)

    class Meta:
        model = TodoProject
        fields = ('id', 'title', 'description', 'is_public', 'users', 'statuses', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'statuses')
