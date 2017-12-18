from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from rucken_todo.actions import AccountProfileUpdateAction
from rucken_todo.viewsets import router
from rucken_todo.swagger import get_swagger_view

schema_view = get_swagger_view(title='Rucken: Todo', url='/api/', patterns=[
    url(r'^account/login', obtain_jwt_token),
    url(r'^account/info', verify_jwt_token),
    url(r'^account/update', AccountProfileUpdateAction.as_view()),
    url(r'^', include(router.urls))
])

urlpatterns = [
    url(r'^api/account/login', obtain_jwt_token),
    url(r'^api/account/info', verify_jwt_token),
    url(r'^api/account/update', AccountProfileUpdateAction.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^swagger', schema_view)
]

if settings.DEBUG:
    urlpatterns += static('/css/', document_root='app/staticfiles/css/')
    urlpatterns += static('/img/', document_root='app/staticfiles/img/')
    urlpatterns += static('/js/', document_root='app/staticfiles/js/')
