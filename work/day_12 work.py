'''
#TASK1
name=input("enter the name:")
method=[name.upper(),name.lower(),name.title(),name.capitalize(),name.swapcase()]
for methods in method:
    b=name.upper()
    print('UPEER',":",b)
    c=name.lower()
    print('LOWER',":",c)
    d=name.title()
    print('TITLE',":",d)
    e=name.capitalize()
    print('CAPITALIZE',":",e)
    f=name.swapcase()
    print('SWAPCASE',":",f)
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
'''
#task2

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
    if not a.isalnum():
        print("does not contain only letters and numbers")
    else:
        print("validition messages")
    a=input("enter the string:")
 '''   

'''->enter the string:100student
the username contains only letters and numbers
it is ascii value

->enter the string:student_name
valid python identifier
the username begins with character
it is ascii value

'''
#task3

'''
student_name,marks=map(int,input("enter the student name:").split(','))
while student_name,marks>3:
    if marks>80:
        print(marks.center(),'A')
        print(marks.ljust()
  '''  
'''
print("=" * 50)
print("STUDENT REPORT".center(50))
print("=" * 50)

print(f"{'Name'.ljust(20)} {'Marks'.center(10)} {'Grade'.rjust(15)}")

for i in range(3):
    student_name, marks = input("Enter name and marks: ").split()
    marks = int(marks)

    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue

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

t = input("enter the text: ")

Letters = 0
Digit = 0
Spaces = 0
Printable = 0

for i in t:
    if i.isalpha():
        Letters += 1

    if i.isdigit():
        Digit += 1

    if i.isspace():
        Spaces += 1

    if i.isprintable():
        Printable += 1

print("Letters :", Letters)
print("Digits :", Digit)
print("Spaces :", Spaces)
print("Printable :", Printable)
print("Lowercase :", t.islower())
print("Uppercase :", t.isupper())
print("Title Case :", t.istitle())
        
        



    
        
    

















    
