
'''
#Exception handling/scope of variables/Built-in Functions

Exception handling->is a mechanisam that helps to responf or make the flow of execution in
normal,way,without this error will occur and disrup the flow of program

common exceptions-->ValueError, indexError,TypeError,AtributeError,ZeroDivisionError...

Syntax:
try:
  #code that will cause the execption
except Exception as e:
     #code will catch the exception
finally:
     #runs irrrespective of try/except....
     

#basic Exception handling
try:
    #a=10  #op->2.0
    a=int(input("enter the value:")) #we if give 0 op->division by zero
    result=20/a
#except Exception as e:
 #   print(e) #it returns the error
except ValueError: #if we take float it returns this
    print(f'Invalid entery enter only integer values')
except ZeroDivisionError: #if we give 0 it returns this
    print(f'division by zero enter only integer values')

except NameError: #if we type resul it gives this
    print(f'check the name of variable properly')

    
#similary if we want to check other Errors->IndexError,AttributeError    

try:
    a=[10,23,40]
    a.apped(25) #attrirbute error
    print(a[5])
#except Exception as e:
   # print(e)
except AttributeError: #append
    print(f'dont rush write name properly')
    
except IndexError:
    print(f'index not applicable,check the len of list properly and access elemts')    


try:
    a=[10,20,30]
    a.append(35) #apped
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a=list(map(int,input('enter the number:').split(',')))
    a.append(34)
    print(a)
    print(a[2])


#BMI-->bmi=(weight)/((height**2))
#Feet-->12 inches-->1inch=2.54cm

while True:
    try:
        weight=int(input("enter the weight in kgs:"))
        height=float(input("enter the height is in meters:"))
        if weight>0 and height>0:
            break
            #continue
            #print("bye")
            #pass
        else:
            print("make sure to enter only corrct values")
    except ValueError:
        print(f'Make sure to enter weight as interger only,height also as number')

bmi=((weight)/(height)**2)
print(bmi)

#include this in bmi Task
'''
#scope of Variables->Scope is basically the region/area where it is acccessible
#Local Scope,Global Scope
#Global keyword,Enclosing Scope(Nested Functions nonlocal keywords)

'''
Local Scope->variables define inside the functions accessible inside

def display():
    """usage of local"""
    name='codegnan' #local variable
    print(name)
display()
print(name)  #NameError 

#Global Scope(variables)-->define outside and can be accessible anywhere

place="Hyderabad" #global variable
def display():
    "usage of Global Scope"""
    name='codegnagn'
    print(name)
    print(f'{name}is in {place}')
display()
print(place)


count=20
def display():
    """usage of global keyword"""
    global count   #global keyword
    count=count+8
    print(f'value inside function is {count}')
display()
print(f'value outside function is {count}')

count=20
def display():
    """priority of local and global"""  #local as high priority
    count=5 #global keyword
    count=count+8
    print(f'value inside function is {count}')
    #op-> value inside function is 13
display()
print(f'value outside function is {count}')
#value outside function is 20

#Enclosing Scope (nonlocal keyword)
def outer():
    """outer function with local variable"""
    count=5
    def inner():
        """Nested function"""
        nonlocal count
        count=count+10
        print(f'vaule inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()    
'''

#Built-in functions-->variables BuiltinScope
len=34
print(len+2)

print(len('codegnan')) #TypeError











