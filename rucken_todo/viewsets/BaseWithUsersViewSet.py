from __future__ import unicode_literals

from django.db.models import Q
from django.utils.timezone import now

from ..serializers import ShortUserSerializer
from . import BaseViewSet
from rest_framework import status
from rest_framework.response import Response
from numbers import Number


class BaseWithUsersViewSet(BaseViewSet):
    @staticmethod
    def create_user(data):
        if not isinstance(data, Number):
            if data is not None:
                data['id'] = int(data['id']) if data['id'] and int(data['id']) > 0 else None
                if data['id'] is not None:
                    user = ShortUserSerializer.Meta.model.objects.get(pk=data['id'])
                    user.username = data['username']
                    user.save()
                else:
                    user = list(ShortUserSerializer.Meta.model.objects.filter(
                        Q(email__iexact=data['email'])
                    )).first()
                    if user is None or user.id is None:
                        serializer = ShortUserSerializer(user)
                        data['is_superuser'] = False
                        data['password'] = data['username']
                        data['username'] = data['username']
                        data['first_name'] = ''
                        data['last_name'] = ''
                        data['is_staff'] = False
                        data['is_active'] = True
                        data['date_joined'] = now()
                        try:
                            user = serializer.create(data)
                        except:
                            return None
                return user.id
            else:
                return data
        return data

    def create(self, request, *args, **kwargs):
        if 'users' not in request.data:
            request.data['users'] = []
        request.data['users'] = list(filter(lambda x: x is not None,
                                       map(BaseWithUsersViewSet.create_user, request.data['users'])))
        request.data['users'].append(request.user.id)
        return super(BaseWithUsersViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if 'users' not in request.data:
            request.data['users'] = []
        items = list(self.model.objects.filter(users__id=request.user.id, id=request.data['id']))
        if request.user.id not in request.data['users'] and len(list(items)) == 0:
            return Response({'errors': 'Not access'}, status=status.HTTP_403_FORBIDDEN)
        request.data['users'] = list(filter(lambda x: x is not None, map(self.create_user, request.data['users'])))
        request.data['users'].append(request.user.id)
        return super(BaseWithUsersViewSet, self).update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.id:
            request.query_params.add('filter{users.id}', request.user.id)
        else:
            request.query_params.add('filter{users.id}', -1)

        result = super(BaseWithUsersViewSet, self).list(request, *args, **kwargs)
        return result
