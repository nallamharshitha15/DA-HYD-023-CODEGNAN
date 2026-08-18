'''
Tokens,Datatype_> control flow statements

Procedure orienterd programmin

Functions-> A function is block of code which perform a specific task
Its a resuable group of statements where we define using

def keyword
Advan->Code resuability,code maintainbility, ease of debugging,avoiding code deplication,modularity..

def fname(paarameters):  #fun defin
     """Doc strings"""  #function body
     statements(s)
     ....
     return value(s)..
fname(args)  #function call

#to perform sum a two numbers
def add(a,b):
    """sum of objects"""
    c=a+b
    return c
print(add(11,5))     #addition
print(add('code','gnan'))  #concatenation
print(add([12,3],[1,2])) #merging
d,e=map(int,input("enter the value:").split(','))
print(d,e)
print(add(d,e))

#without return

def add(a,b):
    """sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,2)) #it returns result along with None


#usage of return

name,age,salary="sree",22,60000 #global values
def details():  #no parameter ->error
    #return name,age,salary
    #return "codegnan" #-> #it will print op as codegnan
    #return 2+3+4 #9
    return  #None
print(details())


#There are 5 types of arguments

->positional arguments
->default arguments
->keyword arguments
->varibale length arguments(*args)
->keyword varibale length arguments(**kwargs)

#positional arguments->No:of arguments in function define should match with function call(order has to be maintained)
#print(len(123,321)) this is per built-in len(obj) will accept one argu

def details(name,place):
    """to store details"""
    name="sree"  #it returns first input 
    place="wrngl"
    return name,place
print(details('codegnan','da'))
print(details(23,43))
#print(details('sree','hyd',23)) #raises Type error as only 2 argu are mentioned 


#Default arguments->we can make arguments as default but not 1t arg as default

#case1
def grocery(items,price):
    """usage of default"""
    print(f'items are {items},and price is {price}')
grocery('milk',34)
grocery('apple')   #items are apple,and price is 35 ->by default it give price as 35
grocery('bread',45) #items are bread,and price is 45->here we given the price as 45

#case2
def grocery(items='cheese',price=60):
    """usage of default"""
    print(f'items are {items},and price is {price}')
grocery(35)

#case3
'''
'''
def grocery(items='cheese',price): #non defult always follows default
    """usage of default"""
    print(f'items are {items},and price is {price}')
grocery(35)

'''

#keyword arguments->when ever we wanted to specify the name of argument
def employee(name,salary,role,place='codegnagn'):
    """Keyword arguments"""
    print(f'name is {name}, and salary is {salary}, and role is {role}, works in {place}')
employee('sree',25000,'data analyst')
#name is sree, and salary is 25000, and role is data analyst, works in codegnagn
employee(salary=40000,role="data analyst",name='si') #keyword arguments
#name is si, and salary is 40000, and role is data analyst, works in codegnagn








