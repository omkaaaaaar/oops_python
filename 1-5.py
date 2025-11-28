# 1.5 Types of Constructors
class Student:
    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__ (self, fullname, marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in the clg db..")

s1=Student("Omkar", 98.4)    
print(s1.name, s1.marks)