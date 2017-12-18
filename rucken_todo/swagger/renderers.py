from __future__ import absolute_import, division, print_function, unicode_literals

from django.core.urlresolvers import reverse
from rest_framework_swagger import renderers
from rest_framework_swagger.settings import swagger_settings


class OpenAPIRenderer(renderers.OpenAPIRenderer):
    def get_customizations(self):
        data = super(OpenAPIRenderer, self).get_customizations()
        return data


class SwaggerUIRenderer(renderers.SwaggerUIRenderer):
    template = 'swagger_index.html'

    def get_ui_settings(self):
        data = {
            'apisSorter': swagger_settings.APIS_SORTER,
            'docExpansion': swagger_settings.DOC_EXPANSION,
            'jsonEditor': swagger_settings.JSON_EDITOR,
            'operationsSorter': swagger_settings.OPERATIONS_SORTER,
            'showRequestHeaders': swagger_settings.SHOW_REQUEST_HEADERS,
            'supportedSubmitMethods': swagger_settings.SUPPORTED_SUBMIT_METHODS
        }
        if swagger_settings.VALIDATOR_URL != '':
            data['validatorUrl'] = swagger_settings.VALIDATOR_URL
        return data