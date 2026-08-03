'''
#control statements-> flow of executuion of program
                     ->conditional statements-->if,elif,else
                     ->repetitive statements(loops)-->while,for(for with else)
                                                               (while with else)
                     ->jumping statements->break,continue,pass
#loops-> loops are helpful for repitation(automative task)
#for keyword will helpful to iterate over a sequence / range
# when using for keyword when we know the last value (NEEDS AN END POINT)
#syntax for (for keyword)

for <temp_var> in sequence/range:
     statemnets(s)...
     ....

#range(start,stop,step)
# by default range picks 0 as start value
for i in range(11):
    print(i)
#in above case we got 10 iterations 0-9
for i in range(1,11):
    print(f'value of i is ->{i}')

for i in range(5,15):
    if i>=5  and i%2==0:
        print(f'values of i is->{i}')

#range(start,slice,step)-> here stop->intervel
for i in range(1,10,2):
    print(i)

for i in range(-10,0,1):
    print(i)

#[]-> list
names=['sri','sree','minnu']
print(len(names))   # shows the lenght of names 
for name in names:
    print(f'names of student= {name}')
    if name == "sree":
        print(f'name is {name}')

#calculate the sum og first 10 numbers
#1st understand your input--> range(11)->10 numbers
# 2nd understand your o/p-> sum(num)

result =0  # target variable
for i in range(21):
    if i%2==0:
        result=result + i  # result += 1
        print(f'even numbers are:{result}')
print("sum of 10 numbers is:",result)
'''
# understand the loops usage with fitness streak ex
#work_out->1,work_out_missed->0

work_log=[0,0,0,1,1,1,1,1,0,1,0]
longest_streak=0  #target_variable
current_streak=0
for day in work_log:
    if day==1:
        current_streak = current_streak +1
        if current_streak>longest_streak:
            longest_streak =current_streak
    else:
        current_streak=0 # streak breaks
print(longest_streak)


    
    











        
