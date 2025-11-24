import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RouteAccessLogMiddleware:
    """ Logs every user access to any route. """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user.username if request.user.is_authenticated else "Anonymous"

        log_message = (
            f"[{datetime.now()}] "
            f"User: {user} "
            f"Method: {request.method} "
            f"Path: {request.path} "
            f"IP: {self.get_client_ip(request)}"
        )

        logger.info(log_message)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
