'''
OOP --> Object Oriented Programming --An Object oriented programming is a mechanism or a process which revolves
around creating around objects
-->It consists of two important properties 
Attributes are variables which carry data to the class
Methods is a function defined inside a class which carry behaviour of object
-->Attributes(data),Methods(Behaviour) Ex:Chair

class,objects-->A Class is a Blueprint(template) for an object
An onject is instance of class
Features of OOP --> Modularity,Scalability
Encapsulation-->(binding the data (attribute),features to the class) (objects)
Abstraction -->it will try to show only relevant information to the class or user
Inheritance -->acquaring properties from one class to another(attributes,methods)
Single -->Fingerprint,eye iris
Multiple --> Parents(Mother,father) --> child
Multi level --> Grandparent --> parent --> child
Polymorphism --> Method Overloading,Method Overriding,Operator Overriding
'''
#syntax for class creation
'''
class Class_Name:
    """Docstring"""
    attributes(characteristics)
    .........
    def func(self):    (behaviour of class)
        .....
        .....
    ....
obj = Class_Name()


#student class with basic details

class Student:
    """Understanding the usage of oop"""
    name = "harshitha"
    id = "CGH3963"
    gender = "f"
    email_id = "nallamharshitha@gmail.com"
    #Methods which carry the behaviour
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail ID is {self.email_id}')
u1 = Student()
print(u1)
#print(dir(u1)) #directory returns all available methods
(u1.display())
u2 = Student()
(u2.display())

#student class for multiple objects

class Student:
    """Understanding the usage of oop"""
    name = input("enter the name:")
    id = input("enter the id number:")
    gender = input("enter the gender")
    email_id = input("enter the email_id")
    #Methods which carry the behaviour
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail ID is {self.email_id}')
u1 = Student()
print(u1)
#print(dir(u1)) #directory returns all available methods
(u1.display())
u2 = Student()
(u2.display())
print(u1.__dict__) #it returns empty dict
print(u2.__dict__) #it returns empty dict
'''
#students details with multple objects
'''
class Students:
    """Understanding the usage of oop"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    #Methods which carry the behaviour
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail ID is {self.email_id}')
u1 = Students()
u1.data("harshitha","CGH3963","f","nallamharshitha@gmail.com")
print(u1.__dict__)
u2 = Students()
u2.data("Minnu","CGH3951","M","minnu15@gmail.com")
print(u2.__dict__)

'''
#create
class Cars:
    """Understanding the usage of oop"""
    def Car_data(self,name,brand,price,color):
        self.name=name
        self.brand = brand
        self.price = price
        self.color = color
    #Methods which carry the behaviour
    def display(self):
        print(f',car name is {self.name}')
        print(f'Car brand is {self.brand}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1 = Cars()
u1.Car_data("suzuki","Bmw","1000000","blue")
print(u1.__dict__)
u2 = Students()
u2.Car_data("","suzuki","2300000","royal green")
print(u2.__dict__)
