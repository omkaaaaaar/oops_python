#1.7 Methods
class Student:
    clg_name="Konkan Gyanpeeth College"

    def __init__(self, fullname, marks):
        self.name=fullname
        self.marks=marks

    def welcome(self):   #Method
        print("Welcome student,", self.name)

    def get_marks(self):
        return (self.marks)

s1=Student("Omkar", 85.3)
print(s1.marks)
s1.welcome()
print(s1.get_marks())