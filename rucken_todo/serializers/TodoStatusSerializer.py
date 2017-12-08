from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer
)

from ..models import TodoStatus


class TodoStatusSerializer(DynamicModelSerializer):
    class Meta:
        model = TodoStatus
        fields = ('id', 'project', 'name', 'title', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
