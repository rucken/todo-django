from __future__ import unicode_literals
from django.apps import AppConfig


class RuckenTodoConfig(AppConfig):
    name = 'rucken_todo'

    def ready(self):
        from . import signals