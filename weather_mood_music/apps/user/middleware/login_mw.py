# user/middleware/login_mw.py
from django.contrib.auth.signals import user_logged_in
import logging

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        user_logged_in.connect(self.user_logged_in_callback)  # Connect to the login signal
        response = self.get_response(request)
        return response

    def user_logged_in_callback(self, sender, request, user, **kwargs):
        # Log the user login here
        self.logger.info(f"User '{user.username}' logged in from {request.META['REMOTE_ADDR']}")
