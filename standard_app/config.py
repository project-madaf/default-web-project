"""This will configure your app.
"""

# This will add a few methods that you can use.
from medaf.conf.apps import AppConfigProperty

class Main(AppConfigProperty):
    """This will configure your app. The name has to be named 'Main'!"""

    def main(self):
        """'main' function has to be defined!"""

        # Set your app type. It could be standard or middleware.
        self.app_type = "standard"

        # Some sort of alias name.
        self.alias = "standard"

        # Set routing. This config will be used by medaf_http.
        self.route = {
            "/home":"home"
        }
