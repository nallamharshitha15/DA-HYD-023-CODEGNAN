movies = input("Enter movie names: ").split(",")
count = 1
for movie in movies:
    print(count, movie)
    count += 1

#count boundrires,dot balls, total score
'''
player=[4,6,1,0,2,4,0,6]
total=0
dot_balls=runs=boundries=0

for i in player:
    if i==4 or i==6:
        boundries += 1   
    elif i==0:
        dot_balls +=1
    else:
        runs +=1
        
        
    total= total+i
print('boundries:',boundries)
print('dot_balls:',dot_balls)
print('runs:',runs)
print(f'total he scored:{total}')



pattern="1234"
curr_attempts=0
last_attempts=5
while curr_attempts<last_attempts:
    my_password=input('enter the password:')
    if my_password==pattern:
        print("my password is correct")
        break
    else:
        curr_attempts +=1
        print('wrong attempts')
else:
    print("please try again")
'''

pattern="1234"
curr_attempts=0
last_attempts=3
while curr_attempts<last_attempts:
    my_password=input('enter the password:')
    if my_password==pattern:
        print("my password is correct")
        break
    else:
        curr_attempts +=1
        print('wrong attempts')
else:
    print("please try again")

pin="1234"
curr_attempts=0
last_attempts=3
while curr_attempts<last_attempts:
    my_pin=input('enter the pin:')
    if my_pin==pin:
        print("my password is correct")
        break
    else:
        curr_attempts +=1
        print('wrong attempts')
else:
    print("please try again")    
'''
user_name="admin"
password="123"
curr_attempts=0
last_attempts=3
while curr_attempts<last_attempts:
    name=input("enter user name:")
    if name==user_name:
        print('user name',name)
        while True:
            p=input("enter the password")
            if p==password:
                print('password id',p)
                
            else:
                print('incorrect')
                curr_attempts +=1
                break
else:
    print("blocked")

'''        




        
