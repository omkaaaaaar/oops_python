# oops_python

#### My learnings of OOPS, there is explanation about everything down below

**Functions:**
Helps in reusabilty, a reusable form of code that performs a specific task when you call it. 2 types of functions - USER DEFINED FN ex- def add, def sub,etc and BUILT IN FN -> these are the functions which are given by python as a default, ex print(), len(), type(), etc. EX - meko agar ek code structure ko bohot baar repeat karna hai then i will simply create a function of that feature, jisse ill be able to use the repeating strucutre without writing it multiple time but by just calling it, example - {def add(a,b ): return a+b} we can use this function multipletimes just by calling it, ex- print(add(78,90)), print(add(40,30))

**CLASS:**
Claas is a blueprint for creating objects, to store multiple attributes/feautres of the object, ex - student name, student division, student roll no, in the student class!

**OBJECTs:**
Object is the particular feautres - roll no, division, student name, etc

**CLASS AND OBJECT:**
THis type of relationship is used explictly to store these type data's in a simple way, ex - create a "class Student" and define the 'objects' it is also known as instance [Instances of class] (s1 = Student()) in it. EX - 1.1 BASIC CLASS EXAMPLE

**CLASS** multiple attributes:
Ex 1.2, shows that there are multiple attributes/features of the car like the car color and the car brand Similary, when we called the car in the object/instance "Car1", there we chose which features of the car that we wanted, ex - car brand car color

**init** (initialization):
It is known as the CONSTRUCTOR, even if you dont write the init fn, python automatically writes it and executes it. The constructor always take an argument/ a parameter called "Self". The self overhere means the new object which is been creating it is that only, means we are now creating s1 right? then the self points the s1 itself that IT IS S1 {MEIN KHUD}

**New Parameters to class: (1.4)**
Adding new paramet, fullname to the constructor, defined self.name=fullname, it means if someone calls s1.name (bcoz s1=self, s2=self **SELF IS A REFRENCE** NOT A OBJECT!!)then provide him the fullname!

**1.5 Default & Parameterized Constructors**
1.5 shows default constructor which only has "Self" in it and nothing else, if we dont create a default constructor then python will automatically create it
The Parameterized constructores are constructores which not only has the self constructor but also few different parametes too. IRL we only create a single parameterized constructor which we satisfies our need

---

**Class & Indtance Attributes**
