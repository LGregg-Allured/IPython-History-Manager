#this is a simple python file designed to delete the history from ipython
#Leo Gregg-Allured
#leogreggallured@gmail.com

#Version: 0.1.0-alpha.1
#Build n0: 1

#notes for myself:
#Better variable names for ("string"), etc

import os

#Clearing the old history:

#navigating to the location of history file: 

Path = os.getcwd() #gets the path to the startup directory
Path_List = Path.split(os.sep)# converts path to a list
Path_List.pop(len(Path_List)-1)#removes the last directory in the list

string = ("") 
for i in range (len(Path_List)): # for loop to generate list from the path to the ipython directory
    string += (Path_List[i]) + "/" # defines the string as the path list items concatenated with "/" to create a string of the path to history file
string += "history.sqlite" #concatenates the file onto the file path

os.remove(string) # deletes the history.sqlite file