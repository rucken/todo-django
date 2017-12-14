from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt import authentication

from ..permissions import CanChangeProfile
from ..models import User
from ..serializers import AccountSerializer


class AccountProfileUpdateAction(APIView):
    authentication_classes = (authentication.JSONWebTokenAuthentication,)
    permission_classes = (CanChangeProfile,)
    renderer_classes = (CamelCaseJSONRenderer,)
    serializer_class = AccountSerializer

    def post(self, request):
        user = User.objects.get(pk=request.user.pk)
        serializer = AccountSerializer(user)
        serializer.update(user, request.data)
        return Response(serializer.data)
