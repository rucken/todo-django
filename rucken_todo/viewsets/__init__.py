from __future__ import unicode_literals

from dynamic_rest.routers import DynamicRouter

from .BaseViewSet import *
from .BaseWithUsersViewSet import *
from .ContentTypesViewSet import *
from .GroupsViewSet import *
from .PermissionsViewSet import *
from .UsersViewSet import *
from .TodoProjectsViewSet import *
from .TodoTasksViewSet import *
from .TodoStatusesViewSet import *
from .TodoChangesViewSet import *

# Routers provide an easy way of automatically determining the URL conf.
router = DynamicRouter()
router.register_resource(UsersViewSet)
router.register_resource(PermissionsViewSet)
router.register_resource(ContentTypesViewSet)
router.register_resource(GroupsViewSet)
router.register_resource(TodoProjectsViewSet)
router.register_resource(TodoTasksViewSet)
router.register_resource(TodoStatusesViewSet)
router.register_resource(TodoChangesViewSet)
