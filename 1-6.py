#1.6 Class & Instance Attributes
class Student:
    clg_name="Konkan Gyanpeeth College" #class attribute, beacuse all students belong to ts college
    name="anonymous" #class attr
    def __init__(self, fullname, marks):
        self.name=fullname
        self.marks=marks

s1 = Student("Omkar", 98.3) #ts is a object
print(s1.name, s1.marks, s1.clg_name) #itll print Omkar as name bcuz, Obj attr > Class attr
print(Student.clg_name)        