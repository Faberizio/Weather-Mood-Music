# user/middleware/logout_mw.py
from django.contrib.auth.signals import user_logged_out
import logging

class LogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        user_logged_out.connect(self.user_logged_out_callback)  # Connect to the logout signal
        response = self.get_response(request)
        return response

    def user_logged_out_callback(self, sender, request, user, **kwargs):
        # Log the user logout here
        self.logger.info(f"User '{user.username}' logged out from {request.META['REMOTE_ADDR']}")
