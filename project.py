"""This will configure your project.
"""

from medaf.conf.project import ProjectConfigProperty

class Main(ProjectConfigProperty):
    """This class has to be defined, and the name is case-sensitive."""

    def main(self) -> None:
        """This function has to be defined, and the name is case-sensitive."""

        # Configure your installed apps. WARNING: The order of your installed plugins matters!
        # If an app 'example' uses an app called 'example1', load 'example1' first!
        self.installed_apps = ['standard_app']

        # This will configure your installed plugins, use your plugin's package name.
        # MEDAF plugin is a Python package that contains a MEDAF standard app. WARNING: The
        # order of your installed plugins matters! For example, a plugin called 'example' uses a
        # plugin called 'example1', load 'example1' first!
        self.installed_plugins = ['medaf_http']

        # Configure your installed middleware, use your middleware's package name. WARNING: The
        # order of your installed middleware matters! For example, middleware called 'example'
        # uses a middleware called 'example1', load 'example1' first!
        self.installed_middleware = []
