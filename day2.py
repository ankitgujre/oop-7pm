'''
self
'''

# class Mydata:
#     def __init__(self, name, age):
#         self.myname = name
#         self.myage = age
#     def myDisplay(self):
#         print("My name is:", self.myname)
#         print("My age is:", self.myage)
# ob1 = Mydata("Rahul", 25)
# ob1.myDisplay()
        
# self is nothing but a reference to the current instance of the class. It is used to access variables that belongs to the class. 
# It does not have to be named self you can call it whatever you like but it has to be the first parameter of any function in the class.
# Why use Self?
'''
without self, python would not know which object properties you want to access. 
'''

'''
calculator
'''

class MyCalculator:
    def __init__(self, a,b):
        self.num1 = a
        self.num2 = b
    def myAdd(self):
        print("Addition:", self.num1 + self.num2)
    def mySub(self):
        print("Subtraction:", self.num1 - self.num2)
    def myMul(self):
        print("Multiplication:", self.num1 * self.num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ob1 = MyCalculator(num1, num2)
ob1.myAdd()
ob1.mySub()
ob1.myMul()

'''
self does not have to be named self
it does not have to be named self you can call it whatever you like but it has to be the first parameter of any function in the class.

'''

# calling method with the self
'''
self is used to call the method with the self.

'''

# class MyData:
#     def __init__(self, name):
#         self.myname = name
#     def myDisplay(self):
#         print("My name is:", self.myname)

#     def myDisplay2(self):
#         print("My name is:", self.myDisplay())
# ob1 = MyData("Ankit")
# ob1.myDisplay()
# ob1.myDisplay2()

class MyClass:
    def __init__(self, name):
        self.myname = name
    def myDisplay(self):
        return "Hi I am " + self.myname

    def myDisplay2(self):
        student_name = self.myDisplay()
        print("Welcome",student_name)

ob1 = MyClass("Ankit")
ob1.myDisplay2()


'''
Python Regular Expressions
RegExp a regular expression is a sequence of characters that forms a search pattern. 
Regular expressions can be used to check if a string contains the specified search pattern.
used to find and replace patterns in strings.
'''
# Python has a built in package called re, which can be used to work with regular expressions.
# import re
