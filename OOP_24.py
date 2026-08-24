'''
OOP->Class,objects,methods(__init__())
Encapsulation-->public,protected,private
Inheritance-->it is one of key feature of OOP where we inherit the propertirs (attribute/method)
from one class to another class(base class(parent class)->derived class(child class)
whatsapp-->personal User,Business User(catalog),community admin
Features->code reusabality,avoiding code duplication,code Maintainability
Ploymorphism(Method-overriding(super()),Method-overloading,operator overloading__add__,__str__)

Types of Inhertance:
1,single Inhertance(Finger Print)
-->One child class inherting properties from one parent class only
2,Multiple Inhertance(Mother,Father-->child)
-->one child class inherting properties from two parent class's
3,multi-level Inhertance(Grandparent->parent->child)
-->level-by-level
4,Hierarchial Inhertance(multiple child class's)
->inheriting propertirs from single parent
-one(parent)-many(child's)
5,Hybrid Inhertance->it can carry one or more type of inhertance

Syntax for single-inhertance:

class Baseclass:
    statemnets(s)
    ....
class Derivedclass(Baseclass):
    .....
    ......


#whatsapp scenario-->Personal User,Business User
class User:
    """single inhertance usgae"""
    def send_msg(self):
        print("sending message")
    def voice_class(self):
        print("do voice call")
    def video_call(self):
        print("making video class")
class Business_User(User):
    #pass
    def create_catalog(self):
        print("displaying products catalog")              
u1=Business_User()
#print(dir(u1))
u1.send_msg()
u1.voice_class()
u1.video_call()  
u1.create_catalog()


#social media login ->users->upade_user

class Users:
    """single inheritance usage"""
    company = "codegnan"  # class attribute
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return self.first_name + self.last_name
class Update_user(Users):
    def update_name(self):
        return self.first_name.title() + " " + self.last_name.title().strip()
u1 = Update_user("sreeharshitha", " naallam")

print(u1.company)
print(u1.update_name())

#wt if we have constructor in child class also
#Father ->child(property)

class Father:
    """usage of constructor in single inhertance"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'father propery is {self.property}')
#class child(Father):
    #pass
class child(Father):
    """usage of construtor """
    def  __init__(self):
        self.cash=200000
    def child_property(self):
        print(f'child property is {self.cash}') 
obj=child()
obj.father_property()            
obj.child_property()
'''
#in above case it giving same value for father also as 
#2l .when we gave proprty as same attribute in both class's

#parent class is having constructor child class is having constructor so constructor overrinding is happeing
#constructor overirng is -->Super keyword
#Super super().__init__()

class Father:
    """usage of constructor in single inhertance"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print(f'father propery is {self.property}')
#class child(Father):
    #pass
class child(Father):
    """usage of construtor """
    def  __init__(self):
        super().__init__() #calling superclass constructor
        self.cash=200000
    def child_property(self):
        print(f'child property is {self.cash}') 
        print(f'kid final property is {self.cash + self.property}')
obj=child()
obj.father_property()            
obj.child_property()
