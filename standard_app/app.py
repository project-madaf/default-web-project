"""This is your app. This file has to exist!
"""

from medaf.project.app import StandardAppProperty
from medaf_http.route import route

class Main(StandardAppProperty):
    """This class has to exist, and the name is case-sensitive."""

    def main(self) -> None:
        """This function has to exist.
        This is your app program. This function is where you write codes.
        """
        # Route a function called 'home' to a 'route name' called home.
        @route(route_name='home')
        def home() -> str:
            return "Hello, world"
