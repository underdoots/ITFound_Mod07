# ------------------------------------------------- #
# Title: Assignment07
# Description: Example of error handling and pickling
# ChangeLog: (Who, When, What)
# ACollins,12.07.2020, Created script
# ------------------------------------------------- #

import pickle

"""Pickling demo"""

system_ID = int(input("Enter an ID "))
system_loc = str(input("Enter a research vessel "))
system_list = [system_ID, system_loc]
print (system_list)

#store data w/pickle dump
objFile = open("GO_systems.dat", "ab")
pickle.dump(system_list, objFile)
objFile.close()

#read data
objFile = open("GO_systems.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)

#error handling
# this first example was my attempt to check if the data were entered properly into the pickled file. incorrect.
# try:
#     if system_ID = >160 #system IDs do not exceed 160
#     print("There was an error! ")
#     elif system_ID = <160
#     print ("Cool ")

print ("Let's try to open the pH instrument database file ")
try:
    f=open("pH_inventory.datZ", "rb")
except: print("That file has not been created yet and you need to get to work!")

