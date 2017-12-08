from __future__ import unicode_literals

from dynamic_rest.fields import DynamicRelationField
from dynamic_rest.serializers import (
    DynamicModelSerializer
)

from ..models import TodoTask
from .ShortTodoStatusSerializer import ShortTodoStatusSerializer
from .ShortTodoProjectSerializer import ShortTodoProjectSerializer


class TodoTaskSerializer(DynamicModelSerializer):
    status = DynamicRelationField(ShortTodoStatusSerializer, embed=True)
    project = DynamicRelationField(ShortTodoProjectSerializer, embed=True)

    class Meta:
        model = TodoTask
        fields = ('id', 'project', 'title', 'description', 'status', 'open_at', 'close_at', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
