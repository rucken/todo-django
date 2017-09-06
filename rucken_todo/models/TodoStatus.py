from __future__ import unicode_literals
from django.db import models
from django.db.models import CASCADE

from TodoProject import TodoProject


class TodoStatus(models.Model):
    project = models.ForeignKey(TodoProject, on_delete=CASCADE)
    name = models.TextField(max_length=512)
    title = models.TextField(max_length=512, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        permissions = (
            ("manage_todostatus", "Can manage status"),
            ("read_todostatus", "Can read status"),
        )
