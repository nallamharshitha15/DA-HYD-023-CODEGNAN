'''
super().__init__() #calling superclass constructor
super().__init__(args) #calling superclass constructor with args
#super().method()

class Father:
    """usage of constructor in single inhertance"""
    def __init__(self,property):
        self.property=property
    def father_property(self):
        print(f'father propery is {self.property}')
#class child(Father):
    #pass
class child(Father):
    """usage of construtor """
    def  __init__(self,cash,property):
        super().__init__(property) #calling superclass constructor
        self.cash=cash
    def child_property(self):
        print(f'child property is {self.cash}') 
        print(f'kid final property is {self.cash + self.property}')
obj=child(200000,1000000)
obj.father_property()            
obj.child_property()

#wt if child class is having same method name as parent class ->method overriding
# findin  area of square.rectangle

class Square:
    """Method overridinf usage"""  
    def __init__(self,x):
        self.x=x
        
    def area(self):
        print(f'area of square is {self.x **2}')
class Rectangle(Square):
    def  __init__(self,x,y):
        self.y=y
        super().__init__(x) #constructor overriding
    def area(self):
        super().area()  #calling superclass method 

        print(f'area of rectangle is {self.x * self.y}')
x,y = map(int,input("enter the numbers:").split(','))        
obj=Rectangle(x,y)
obj.area()
'''
#multiple Inhertance
'''
class parent1:
    ......
class parent2:
    ....
class child(parent1,parent2):
    ......


class User:
    """First parent class with User features"""
    def voice_calls(self):
        print("making voice calls")
class Notification:
    def notifications(self):
        print('sending notifications')
class PremiumUser(User,Notification):
    def verification_badge(self):
        print('blue tick verification done')            
user=PremiumUser()
user.verification_badge()
user.voice_calls()
user.notifications()        
'''

#Mutlilevel Inhertance
'''
class Grandparent:
    .....
class parent(Grandparent):
    .....
class child(parent):
    .....


class User:
    def voice_calls(self):
        print("making voice calls")
class BusinessUser(User):
    def catalog(self):
        print("catalogs")
class VerifyBusinessUser(BusinessUser):
    def verification_badge(self):
        print("blue tick verification done")
user=VerifyBusinessUser()
user.verification_badge()
user.catalog()
user.voice_calls()           
''' 
'''            
#Task hierarchial Inhertance
#task2 hybrid (single,mutliple,mutlilevel)
#flipkart ex
class User:
    def login(self):
        print("gives login credentials")
class  premiumUser(User):
    def more_discounts(self):
        print("user have more discounts")
class UltrapremiumUser(User):
    def high_discount(self):
        print("user have more discount!!!!")
class carts(User):
    def add_carts(self):
        print("it gives produts we added to carts")        
user=carts()
user.add_carts()
user.login()
#user.high_discount()
'''
#Task 2 Hybrid inheritance

class CodegnanPortal:
    def portal_info(self):
        print("give information about portal ")
class Student_portal(CodegnanPortal):
    def student_details(self):
        print("gives student details")
class Exam_report(Student_portal):
    def final_report(self):
        print("gives student final report")
class student_attendance(CodegnanPortal):
    def overall_attendance(self):
        print("gives student attendance")        
user1=Exam_report()
user1.final_report()
user1.student_details()
user1.portal_info()
user2=student_attendance()
user2.portal_info()