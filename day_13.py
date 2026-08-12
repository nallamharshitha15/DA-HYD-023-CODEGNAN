'''
sequences->strings,lists,tuples,sets
Mapping->dictionary
'''
#List->collection of heterogenous elements
#list->index,ordered,mutable,hetrofgenous,we us[]
'''
marks=[1,2,3,4]
print(marks)
print(len(marks))
print(type(marks))
print(2 in marks)
b=marks.index(2) #index
print(b)
'''
#operations->indexing,slicing,striding,membership,merging,repetition

#Nested list-> A Nested List is basically List inside another List
'''
name=['Codegnan',23,43,23,[1,2,3,4],'DA23',45]
print(type(name))
print(len(name))
print(name[0])
print(name[0][:4])
print(name[0][4:])

#Cdga
print(name[0][::2])
print(name)
name[0]=name[0][::-1]
print(name)
name[5]=name[5][::-1] 
print(name)

print(name[4])
print(len(name[4]))
print(name[4][2]) #index of number op=3
#indexing,slicing-->mutable
name[2]='python'
print(name)
#by indexing if we change the elements ,len,of collection will remin same
name[5]=['python','c','java']
print(name)
print(len(name))

print(name[5][0][::-1])
print(name[5][2][:2])

#in slicing wtever elemrnts you pass  as per the logic len keeps on increasing
name[2:3]='sri','sai','saketh','sairam'
print(name)
print(name[2:6])
name[3:6:2]='python','java'
print(name)
'''
#creating a nested list with strings,lists and work on Indexing,slicing,striding
#added advantages if u could add string functions also to it

#list Function->append(),insert(),extend(),pop(),remove(),clear(),index(),count(),copy(),reverse()

names=['code','sri']
#append->it inserts single element to the end of the list
#names.append('data')
#print(names)
#append() 
names.append(['analysis','agents'])
#print(names)
'''
print(names[3])
names[3].append('chatgpt')
print(names)
print(names[3][1][::2])
print(names)
print(names[3].append('chat'))#returns none as append is applicables on list not print
'''
#extend()=>insert multiple elemnts to the end of list
'''
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis']) #it will return same string at last
print(names)
names.extend([1,2,3,4])
print(names)
#names.extend(1,2,3,4) #Typeerror
#print(names)

'''

#insert()=>(index,object)->inserts given object before index
print(names)
names.insert(0,'sree') 
print(names)
#names.insert([1:4],['a','b'])#invalid syntax
#print(names)

names.insert(-1,'harshitha')
print(names)

#remove objects we use->we can remove specific value
#names.remove('harshitha')
#print(names)
#names.remove('harshitha')#it raises error because alredy we removed from list

#pop()->by default last in first out,else give index
names.pop()#reomve last element
print(names)

#del names[1:3]
#print(names)

#clear()->will remove all elemnts and returns empy list
names.clear()->op=[]
print(names)

#Task->data=['codegnan','saketh','python','java'] #input
#op=using for loop
'''
0 : codegnan
1 : saketh
2 : python
3 : java
'''
data=['codegnan','saketh','python','java']
for i in data:
    















