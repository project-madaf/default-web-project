"""This will configure your app.
"""

from medaf.conf.app import AppConfigProperty

class Main(AppConfigProperty):
    """This will configure your app. The name has to be named 'Main'!"""

    def main(self) -> None:
        """'main' function has to be defined!"""

        # Set your app type. It could be standard or middleware.
        self.app_type = "standard"

        # Set routing. This config will be used by medaf_http.
        self.route = {
            '/':'home'
        }

        # Set port.
        self.port = 8080

        # Set host.
        self.host = '0.0.0.0'
