'''
secret="121"
while True:
    a=input("enter the number:")
    if secret==a:
        print("your secret number is:",a)
        break
    elif a>secret:
        print("very high")
        print("try again")
    elif a<secret:
        print('very low')
        print("try again")
        
        

#task->otp verification
otp="950"
curr_attempts=0
last_attempts=7
while curr_attempts<last_attempts:
    curr_otp=input("enter the otp:")
    if curr_otp==otp:
        print(f'your otp is correct{curr_otp}')
    else:
        remaining=last_attempts-curr_attempts
        print(f'wrong otp you have only {remaining}attempts')
        curr_attempts += 1
else:
    print('wait for 30 secs!!')



otp="123"
current_otp=0
while current_otp<7:
    present_otp=input("enter the otp:")
    if present_otp==otp:
        print("your otp is correct!!!")
    else:
        remaining=7 - current_otp
        print(f'wrong you have only{remaining} attempts')
if present_otp==current_otp:
    print("blocked")



foods=input()
count=0
while foods != "exit":
    count += 1
    foods=input()
print(f'food ordered',count)    
    '''

program="python"
current=0
last=3
while current<last:
    p=input('enter the name:')
    if p==program:
        print(f'your progrm is{p}')
    else:
        remaining=last-current
        print('try again you have only {remaining} attempts')
        current += 1
else:
    print("blocked")
        









    
       
