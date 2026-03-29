#this is a simple python file designed to delete the history from ipython
#Leo Gregg-Allured
#leogreggallured@gmail.com
#https://github.com/LGregg-Allured/IPython-History-Manager

#Version: 0.2.2
#Build n0: 6

#imports

import tomllib
import os

#load infomation from the config file
with open("config.toml","rb") as f:
    config = tomllib.load(f)

path = config['path'] #defining the path to variable "path"

#delete the histroy.sqlite file
os.remove(path+"/history.sqlite") # concatenates path and "..." to get the path to the history file.

#import variables:

variables = config['variables'] # saves the dictionary for variables internally

for name, value in variables.items(): # loop over all variables
    globals()[name] = value # creates new entry in globals variable dictionary