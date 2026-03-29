#this is a simple python file designed to delete the history from ipython
#Leo Gregg-Allured
#leogreggallured@gmail.com

#Version: 0.2.0-alpha.1
#Build n0: 2

#imports

import tomllib
import os

#load infomation from the config file
with open("config.toml","rb") as f:
    config = tomllib.load(f)

path = config['path']

#delete the histroy.sqlite file
os.remove(path+"/history.sqlite")