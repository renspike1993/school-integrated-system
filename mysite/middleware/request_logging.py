import logging
from django.utils.deprecation import MiddlewareMixin

# Get the Django request logger
request_logger = logging.getLogger("django.request")

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        try:
            # Get user info
            user = request.user.username if hasattr(request, "user") and request.user.is_authenticated else "Anonymous"
            ip = request.META.get("REMOTE_ADDR")
            method = request.method
            path = request.get_full_path()
            status_code = response.status_code

            # Get request data (POST or GET)
            data = request.POST.dict() if request.method == "POST" else request.GET.dict()

            # Prepare structured extra data
            extra_data = {
                "user": user,
                "ip": ip,
                "method": method,
                "path": path,
                "status_code": status_code,
                "data": data
            }

            # Create a log message including the data
            log_message = f"[{user}] {method} {path} from {ip} -> {status_code} | Data: {data}"

            # Log it
            request_logger.info(log_message, extra=extra_data)

        except Exception as e:
            # Fail silently to not break responses
            request_logger.error(f"Failed to log request: {e}")

        return response
