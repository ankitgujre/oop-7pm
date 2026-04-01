'''
Regular Expression

RegExp a regular expression is a sequence of characters that forms a search pattern. 
Regular expressions can be used to check if a string contains the specified search pattern.
used to find and replace patterns in strings.
'''

# Python has a built in package called re, which can be used to work with regular expressions.
# import re

import re

# txt = "the rain in India"
'''
The search() function searches the string for a match and return a Match object if there is a match

if there more than is one match  onlythe first occurence of the match will be returned
'''
# # x = re.search("^The.*India$", txt)  #  None

# x = re.search("^the.*India$", txt)
# print(x)  # this will print an object

''' The findall() function

The findall() function returns a list containing all matches
'''

# txt = "The India is inside asia in a world"

# x = re.findall("in", txt)
# data = re.search("\s", txt)   # where is first space search for the first white space
# data = re.search("Bhopal", txt)


# print(x)
# print(data)

# print("The first white space is located in", data.start())

'''
the split() function

the split() function returns a list where the string has been split at each match
'''

# string = "Hello we are indian from bhopal"
# string = "Hello we are indian from bhopal india"

# data = re.split("\s", string)
# print(data)
# print(type(data))

# you can control the number of occurence by specifying the max split parameter
# data = re.split("\s", string, 3)
# print(data)

'''
the sub() function replaces the matches with the text of your choice

ex = replace every white spaces character with 9
'''
# data = re.sub("\s","=", string)
# data = re.sub("india","pakistan", string)
# data = re.sub("india","pakistan", string, 1)
# print(data)  

'''
Match object

A match object is an object containing information about the search and the result

note: If there is no match the value
'''

'''
span(), string, group() this are methods of match

The match object has properties and methods used to retrieve information about the search and the result
'''


str = "Hello indian we are indian look like indian from bhopal"

# x = re.findall("indian", str)
# print(x)
# print(len(x))


x = re.sub("indian","bhopal", str)
print(x)



