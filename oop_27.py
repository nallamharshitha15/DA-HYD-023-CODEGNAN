'''
#-->operator overloading(+,*,-,/)->operators will behave in diff way
# (__add__,__str__)

# +(addition,concatenation,merging)
print(2+3)#add
print('sree'+'sree') #concatenation
print([1,2,3]+[4,5,6])#merging

#print(3.__add__(4)) #__add__(self,other) magic method
a=2;b=3
print(a.__add__(b))
c=[1,2,3];d=[4,5,6]
print(c.__add__(d)) #merging
print(c.__len__()) #len(a)
print(c.__mul__(3))

#lets apply smae scenario Hotstar Watch History

class WatchHistory:
    """define the no:of hours"""
    def __init__(self,hours):
        self.hours=hours
sri=WatchHistory(100)
print(sri.hours)
sree=WatchHistory(120)
print(sree.hours)
#print(sri+sree)  #typer error unsupported because + for int,str not for class
print(sri.hours+sree.hours)  #we have take attributes also (sri.hours)

'''

class WatchHistory:
    """define the no:of hours"""
    def __init__(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        return f'watchHistory is {self.hours}'     
#other gives obj instance 
sri=WatchHistory(200)
print(sri) #__str__() method
print(sri.hours)
sree=WatchHistory(100)
print(sree)
print(sree.hours)
print(sri + sree )