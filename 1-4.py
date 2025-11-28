#1.4 passing another parameter to the __init__ method
class Student:
    def __init__(self, fullname, marks:float):
        self.name=fullname
        self.marks=marks
        print("adding new student in the clg db..")
s1=Student("Omkar", 98.4)# new name Omkar is passed to the __init__ method
print(s1.name) #outputs Omkar because the name attribute of the instance s1 is
print(s1.marks)

s2=Student("Karan", 96.5)
print(s2.name, s2.marks) #outputs Karan because the name and marks attribute of the instance s2 is in the same life 