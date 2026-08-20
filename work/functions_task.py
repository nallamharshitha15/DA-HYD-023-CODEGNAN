#Task1
'''
def calculate_grade(marks):
    if marks>=80:
        return "A grade"
    elif marks>=60:  #in between 60-79
        return "B grade"
    elif marks>=40: #in between 40-59
        return "C grade"
    else:
        return "Fail"

    return calculate_grade
for i in range(3):
    marks=int(input("enter the marks of student:"))
    grade=calculate_grade(marks)
    print("marks are:",marks)
    print("grade is:",grade)
    
op->enter the marks of student:67
marks are: 67
grade is: B grade
enter the marks of student:89
marks are: 89
grade is: A grade
enter the marks of student:20
marks are: 20
grade is: Fail        

#Task2

def bill_calculate(price, quantity=1, discount=0):
    total = price * quantity
    discount_percentage = total * discount / 100
    final_bill = total - discount_percentage
    return final_bill
# only price
bill_1 = bill_calculate(300)
print("bill_1 is:", bill_1)

# with price and quantity
bill_2 = bill_calculate(300, 4)
print("bill_2 is:", bill_2)

# with values as keyword arguments
bill_3 = bill_calcraulate(price=300, discount=25, quantity=3)
print("bill_3 is:sr", bill_3)

op->bill_1 is: 300.0
bill_2 is: 1200.0
bill_3 is: 675.0


#Task3-> BMI Calculator


def calculate_bmi(weight, height): 
    """Calculate and return BMI.""" 
    result = weight / height ** 2 
    return result 
 
 
def bmi_status(values): 
    """Check which category the person is.""" 
    if values < 18.5: 
        return "Underweight" 
    elif values <= 24.9: 
        return "Normal" 
    elif values <= 29.9: 
        return "OverWeight" 
    else: 
        return "Obese" 
 
 
for i in range(3): 

    while True:
        name = input("enter the name of the person: ")

        if name.isalpha(): 
            break
        else: 
            print("enter alphabets, integers are not accepted")
 
    while True: 
        try: 
 
            weight = int(input("enter the weight in kgs: ")) 
            height = float(input("enter the height in meters: ")) 
     
            if weight > 0 and height > 0: 
                break 
            else: 
                print("make sure enter correct values") 
                 
        except ValueError: 
            print("Make sure to enter weight as integer only, height also as number") 
 
    #we have to call the function for every person
    BMI = calculate_bmi(weight, height) 
    catagory = bmi_status(BMI) 
 
    print(f"name is {name}") 
    print(f"bmi is {BMI:.2f}")  # .2f gives two decimals 
    print(f"person is {catagory}")  # it returns person's category 
    print()

op->enter the name of the person: 54
enter alphabets, integers are not accepted
enter the name of the person: sri
enter the weight in kgs: 30
enter the height in meters: 1.45
name is sri
bmi is 14.27
person is Underweight

enter the name of the person: 60
enter alphabets, integers are not accepted
enter the name of the person: sree
enter the weight in kgs: 60
enter the height in meters: 1.70
name is sree
bmi is 20.76
person is Normal

enter the name of the person: 120
enter alphabets, integers are not accepted
enter the name of the person: bot
enter the weight in kgs: 120
enter the height in meters: 1.50
name is bot
bmi is 53.33
person is Obese




#Task 4->Marks Summary Using *args
def mark_summary(*args):
    total = 0
    for mark in args:
        total += mark
    if len(args) > 0:
        average = total / len(args)
    else:
        average = 0
    return total, average

# One mark we should take
total, average = mark_summary(80)
print("Total:", total)
print("Average:", average)

# Several marks 
total, average = mark_summary(80, 70, 90)
print("Total:", total)
print("Average:", average)

# No marks
total, average = mark_summary()
print("Total:", total)
print("Average:", average)
'''
        
#Task 5->
def display_employee(**kwargs):
    """keyword vairable task"""
    for key,value in kwargs.items():
        print(f'{key} : {value}')
    if "salary" in kwargs:
        print("salary info:available")
    else:
        print("salary info : not provided")
    if "department" in kwargs:
        print("department info:available")
    else:
        print("department info : not provided")
    print()
#1st employee
display_employee(name="harshitha",age=20,salary=60000,department="cyber security")
#2nd employee
display_employee(name="sree",age=22,salary=20000)
display_employee(name="sri",age=21,department="IT")

    
