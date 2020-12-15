# Using Pickling and Exception Handling in Python
## Introduction
Pickling is a process where the programmer converts an object into a byte stream (to me this sounds similar to zipping or compressing a folder/file); unpickling is the process of unpacking the data in that object. One important thing to keep in mind is that pickling and unpickling can be subject to security risks, where someone could insert malicious code into a pickled object and when another user unpickles it, they are subject to a malicious attack. I found this link to be a succinct and easy to understand demonstration of pickling. 

I found this concept a lot easier to understand than previous ones, because I think it might be more in line with the type of work I might be applying Python to. I’d like to expand upon the error handling to apply it to the data entered into the pickled database, but for now I will try to get this assignment submitted ASAP. 


Exception handling is a useful way to catch errors or mistakes in your code. I found this website to provide a useful example of how it can be used. By writing in exceptions to code, the programmer can make sure errors are caught and the remaining code is not run before they’re corrected.

## Code

```
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

