# file Handling in python is used to read and write files.

# f = open("ankit.txt",)
# print(f.read())

# open() function is used to open a file.
# open() function takes two arguments, the file name and the mode.
# mode is optional, if not specified, it defaults to 'r' (read mode).
# mode can be 'r' (read mode), 'w' (write mode), 'a' (append mode), 'x' (create mode), 'b' (binary mode), 't' (text mode), '+' (read and write mode).
# mode can be 'r' (read mode), 'w' (write mode), 'a' (append mode), 'x' (create mode), 'b' (binary mode), 't' (text mode), '+' (read and write mode).

'''
using with statement
you can also use the with statement to open a file.
'''

with open("ankit.txt", "r") as f:
    print(f.read())


# close file
# It is good practice to always close the file when you are done with it.
# if you are using with statement, you don't need to close the file.
f.close() # this will close the file

# You should always close your file, in some cases, due to buffering, changes made to a file may not show until you 
# close the file.

# read only parts of the file
# By default the read() method returns the whole text, but you can also specify the number of characters you want to return.

h = open("ankit2.txt")
# print(h.read(1))  # this will read the first character of the file

# print(h.read(5)) # this will read the first 5 characters of the file


# read line 
# you can return one line by using the readline() method.
print(h.readline()) # this will read the first line of the file

print(h.readline()) # this will read the second line of the file


# By calling readline() two times, you can read the two first lines of the file, like this:

# read two lines of the file


# by looping through the file you can read the whole file, line by line
with open("ankit2.txt") as f:
    for x in f:
        print(x)
'''
Python file write 
write to an existing file
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''

with open("ankit2.txt", "a") as f:
    f.write("I am from mumbai")
    f.write("this is extra line")

with open("ankit.txt", "w") as f:
    f.write("I am from mumbai")


# create a new file
# f = open("ankit3.txt", "x")
# f.write("I am from mumbai ")
# f.write("this is extra line")
# f.close()

import os
# delete a file

# to delete a file you can use the os module

# os.remove("ankit3.txt")
# print("File deleted successfully")

# check if file exists
if os.path.exists("ankit4.txt"):
    os.remove("ankit4.txt")
    print("File deleted successfully")
else:
    print("file does not exist")

# delete folder
os.rmdir("ankitFolder")
print("Folder deleted successfully")  # you can remove  empty folder
