'''
strings->caseconversion,searching,&finding,string testing methods,
replace,space removal


#searching ,finding,replacing,joining...
a="Sreeharshitha"
print(len(a))
print(min(a))
print(max(a))

#index
b=a.index('h')#it returns index position
print(b)
c=a.index('e')#it return only first occurance
print(c)
e=a.index('e',2)#it returns the next occurance
print(e)
#f=a.index('e',3)#it returns value erroe because there is no e 
#print(f)
#h=a.index('b') #value error
#print(h)


#rindex ()->returns last occurance

a="sreeharshitha"
b=a.rindex('a')#returns last occuance from string
print(b)
#c=a.rindex('a',13)#returns value error
#print(c)

#count#returns the no:of items object is repeating
print('sreeharshitha'.count('a'))
print('sree'.count('w'))#it returns 0 as we dont have'w'


#find()
print('sree'.find('t'))# it return -1 if substring is not found
print('sree'.find('e'))#it returns 1st e position

#rfind()
print('sree'.rfind('e')) #rfind returns last position of given latter
print('sree'.count('e'))


a="dataAnalysis"
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
    

#replacing,splitting,joining
#strings are immutable
a='codegnan'
print(a.replace('g','m'))
print(a)

a=a.replace('g','s')
print(a)

a=a.replace('code','node')
print(a)

b=a.replace('x','s')
print(b)


#split()
a='Sree@harshitha@naallam'
print(len(a))
b=a.split()
print(b)
print(len(b))

c=a.split('@')
print(c)
print(len(c))


#join
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print(' '.join('minnu'))



#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...

a='sri123'
print(a.isalnum())#returns True for alphanumeric strings else False
b='sri'
print(b.isalnum())#returns True supports or operstor as if there is string or num it returns True
print(b.isdigit())#false no alpha supports in isdigit
c='sri123'
print(c.isalpha())#False ->only supports aphla not num

d='950299'
print(d.isdigit()) #returns True only digits supports
print('1234',isnumeric())#this has upper edge(numbers,fractions,romas)

print('codegnan'.startswith('c'))#True
print('codegnan'.startswith('g'))#False
print('codegnan'.startswith('g',4))#True
print('codegnan'.endswith('n')) #True
print('codegnan'.endswith('a'))#False

print('codegnan'.islower())#returns True
print('CodeGnan'.islower()) #returns False
print('CODE'.isupper()) #returns True
print('codegnan'.isupper()) #returns False
print('Code Gnan'.istitle()) #True
print('Codegnan'.capitalize())


#space removal--> strip() (removes leading and trailing spaces)

a=' sree '
print(a.strip())

b = input("enter the string:").strip().lower()
print(b)
'''

#zfill filling with 0's as per the numeric string
print('123'.zfill(5))
print('3245'.zfill(10))


#center(),ljust(),rjust()-> alignment of strings(check length and then modify the width accordingly)

print('123'.center(6))
print('123'.center(6,'@'))

print('123'.ljust(6,'@'))
print('123'.rjust(6,'@'))


































