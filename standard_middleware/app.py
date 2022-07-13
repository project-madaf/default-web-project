"""This is your app. This file has to exist!
"""

# Any class will be recognized as an app if the app's main class extends class
# StandardAppProperty, MiddlewareAppProperty, and PluginAppProperty. Simple as that.
from medaf.app.middleware import StandardMiddlewareProperty

class Main(StandardMiddlewareProperty):
    """This class has to exist, and the name is case-sensitive."""

    def request(self):
        """This function has to exist. This is where you interact with the request data.
        NOTE: You can not interact with any response data. Because it is unavailable!"""
        # Get the path.
        self.request_path: str | None = self.get_gateway_request(type="path")

        # Check the path. If the path is '/', redirect to '/home'.
        if self.request_path == '/':
            self.modify_gateway_request(type='path', value='/home')

    def response(self):
        """This function has to exist. This is where you interact with the response data.
        NOTE: All request data is unavailable."""
        # Get the response data.
        self.status_code: str = self.get_app_response(type="status")

        # Change the status code from 200 OK to 404 Not Found.
        if self.status_code == '200 OK':
            self.modify_app_response(type='status', value='404 Not Found')
