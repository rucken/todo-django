from __future__ import unicode_literals

from dynamic_rest.fields import DynamicRelationField
from dynamic_rest.serializers import (
    DynamicModelSerializer
)

from .ShortTodoProjectSerializer import ShortTodoProjectSerializer
from .ContentTypeSerializer import ContentTypeSerializer
from .UserSerializer import UserSerializer
from ..models import TodoChange


class TodoChangeSerializer(DynamicModelSerializer):
    project = DynamicRelationField(ShortTodoProjectSerializer, embed=True)
    user = DynamicRelationField(UserSerializer, embed=True)
    content_type = DynamicRelationField(ContentTypeSerializer, embed=True)

    class Meta:
        model = TodoChange
        fields = (
            'id', 'project', 'content_type', 'action', 'data_id', 'data', 'user', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
