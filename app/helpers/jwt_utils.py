from __future__ import unicode_literals
from rucken_todo.serializers import AccountSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    user_info = AccountSerializer(user, context={'request': request})
    return {
        'token': token,
        'user': user_info.data
    }
