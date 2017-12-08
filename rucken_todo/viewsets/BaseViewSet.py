from __future__ import unicode_literals

from dynamic_rest.viewsets import DynamicModelViewSet
from dynamic_rest.renderers import DynamicBrowsableAPIRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

from dynamic_rest.conf import settings


class DynamicPageNumberPagination(PageNumberPagination):
    """A subclass of PageNumberPagination.

    Adds support for pagination metadata and overrides for
    pagination query parameters.
    """
    page_size_query_param = settings.PAGE_SIZE_QUERY_PARAM
    page_query_param = settings.PAGE_QUERY_PARAM
    max_page_size = settings.MAX_PAGE_SIZE
    page_size = settings.PAGE_SIZE or api_settings.PAGE_SIZE

    def get_page_metadata(self):
        # returns total_results, total_pages, page, per_page
        return {
            'total_results': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            self.page_query_param: self.page.number,
            self.page_size_query_param: self.get_page_size(self.request)
        }

    def get_paginated_response(self, data):
        meta = self.get_page_metadata()
        if 'meta' in data:
            data['meta'].update(meta)
        else:
            data['meta'] = meta
        return Response(data)


class BaseViewSet(DynamicModelViewSet):
    pagination_class = DynamicPageNumberPagination
    renderer_classes = (CamelCaseJSONRenderer, DynamicBrowsableAPIRenderer)

    def has_model_permissions(self, entity, model, perms, app):
        for p in perms:
            if entity.has_perm("%s.%s_%s" % (app.lower(), p.lower(), model.__name__.lower())):
                return True
        return False

    def create(self, request, *args, **kwargs):
        if not self.has_model_permissions(request.user, self.model, ['add', 'manage'], self.model._meta.app_label):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(BaseViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not self.has_model_permissions(request.user, self.model, ['change', 'manage'], self.model._meta.app_label):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(BaseViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not self.has_model_permissions(request.user, self.model, ['delete', 'manage'], self.model._meta.app_label):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(BaseViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if not self.has_model_permissions(request.user, self.model, ['read', 'manage'], self.model._meta.app_label):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(BaseViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not request.query_params.get('cur_page'):
            request.query_params.add('cur_page', 1)
        if not request.query_params.get('per_page'):
            request.query_params.add('per_page', 10)
        if not request.query_params.get('sort[]'):
            request.query_params.add('sort[]', ['-id'])
        if not self.has_model_permissions(request.user, self.model, ['read', 'manage'], self.model._meta.app_label):
            return Response({'errors': 'Not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(BaseViewSet, self).list(request, *args, **kwargs)

    def to_response(self, obj):
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
