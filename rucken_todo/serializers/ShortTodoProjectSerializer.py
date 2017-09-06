from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicModelSerializer
)

from ..models import TodoProject


class ShortTodoProjectSerializer(DynamicModelSerializer):

    class Meta:
        model = TodoProject
        fields = ('id', 'title', 'description', 'is_public', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'statuses')
