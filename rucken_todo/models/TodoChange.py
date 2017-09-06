from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import CASCADE, SET_NULL

from User import User
from TodoProject import TodoProject


class TodoChange(models.Model):
    project = models.ForeignKey(TodoProject, on_delete=SET_NULL, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True, blank=True)
    action = models.TextField(max_length=100, null=True, blank=True)
    data_id = models.TextField(max_length=100, null=True, blank=True)
    data = models.TextField(max_length=4000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        permissions = (
            ("manage_todochange", "Can manage change"),
            ("read_todochange", "Can read change"),
        )
