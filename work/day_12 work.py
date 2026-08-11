'''
#TASK1
name=input("enter the name:")
method=[name.upper(),name.lower(),name.title(),name.capitalize(),name.swapcase()]
for methods in method:
    b=name.upper()
    print(b)
    c=name.lower()
    print(c)
    d=name.title()
    print(d)
    e=name.capitalize()
    print(e)
    f=name.swapcase()
    print(f)
    break
print('PYTHON IS FUN'.isupper())
print('python is fun'.islower())
print('python is fun'.istitle())


if name.isupper():
    print('it is upper')
elif name.islower():
    print('it is lower')
elif name.istitle():
    print('it is title')
else:
    print('null')


'''
#task2
'''
a=input("enter the string:")
while a!="exit":
    if a.isalnum():
        print("the username contains only letters and numbers")
    if a.isidentifier():
        print("valid python identifier")
    if a[0].isalpha():
        print("the username begins with character")
    if a.isascii():
        print('it is ascii value')
    else:
        print("null")
    a=input("enter the string:")
    '''

'''->enter the string:100student
the username contains only letters and numbers
it is ascii value

->enter the string:student_name
valid python identifier
the username begins with character
it is ascii value


#task3
'''
'''
student_name,marks=map(int,input("enter the student name:").split(','))
while student_name,marks>3:
    if marks>80:
        print(marks.center(),'A')
        print(marks.ljust()
    
'''

print("-" * 80)
print("STUDENT REPORT".center(80))
print("-" * 80)

for i in range(3):
    student_name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))

    if marks >= 80 and marks <= 100:
        grade = "A Grade"
    elif marks >= 60:
        grade = "B Grade"
    elif marks >= 40:
        grade = "C Grade"
    else:
        grade = "Fail"

    print(f"{student_name.ljust(20)} {str(marks).center(10)} {grade.rjust(15)}")





     

'''
#Task 4

name=["python class 10"]
for i in name:
    print(i.count(i))
''' 


    
        
    

















    
