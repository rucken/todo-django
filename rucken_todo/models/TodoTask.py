from __future__ import unicode_literals

from django.db import models
from django.db.models import CASCADE, PROTECT

from .TodoProject import TodoProject
from .TodoStatus import TodoStatus


class TodoTask(models.Model):
    project = models.ForeignKey(TodoProject, on_delete=CASCADE)
    title = models.TextField(max_length=512)
    description = models.TextField(max_length=512, null=True, blank=True)
    status = models.ForeignKey(TodoStatus, on_delete=PROTECT)
    open_at = models.DateTimeField(null=True, blank=True)
    close_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        permissions = (
            ("manage_todotask", "Can manage task"),
            ("read_todotask", "Can read task"),
        )
