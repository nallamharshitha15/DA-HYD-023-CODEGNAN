'''#useage for else with for-> the else keyword will only be executed when the loop is completwly done
                           #without any break

#work_out->1,work_out_missed->0

work_log=[0,0,0,1,1,1,1,1,0,1,0]
longest_streak=0  #target_variable
current_streak=0
for day in work_log:
    if day==1:
        current_streak = current_streak +1
        if current_streak>longest_streak:
            longest_streak =current_streak
            print(longest_streak)
            #break #->it stopes here and it cannot execute else part(terminating the loop)    
    else:
        current_streak=0 # streak breaks
else:
    print(f'longest_streak is {longest_streak}')
print("execution done")


# for-else with notification
n=[0,0,1,0,1]
for notification in n:
    if notification == 1:
        print("unread notification")
        break
else:
    print("all read") 

#try to take notification from user-->list of integires
n=list(map(int,input("enter the values:").split(',')))
print(n)
for notification in n:
    if notification == 1:
        print("unread notification")
        break
else:
    print("all read")
print("all")    

# while -> it relies on condition , it will be completly executed until the condition satisfies
syntax while:

while <condition>:
    statesments(s)..
    ......
    ....


while True:
    print("sri")
#it runs infinite loops   ->to stop the executuion we use ctrl+c

i=10
while i>=1: 
    print(i)
    i -= 1 #counter -> it stops until the condtion mets

    
i=0
while i<=10: 
    print(10-i)
    i += 1
'''

#banking scenario-> PIN authentication if more than 3 attempts
#account locked..
pin ="1234"
max_attempts=3
curr_attempts=0
while curr_attempts< max_attempts:
    a=input("enter the pin:")
    if a == pin:
        print("access gained")
        #break
        continue
    else:
        print("try again")
        curr_attempts += 1
else:
    print("try after 24 hrs")










    
