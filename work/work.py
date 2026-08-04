'''marks=int(input("enter the marks:"))
if marks<0 or marks>100:
    print("Invalid marks entered")
elif marks>=90:
    print("Grade: A")
    print("Remark: Outstanding!",marks)
elif marks>=80:
    print("Grade: B")
    print("Remark: Excellent!",marks)
elif marks>=70:
    print("Grade: C")
    print("Remark: Good",marks)
elif marks>=60:
    print("Grade: D")
    print("Remark: Fair, needs improvement",marks)
elif marks>=50:
    print("Grade: E")
    print("Remark: Poor, needs serious improvement",marks)
else:
    print("Grade: F")
    print("Remark: Failed, needs to reappear",marks)



a=int(input("enter the number:"))
if a==0:
    print("Zero is nither even or odd",a)
elif a%2==0 and a<0:
    print("negative even number",a)
elif a%2 !=0 and a<0:
    print("negative odd number",a)
elif a%2==0 and a>0:
    print("positive even number",a)
else:
    print("positive odd number",a)

'''
month=int(input("enter the number:"))
if month<=0 or month>12:
    print("Invalid month entered")
elif month==12 or month==1 or month==2:
    print("season:Winter",month)
elif month==3 or month==4 or month==5:
    print("season:spring",month)
elif month==6 or month==7 or month==8:
    print("season:summer",month)
else:
    print("season:autumn",month)
