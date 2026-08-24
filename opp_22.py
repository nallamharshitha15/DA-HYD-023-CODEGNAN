'''
constructor -->Instance method-->public attribute
Encapsulation

constructor -->it is a special method(__init__())
which will automatically initialze the attributes and the methods to the object in the class

class Cars:
    """Understanding the usage of constructor"""
    def __init__(self,name,brand,price,color):
        self.name=name
        self.brand = brand
        self.price = price
        self.color = color
    #Methods which carry the behaviour
    def details(self):
        print(f',car name is {self.name}')
        print(f'Car brand is {self.brand}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1 = Cars("Tata","Nexon","12l","blue")
u1.details()
'''
#paramertized constructor
class Cars:
    """Understanding the usage of constructor"""
    def __init__(self): #public attributes
        self.name="sedons"
        self.brand = "BMW"
        self.price = "50lpa"
        self.color = "White"
    #Methods which carry the behaviour
    def details(self): #Instance method
        print(f'car name is {self.name}')
        print(f'Car brand is {self.brand}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1 = Cars()
print(u1.name,u1.brand,u1.price,u1.color)
u1.details()
'''
Encapsulation->It is one of the main feature of OOP.
It binds(bundles) the data (attributes) and the methods(behaviour)
into a single unit(class)-->multiple objects
-->Attributes-->public,protected,private

#public attribute -->Attribute defined inside the class(constructor)
and can be modifed outside the class

class CodegnanPortal:
    """codegnan portol with users"""
    def __init__(self,username):
        self.user=username #public attribute
    #to access student details
    def display(self): #instance method
        print(f'student username is {self.user}')
u1=CodegnanPortal("harshitha")
u1.display()
print(u1.__dict__) #it returns the key-value pairs for attributes
u1.user="sreeharhsitha"
u1.display()
u2=CodegnanPortal("sree")
u2.display()
print(u2.__dict__)            
'''