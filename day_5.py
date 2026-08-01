'''a=str(input("enter the number"))
if a in('a','e','i','o','u'):
    print("v:",a)
else:
    print("c:",a)

a=int(input("enter the number"))
if a%2==0:
    print(" even ")
else:
    print("odd")


marks=int(input("enter the marks:"))
if marks>0 and marks<=100:
    marks=marks-100
    print(marks)
    if marks>=90:
        print("A")
    if marks>80 and marks<=89:
        print("b")
    if marks>70 and marks<=79:
        print("C")
    if marks>60 and marks<=69:
        print("D")
    if marks <60:
        print("Fail")
else:
    print("enter only +ve values no 0")

#elif:
    syntax :
    if<condition1>:
        statements()
        .....
    elif<condition2>:
        statement(S)
    elif(condition3>:
         statement()..
        ....
    else:
        statement(s)...
        
marks=int(input("enter the marks:"))
if  marks>=100:
    marks=marks-100
    print("only enter 0 to 100")
elif marks>=90:
    print("A",marks)
elif marks>80 and marks<=89:
    print("b",marks)
elif marks>70 and marks<=79:
    print("C",marks)
elif marks>60 and marks<=69:
    print("D",marks)
elif marks <60 and marks>=0:
    print("Fail with marks:",marks)
else:
    print("enter only +ve values no 0",marks)
    
    
#task--> same usecase try with if-elif-else usage in other way

#voter elgiibility checkcase-->make sure to satisy all possible
#>=18-->yes access-->100
#<18==>no
#negative values--> not allowed

age=int(input("enter the age:"))
if age>=18 and age<=100:
    print("elgible")
    print("access granted")
elif age<18 and age>0:
    age=18-age
    print("not elgible and wait for more",age,"years")
else:
    print("no 0 and -ve values are accpected")
        '''
a,b=8,9
print(a,b)
name='codegnan';batch='da'
print(name,batch)
print(name,batch,sep='#')
print(name,batch,end='\n')
print(a,b,end='\n')
print('minnu')

#old foramting-->%d-->integer,%s-->string,%f-->float
salary=2500.78
print("my salary %d"%(salary))
print("my salary %f"%(salary))
print("my salary %.1f"%(salary))

#.format() usage
print('{} is in {}'.format(name,batch))

#f-string usage
age=8
name='sree'
print('my name is',name,'my age is',age,end='\n')
print(f"my name is {name} my age is {age}")














