#Task->data=['codegnan','saketh','python','java'] #input
#op=using for loop
'''
0 : codegnan
1 : saketh
2 : python
3 : java

data=['codegnan','saketh','python','java']
for i in range(len(data)):
    print(i,":",data[i])
  
data=['codegnan','saketh','python','java']
for i in data:
    print(data.index(i),':',i)
'''

'''
List,Tuples

#List->Mutable,ordered,hetrogenous
#index(),count(),copy(),sort(),reverse()

d=['codegnan',7,2020,'java']
print(len(d))
print(d.index(7))
print(d.index('codegnan'))
d.extend([3,4,5,4])
print(d.index(4))
#print(d.index(4,6))  #value error


#copy()-->shallow copy of the given collection

data=['codegnan','saketh','python','java']
new=data.copy()
print(new)
print(data)
print(len(new))

new[3]='data analysis'
print(new)
print(data)
data.extend(['sri','sree'])
print(len(data))
print(data)
print(new)
new.insert(2,'code')
print(new)
print(data)

data=[1,2,3,4,[8,9,7],5]
new=data.copy()#both existing and  new list are independent
print(new)
new[4][2]='agents' #whenevere we make changes in nested list original will also be effected
print(new)
print(data)

new[1]='set' #if we change in new list out side nested list it will not change only the happen if it is nested list
print(new)
print(data)

marks=[23,54,43,-45,32,]
print('before sorting:',marks)
#marks.sort()
#print('after sorting:',marks)
#marks.sort(reverse=True) #returns decending order
#print(marks)

#marks=[23,54,43,-45,32,'sri']#type error int and str not possible

#reverse->it returns in reverse order

marks.reverse()
print(marks)
print(marks[::-1]) #reverse the order



#type(),min(),len(),max().print()-> use for any collection as list,str

print(sorted('codegnan'))
#print(sorted(['code','23',34,54])) #type error int,str not supported

#Tuples-> Indexed(),ordered(),heterogenous,immutable collection
#used for dimensions,coordinates,database record,we perfer "()" for tuple notation

a=()
print(type(a))
print(len(a))

d=1.2,5.4
print(d)
print(type(d))
print(len(d))

#operations->Indexing,slicing,striding,memebership,merging,repitation

courses=('python',['java','da'],'genai','agenticAI',[100,50])
print(len(courses))
print(type(courses))
print(courses[3][-2:])#AI

#couses[2]='abc' #error ->immutabke tuple

courses[-1].append('codegnan')
print(courses)
print('python' in courses) #membership 
d=courses*2 #repitation
print(d)
e=course+[2,3,4] #merging  error
print(e)



#Task
#create a nested tuple as above and work on slicing,striding,and list function

a=('aba','xyz','pqrs','aeiou')
print(type(a))



#Tuple->immutable->count(),index()
courses=('python',['java','da'],'genai','agenticAI',[100,50])
print(courses.index('genai')) #returns 1st occurance
print(courses.count('agentsAI'))

#print(courses.sort()) #attribute error sort not supported in tuple

print(sorted(courses[-1])) # as we have mixed type
print(sorted(courses[2]))

#Typecasting
d=tuple(sorted((23,43,54,23))) 
print(d)
'''

##eval()
print(eval("9+8")) #-> #adds the number
print("9+8") #-> #returns as 9+8 
a=eval(input("enter the list")) #it returns wt evere we keep inside the input like if list it prints list if it tuple it returns tuple format
#it takes list 
print(a)
print(type(a))


#task->take a user input as string ,do this in two ways..
'''
1) give the count of each repeating charcter
Test case: programming
using count

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]







































