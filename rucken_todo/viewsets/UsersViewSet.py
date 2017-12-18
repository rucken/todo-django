from __future__ import unicode_literals

from ..serializers import UserSerializer
from . import BaseViewSet
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


class UsersViewSet(BaseViewSet):
    model = UserSerializer.Meta.model
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.queryset
        if q:
            qs = qs.filter(Q(username__icontains=q))
        return qs

    def list(self, request, *args, **kwargs):
        if not request.query_params.get('sort[]'):
            request.query_params.add('sort[]', ['-date_joined'])

        return super(UsersViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not self.has_model_permissions(request.user, self.model, ['change', 'manage']):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        user = UserSerializer.Meta.model.objects.get(pk=request.data['id'])
        serializer = UserSerializer(user)
        serializer.update(user, request.data)
        return Response(serializer.data)

