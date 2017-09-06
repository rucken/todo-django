from __future__ import unicode_literals
from django.db import models

from User import User


class TodoProject(models.Model):
    title = models.TextField(max_length=512)
    description = models.TextField(max_length=512, null=True, blank=True)
    is_public = models.BooleanField(default=False, blank=True)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        permissions = (
            ("manage_todoproject", "Can manage project"),
            ("read_todoproject", "Can read project"),
        )
