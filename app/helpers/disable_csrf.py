from __future__ import unicode_literals


class DisableCSRF(object):

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
