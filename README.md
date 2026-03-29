This is a simple python project for managing the history of Ipython (Interactive python)

IPython is an interactive version of python that runs inside the terminal. It is incredibly usefull to quickly test small lines of code or run small calculations. BUT did you know, ipython stores every single line of code you run and you still have to import scientific constants!!.

this project aims to stop storing every line and automatically import scientific constants and modules.... or any variables and modules the user wants.

If you have any issues when using program or want to provide feedback you can contact me at: leogreggallured@gmail.com

repo : https://github.com/LGregg-Allured/IPython-History-Manager/tree/main
version : 0.2.2 
Owner : LGregg-Allured

This version 0.2.2 is designed to be dropped into the startup directory for Ipython, and the path to the Ipython defualt profile is to be entered into the config.toml file.


INSTRUCTIONS FOR USE:


1. drop the files in "startup" into the startup directory located in the .ipython parent directory.

The ipython (usually hidden) directory can oftenly be found from the following path: "/home/user/.ipython/profile and the startup directory is located there too.

2. Edit the path in the config file to your profile directory for ipython NOTE: this directory will contain the startup folder.

3. Edit/add variables and constants you want to the config.toml file, there are already two examples loaded. This example is also shown below.

[variables]
pi = 3.14159
e = 1.6e-19