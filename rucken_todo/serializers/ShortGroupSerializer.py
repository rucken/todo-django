from __future__ import unicode_literals

from dynamic_rest.serializers import (
    DynamicRelationField
)
from ShortPermissionSerializer import ShortPermissionSerializer
from GroupSerializer import GroupSerializer


class ShortGroupSerializer(GroupSerializer):
    permissions = DynamicRelationField(ShortPermissionSerializer, many=True, embed=True)
