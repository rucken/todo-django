from __future__ import unicode_literals

from django.contrib.auth.models import Permission

from PermissionSerializer import PermissionSerializer


class ShortPermissionSerializer(PermissionSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'content_type', 'name', 'codename')
