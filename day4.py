# what is PIP?
'''

PIP is a package manager for Python packages, or modules that you want to install.

What is a package?


'''

import camelcase

str = "welcome to bhopal"

c = camelcase.CamelCase()
print(c.hump(str))  # what is hump() method? 

# hump() method is used to convert the first letter of each word in a string to uppercase and the rest of the letters to lowercase. 
#It is a method provided by the CamelCase class in the camelcase module. When you call c.hump(str), it takes the input string 
#"welcome to bhopal" and converts it to "Welcome To Bhopal".

# x = camelcase.CamelCase(str)
# print(x)  # this will print the object address




'''
Python Math Module

Python has a set  of built in math functions, which are always available to use. However, for advanced math functions, you need to import 
the math module.
'''
# built in math functions 
# the min() and max() functions can be used to find the smallest and largest value in an iterable or among two or more arguments.


ans = max(10,15,20,60,100)
print(ans)

ans = min(10,15,20,60,100)
print(ans)

a = [1,2,4,6,45,78,90,100]

ans = max(a)
print(ans)

ans = min(a)
print(ans)

# abs() function returns the absolute value of a number
ans = abs(-7.5)
print(ans)


# the pow() function returns the value of x to the power of y (xy)
ans = pow(4,5)
print(ans)

# the sqrt() function returns the square root of a number
import math
ans = math.sqrt(64)
print(ans)

ans = math.sqrt(10)
print(ans)

# the ceil() function rounds a number upwards to its nearest integer
ans = math.ceil(-1.4)
print(ans)

ans = math.ceil(1.6)
print(ans)

# the floor() function rounds a number downwards to its nearest integer
ans = math.floor(1.4)
print(ans)

ans = math.floor(1.6)
print(ans)

ans = math.floor(-65.0265)
print(ans)

# math.pi is a constant that represents the value of pi (3.141592653589793)

ans = math.pi
print(ans)


# wap to find the area of triangle when  w and h are given by user

w = float(input("enter the width: "))
h = float(input("enter the height: "))
area = 1/2 * (w * h)
print("The area of triangle is:", area)