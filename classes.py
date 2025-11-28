# #1.1 creating a basic class Example 
# class Student:
#     name="Omkar"

# #creating an object of the class
# s1=Student() #stored student class in s1 object/ instance
# print(s1.name)
# s2=Student()
# print(s2.name) #outputs the same value because s1 & s2 are instances/objects of the same class Student



# # 1.2 creating a class with a method
# class Car:
#     color="blue"
#     brand="Mercedes"

# car1=Car()
# print(car1.color)
# car2=Car() #outputs blue because car1 is an instance of class Car which has color attribute set to value blue    
# print(car1.brand) #outputs Mercedes because car1 is an instance of class Car which has brand attribute set to value Mercedes 



# # 1.3 __init_ method
# class Student:
#     name="Omkar"
#     def __init__(self):
#         print("adding new student in the clg db..")

# s1=Student()#<- ts parenthesis are used to call the constructor method __init__


# #1.4 passing another parameter to the __init__ method
# class Student:
#     def __init__(self, fullname, marks:float):
#         self.name=fullname
#         self.marks=marks
#         print("adding new student in the clg db..")
# s1=Student("Omkar", 98.4)# new name Omkar is passed to the __init__ method
# print(s1.name) #outputs Omkar because the name attribute of the instance s1 is
# print(s1.marks)

# s2=Student("Karan", 96.5)
# print(s2.name, s2.marks) #outputs Karan because the name and marks attribute of the instance s2 is in the same life

# # 1.5 Types of Constructors
# class Student:
#     #default constructor
#     def __init__(self):
#         pass

#     #parameterized constructor
#     def __init__ (self, fullname, marks):
#         self.name=fullname
#         self.marks=marks
#         print("adding new student in the clg db..")

# s1=Student("Omkar", 98.4)    
# print(s1.name, s1.marks)

# #1.6 Class & Instance Attributes
# class Student:
#     clg_name="Konkan Gyanpeeth College" #class attribute, beacuse all students belong to ts college
#     name="anonymous" #class attr
#     def __init__(self, fullname, marks):
#         self.name=fullname
#         self.marks=marks

# s1 = Student("Omkar", 98.3)
# print(s1.name, s1.marks, s1.clg_name) #itll print Omkar as name bcuz, Obj attr > Class attr
# print(Student.clg_name)        

