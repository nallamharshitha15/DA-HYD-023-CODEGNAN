'''
Functions -->
  Variable length arguments(*args)
  Keyword variable length arguments(**kargs)

Variable length arguments --> the no of positions are not limited we can pass any number of arguments,but we need to use * representation,data is stored in tuple
Keyword variable length aruguments --> we can pass any number of keyword arguments we use ** representation data is stored in dictionary



#variable length argument
def sample(*args):    #can pass any number of positional arguments
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()   #no arguments
sample(1,2,3,4) #any number
sample('Jash','da',89)
details = [23,45,78,56]
sample(details)     #returns list inside tuple as length 1  (passing a collection)
sample(*details)  #returns details inside a tuple as length 4(* is used for unpacking a collection)
 
a,b,c = 13,4,'a'
print(a,b,c)
#a,*b,c = 'codegnan','python',45,98,40,'data'
#a,b,*c = 'codegnan','python',45,98,40,'data'  *used to unpack values
a,b,*c = 'code','gama'   #retuns empty list for c because it doesnot have values
print(a)
print(b)
print(c)
c.extend([67,90,56])
print(c)


#Task --> we wanted to calculate the sum of given objects using function
def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    result = 0
    for i in a:
        #print(i)
        if type(i) == int or type(i) == float:
            result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(12,3,4,5.9))
#print(add(3,4,5,'hgfd',3.9))
b = list(map(int,input('Enter numbers:').split(',')))
print(add(*b))
#print(*b)
for i in b:
    print(i,end=' ')  #returns value side by side same as above line code



#Keyword variable length arguments
def details(**kwargs):
    """Usage of kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()
details(name='jashnavi',place='Hyd',batch='da')
batch = {'number':'da23','place'='Hyd'}
details(**batch)



#now let us include both * ** into a function
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if(type(i) in (int,float,complex)):
            result = result + i
    print(result)
    for key,value in b.items():
           print(f'key is {key}')
           print(f'value is {value}')
sample(2,3,5,'pol','vig',2.4,name = 'code',place = 'hyd')

#sample(name = 'jash',ids=23,33)  #positional argument follows keyword arguments     
        
'''
