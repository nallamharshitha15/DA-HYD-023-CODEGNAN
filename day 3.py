'''# input formating --> accepting input from user --> input()

# accepting user input
# by default input() accepts any input()--> str 
# int(input()) accepts only integer
#float(input()) accpets only float
#str(input()) accpets only str


age=str(input(22"enter the name:"))
print("name:",age)
print(type(age))


age=float(input("enter the age:"))
print("age:",age)
print(type(age))

c=input("enter names:").split()
print(c)

a=input().split(',')
print(a)

b=input().split()
print(b)

#List of integers
 
marks=list(map(int,input("enter the numbers:").split(','))) #list is used for no.of values
print(marks)

#now we want only 2 values from user
age,salary=map(int,input("enter the numbers:").split(','))
print("age:",age)
print(salary)

#single input()--> int(input())
#two numbers in int --> a,b =map(int,input("enter the numbers").split())
#any numbers result as list --> list(map(int,input("enter number").split()))
#two numbers in float --> a,b =map(float,input("enter the numbers").split())
age=list(map(float,input("enter the numbers:").split(',')))
print(age)


#operations -->arithemitc,assignment,comparision(realtionship),logical,identity,membership,bitwise
#arithemetic-->+,-,*,/
# % --> remainder
# / --> float value
# // -->floor devision -->quotient
# area of rectangle =l*b 

length=int(input("enter the number:"))
breath=int(input("enter the number:"))
area=length*breath
print("area of rectangle:",area)


length=int(input("enter the number:"))

area=length*length
print("area of square:",area)

length=int(input("enter the number:"))
breath=int(input("enter the number:"))
area=0.5*length*breath
print("area of trinagle:",area)

#assignment operator --> =,+=,-=

a=30
print(a)

#update the number

a=a+10
print(a)

# +=
b=34
b *= 2 # 68
print(b)

c=44
c **= 2
print(c)

#comparision operators --> ==,<(less than),>(greater than),!=(not equal),<=,>=


age=24
print(age == 20)
print(age > 23)
print(age >= 24)
print( age !=24)
print(age <=50)


# marks
marks,age=24,22
print(marks==24,age==21) 

#memebership operators --> in,not in
# it checks for the existance of an object in a collection'''

a=[23,22,24]
print( 22 in a)
print(23 not in a)
#print(23 in 2333) # Type error

#logical --> AND ,OR, NOT --> decisin=on making
#AND --> all should true
#OR --> any one can true

a=(25 in [20,25]) and 20<30
print(a)

b= 45>60 or (45 <= 50)
print(b)
c= not True
print(c)

#identity -->IS, IS NOT
#THEY check for identity of an object --()
a=35
b=35
print(a is b)
print(id(a))
print(id(b))
c=a
print(id(c)) 












