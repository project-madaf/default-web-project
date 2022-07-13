"""This is your app. This file has to exist!
"""

# Any class will be recognized as an app if the app's main class extends class
# StandardAppProperty, MiddlewareAppProperty, and PluginAppProperty. Simple as that.
from medaf.app.standard import StandardAppProperty
from medaf_http.route import route, handle_modify

class Main(StandardAppProperty):
    """This class has to exist, and the name is case-sensitive."""

    def response(self):
        """This function has to exist.
        This is the function that is going to give a response to MEDAF.
        """
        # Route a function called 'home' to a 'route name' called home.
        @route(route_name="home", content_type="text/plain")
        def home() -> str:
            return "Hello, world"

        return home

    def modify(self, **kwargs):
        """This function has to exist.
        This is the function that will be called if a middleware is trying to modify the
        response.
        """
        # medaf_http is going to handle the modifying stuff.
        handle_modify(kwargs)
