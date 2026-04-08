# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printName(self):
#         print(self.firstname, self.lastname)


# # class Student(Person):
# #     pass

# class Student(Person):
#     def myDisplay(self):
#         print("This is child method")


# x = Student("Ankit", "Gujre")
# x.printName()
# x.myDisplay()


class Indore:
    def __init__(self, college_name):
        self.city = "Indore"
        self.college = college_name

    def display(self):
        print("City:", self.city)
        print("College:", self.college)


class Bhopal(Indore):
    def __init__(self, college_name):
        
        self.city = "Bhopal" 
        self.college = college_name            
    
    def mydisplay(self):
        print("City:", self.city)
        print("College:", self.college)

x = Bhopal("BU")
x.display()
x.mydisplay()

