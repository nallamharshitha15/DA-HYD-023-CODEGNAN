'''s=list(map(int,input('enter the prices:').split(',')))
sum=0
for i in s:
    sum = sum+i
print('sum of the products are:',sum)



a=input("enter the string:")
upper=lower=digit=special=0
for i in a:
    if 'A'<=i<='Z':
        upper += 1
    elif 'a'<=i<='z':
        lower += 1
    elif '0'<=i<='9':
        digit += 1
    else:
        special += 1
print("upper",upper)
print('lower',lower)
print('digit',digit)
print('special',special)


a=input().split()
for i in a:
    print(i.split("@")[1])
'''
movies=list(map(str,input().split(',')))
for i in movies:
        print(id(i))
        i += 1








