from django.views.decorators.csrf import csrf_exempt
from django.db import models
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from .renderers import OpenAPIRenderer, SwaggerUIRenderer

def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
    """
    Returns schema view which renders Swagger/OpenAPI.
    """
    class SwaggerSchemaView(APIView):
        _ignore_model_permissions = True
        exclude_from_schema = True
        permission_classes = [AllowAny]
        renderer_classes = [
            CoreJSONRenderer,
            OpenAPIRenderer,
            SwaggerUIRenderer
        ]

        def get(self, request):
            generator = SchemaGenerator(
                title=title,
                url=url,
                patterns=patterns,
                urlconf=urlconf
            )
            schema = generator.get_schema(request=request)

            if not schema:
                raise exceptions.ValidationError(
                    'The schema generator did not return a schema Document'
                )

            return Response(schema)

    return SwaggerSchemaView.as_view()
