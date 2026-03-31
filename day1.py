# class myData:
#     x = 10

# ob1 = myData()
# print(ob1.x)

# class student:
#     name = "Rahul"
#     subject = "Python"
#     fees = 5000

# ob2 = student()
# print(ob2.name)
# print(ob2.subject)
# print(ob2.fees)

# ob3 = student()
# print(ob3.name)


# class myData:
#     def myCollege(self):
#         print("My college name is cybrom")
#     def myFees(self):
#         print("My fees is 5000")
#     def mySubject():
#         print("My subject is python")
# ob1 = myData()
# ob1.myCollege()
# ob1.myFees()
# myData.mySubject()


'''
constructor
python __init__() method
All class have a built in method called __init__(), which is always executed when the class is being initiated. Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created.
'''

# class MyData:
#     def __init__(self):
#         print("This is automatically called when the object is created")

#     def myDisplay(self):
#         print("This is a display method")

# ob1 = MyData()
# ob1.myDisplay()

'''
self
'''

class Student:
    def myName(self, fnm, snm):
        self.myfnm = fnm
        self. mysnm = snm

        print("My name:", self.myfnm, self.mysnm)

ob1 = Student()
ob1.myName("Ankit","Gujre")
