# class Bhopal:
#     def college(self):
#         print("Bhopal College")
#     def myCity(self):
#         print("Bhopal")

# class Indore:
#     def fees(self):
#         print("My fees is 45000")
#     def myCity(self):
#         print("Indore")

# class Jabalpur:
#     def mySub(self):
#         print("My subject is python")
#     def myCity(self):
#         print("Jabalpur")

# ob1 = Bhopal()
# ob2 = Indore()
# ob3 = Jabalpur()
# ob1.college()
# ob2.fees()
# ob3.mySub()
# ob1.myCity()
# ob2.myCity()    
# ob3.myCity()

class Bhopal:
    def college(self):
        print("Bhopal College")
    def myCity(self):
        print("Bhopal")
    def mySubject(self):
        print("My subject is Java")

class Indore(Bhopal):
    def fees(self):
        print("My fees is 45000")
    def mySubject(self):
        print("My subject is python")
    
ob1 = Indore()
ob1.college()
ob1.fees()
ob1.mySubject()