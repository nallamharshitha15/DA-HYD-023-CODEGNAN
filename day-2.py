'''#multiassignment

name,age,place='sree',22,'warangal'
print("info:", name,age,place,sep='-->')

#a,b=2,3,4 #value error as to many values to unpack
#reassigning variables
name='sree'
a,b=21,22
print(a,b)
a,b=b,a
print(a,b,sep=',')

#a,b=b,c # name error where c is not defined

#deleting the variables -->del 
#del a,b
#print(a,b)
a=21
print(a)

#punctuators--> [list],{tuple},(dict,sets)
name='sri';age=22;course='cyber'
print(name,age,course)

# Data types --> numeric(int,float,complex),boolean,None,
             #-->sequences -->Lists,tuples,sets,Strings,
              #-->frozenset,mapping(dict)
 #int datatype -->quantity,age..
age=10
print(type(age)) #type--> returns datatype of an objects
print(type(123))

#quantity = 03  # starting 0 is not allowed
#print(quantity)

#float datatypes --> salary,discount,temp,price...

price=12.43;dis=12.7;salary=8900.00
print(price,dis,salary)
print(type(price))

#complex --> combination of real and imaGINARY
i2=4
data= 5+i2
print(data)
data=2+5j  #j is imag representation 
print(data)
print(type(data))

# boolean --> True/Flase

valid=True
print(type(valid))

error=False
print(type(error))


# type casting --> converting one datatype to another type
#python by default follows Implicit converstion (pre-defined)

#Explicit type-->we have to convert

#every built-in datatype is a built-in function
#int,float,complex,bool 

#int-->
age=22
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e) 

#float-->

float=29.06
print(type(float))
b=int(float)
print(b)
c=complex(float)
print(c)
print(type(float))
d=bool(float)
print(d)
e=bool(0)
print(e) 


#complex -->
img=5+2j
print(img)
print(type(img))
#a=int(img) #Type error #for float also Type error 
#print(a)
b=bool(img)
print(b)'''


x=float(bool(int(45)))
print(x)

f= 45 + 2.5 + 2+3j + False
print(f)





