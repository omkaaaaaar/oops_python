#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

#Method 1, normal basic way
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def print_average(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        return (f"Average Marks ={avg}")

s1=Student("Omkar", 42,41,43)
print(s1.name)
print(s1.print_average())

#Method 2, with List  List =[30,40,50]
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum = self.marks



s1 = Student("Omkar Patkar", [42,41,43])        
