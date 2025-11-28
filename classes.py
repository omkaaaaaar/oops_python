# #1.1 creating a basic class Example 
# class Student:
#     name="Omkar"

# #creating an object of the class
# s1=Student() #stored student class in s1 object/ instance
# print(s1.name)

# s2=Student()
# print(s2.name) #outputs the same value because s1 & s2 are instances/objects of the same class Student

# 1.2 creating a class with a method
class Car:
    color="blue"
    brand="Mercedes"

car1=Car()
print(car1.color)

car2=Car() #outputs blue because car1 is an instance of class Car which has color attribute set to value blue    
print(car1.brand) #outputs Mercedes because car1 is an instance of class Car which has brand attribute set to value Mercedes 