# MEDAF Default Web Project

This is the official template for MEDAF Default Web Project. This template is minimal and only require a few set of plugin dependencies. The structure of the project is quite simple:

```
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

Now, to run the project:

```bash
medaf run example # Run this command in the root directory of the project!
```