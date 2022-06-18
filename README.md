<div align="center" style="display : flex; justify-content : center;">
  <h1>This is a MADAF project.</h1>
</div>

This is a default MADAF web application project. This project uses:
- ```madaf```
- ```madaf_http```

## How to Run:

Assuming that you already installed MADAF, type this:

Bash:

``` bash
$ madaf depen install hello_world
$ madaf run dev hello_world
```

Powershell:

``` powershell
> madaf depen install hello_world
> madaf run dev hello_world
```

Open [http://localhost:8080](http://localhost:8080) on the browser, you should see a text that said 'Hello, world!'. Note that you can build other kind of apps than just web apps.

## Directory Structure:

### ```./apps/```

This is where you are going to store your applications.

### ```./apps/[app_name]/main.py```

That file is the main entry point into your app.

### ```./configs/```

This is your configuration files, powered by Python.
In a nutshell, your configuration files are merely just 
a bunch of Python modules. Each subfolder belongs to it's 
respective application.

### ```./tests/```

This is your testing folder, each subfolder belongs to it's 
respective applcation.

### ```./madafrc.py```

This file stores the general configuration of the project.


