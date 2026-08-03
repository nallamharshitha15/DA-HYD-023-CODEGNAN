'''
x=4
y=x
print(id(x))
print(id(y))
z=4
print(id(z))
a=[1,2,3]
b=a
print(id(a))
print(id(b))
c=[1,2,3]
print(id(c)) # as we have list (mutable collection(we be modified)) both c and a list will be diff
#ids where values are same but id is diff 
print(a is c)
print(a==c)
print(a is not c) 


# bitwise operators --> XOR(^),AND(&),OR(|),(<<,>>),(perfrom bitwise operations or operands)
# number will be converted to binary format 
a=5^3 #both 5 and 3 perfom biteise XOR operation op/6
b=5&3# AND op/ 1
c=5|3# OR op/73
print(a)
print(b)
print(c)

print(5 or 3) #op/5
print(5 and 3) # op/3 ( AND is logical operators checks for both existances)

#leftshift << and rightshit >>;
print(15<<2)
print(15>>2)


#input formating --> input(),int(input()),float(input())
# for single--input()
#2 or 3 inputs--2>map(int,input())
#group of integers-->list(map(int,input()))

name=input("enter the name").split(',')
print(name)

#control blocks statemnets  3 TYPES # THEY CONTROL THE FLOW OF PROGRAM (WHEN TO EXECUTE AND HOW TO EXECUTE)
#conditional statemnts --> IF,ELSE,ELIF(rely on condition to be executed)
#repetition(loops) --> WHILE,FOR


#CONDITIONAL STATEMENTS:
#IF USAGE:
syntax :
    if<condition>:
        statements()
        ....

age=int(input("enter the age="))
if age>18 or age in[20,20,40]:
    print("your age is :",age)

#if-else keyword    


syntax :
    if<condition>:
        statements()
        ....
    else:
        statement(s)...
        '''

marks=int(input("enter the marks:"))
if(marks>0 and marks<=100):
        if marks>90: 
                  print("A",marks)
else:
        if(marks>80 and marks<90):
                print("B",marks)
        else:
                if(marks>70 and marks<80):
                        print("C",marks)
                else:
                        
                        if(marks>60 and marks<70):
                                
                                print("D",marks)
                        else:
                                
                                if(marks>50 and marks<60):
                                        print("E",marks)
                                else:
                                     print("Fail",marks)

'''

marks=int(input("enter the marks:"))
    
if (marks>90 and marks<100):
        print("pass",marks)
        print("A")
elif (marks>80 and  marks<89):
        print("B",marks)
elif(marks>70 and marks<79):
        print("C")
else:
    print("False")'''





            
