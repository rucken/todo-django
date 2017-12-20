from __future__ import unicode_literals

import django.contrib.contenttypes.models
from django.db import models
from django.db.models import CASCADE, SET_NULL

from .TodoProject import TodoProject
from .User import User


class TodoChange(models.Model):
    project = models.ForeignKey(TodoProject, on_delete=SET_NULL, null=True, blank=True)
    content_type = models.ForeignKey(django.contrib.contenttypes.models.ContentType, on_delete=CASCADE, null=True,
                                     blank=True)
    action = models.TextField(max_length=100, null=True, blank=True)
    data_id = models.TextField(max_length=100, null=True, blank=True)
    data = models.TextField(max_length=4000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        permissions = (
            ("manage_todochange", "Can manage change"),
            ("read_todochange", "Can read change"),
        )
