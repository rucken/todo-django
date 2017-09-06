from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer
)

from ..models import TodoTask


class ShortTodoTaskSerializer(DynamicModelSerializer):

    class Meta:
        model = TodoTask
        fields = ('id', 'project', 'title', 'description', 'status', 'open_at', 'close_at', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
