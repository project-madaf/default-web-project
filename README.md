# MEDAF Example Web Project

This is the official template for MEDAF Example Web Project. This template is minimal and only require a few set of plugin dependencies. The structure of the project is quite simple:

```text
./example/
    config.py
    main.py
./project.py
```

You can ignore other files, this is the only files that you need to focus at.

- ```./example/``` : This is a folder that contains an app called 'example'.
- ```./project.py``` : This file contains the general configuration of the project.

Each app folder contains a batch of files:

- ```main.py``` : Main entry-point to your program.
- ```config.py``` : App behaviour configuration.
- ```routing.py``` : App routing configuration.

Now, to run the project, follow this steps:

- Make sure that debug mode is on.

```python
# project.py

# This will add a few methods that you can use.
from medaf.conf.app import AppConfigProperty

class Main(AppConfigProperty):
    """This will configure your app. The name has to be named 'Main'!"""

    def main(self) -> None:
        ........

        # Set port.
        self.port = 8080

        # Set host.
        self.host = '0.0.0.0'

        # Set debug mode. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.debug = True

```

And then, run the app via MEDAF project command line utillity:

```bash
medaf-project run example # Run this command in the root directory of the project!
```
