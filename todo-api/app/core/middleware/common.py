from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from core.views import maintenance_view


class MaintenanceModeMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        if settings.MAINTENANCE_MODE:
            return maintenance_view(request)
