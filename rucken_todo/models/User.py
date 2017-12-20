from django.db import models
import django.contrib.auth.models


class User(django.contrib.auth.models.AbstractUser):
    date_of_birth = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        permissions = (
            ("read_user", "Can read user"),
            ("read_group", "Can read group"),
            ("read_permission", "Can read permission"),
            ("read_contenttype", "Can read content type"),
            ("read_homepage", "Can read home page"),
            ("read_themespage", "Can read themes page"),
            ("read_accountpage", "Can read account page"),
            ("read_profileframe", "Can read profile frame"),
            ("read_adminpage", "Can read admin page"),
            ("read_groupsframe", "Can read groups frame"),
            ("read_usersframe", "Can read users frame"),
            ("read_projectspage", "Can read projects page"),
            ("read_projectsframe", "Can read projects frame"),
            ("change_profile", "Can change profile"),
        )