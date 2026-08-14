'''
sequence-> Strings,List,Tuple,Sets
Mapping->Dictionary

#Sets -> A Set is a uniques Collection of objects,unoredered,Mutable,Hashing,Unindexed,Hetergenous
#set(),{}

#a={} ->dict
a=set()
print(type(a))
stud_id={123,345,456,765,123} #prints uniques values
print(stud_id)
print(type(stud_id))
print(len(stud_id))
#print(stud_id[2]) # Type error because ste is unordered [it does not show postion of value]
print(123 in stud_id)
#print(stud_id*2)# error can't be repeated
#print(stude_id  stud_id) # error teo set cannot be merged 
#slicing and striding is not accpeted in sets ->no indexed followed

#Hashing-we can retrive data fast
#function of sets

data={12,3,4,5,6,[1,2,3],'sri'}
print(data) #no list inside a set (hashing technique) as list are mutable

data={12,3,4,5,6,(1,2,3),'sri'}
print(data) # tuple is supported in sets->tuple is immutable
print(len(data))
for i in data:
    print(i)
    print(i,end='')

#methods on sets-> add(),update(),remove(),discard(),pop()

#add()
a={'sri','sree','code'}
#print(len(a))
a.add('python')
print(a)
#add() will insert an element into the set (it can be anywhere but only uniques)
#a.add('sri')
print(a)
#a.add('sri','hasrhitha') #only accepts one value 
#print(a)
a.add(('abc','xyz')) # supports tuple not support list
print(a)

#Update()
da_name={'sri','maha','bot'}
print(da_name)

a.update(da_name)
print(a)
print(len(a))
print(da_name)
print(len(a))
print(len(da_name))
da_name.update(a)
print(a)
print(da_name)
print(len(da_name))

#reomve(),discard(),pop(),clear()

#reomve() ->remove() an element from the set (it must be a number)
da_name.remove('sri')
print(da_name)
#da_name.remove('sri') #ker error beacuse it is alredy removed from set 

#discard() will remove an element if its present else it ignores [no error]
da_name.discard('sri') 
print(da_name)

#pop()
print(da_name.pop())  #returns  the name wt we pop 
print(da_name)

da_name.pop() #returns and removes arbitrary element
print(da_name)

#print(da_name.pop()) #returns keyerror
#print(da_name)

da_name.clear()
print(da_name)

da_name.add('sri')
print(da_name)

da_name.update(['hasrh','minnu'])
print(da_name)



#copy()
a=da_name.copy()
print(a)
a.update(['minnu','xyz'])
print(a)

a.add('pqr')
print(a)

c=a.copy()
print(c)
'''
#mathematical operations->union(),intersection(),difference(),symmetric_diff(),issubset(),issuperset(),isdisjoint()

da_23={23,44,49,51,33}
da_24={49,44,63,21}
'''
da_25={87,99,44}
e=da_24.union(da_25)
e=da_24 | da_25 #  "|" ->union
print(e)
print(len(e))
event=(da_23.union(da_24))
print(event)
print(len(event))
common=da_23.intersection(da_24) # da_23 "&" da_24 
print(common)
print(len(common))

c=(da_23.intersection_update(da_24)) #returns common numbers eith update
print(c) # returns NULL
print(da_23) # common elements are finally stored
'''

#difference()
#difference removes common elements and prints values preswent from fisrt list

print(da_23)
print(da_24)
'''
diff=da_23.difference(da_24) #removes common and prints values present in da_23
print(diff)

f=da_23-(da_24)  # difference
print(diff) '''

#symmetric_diff()
# removes common elements and return all remaing elements from two list
symm=da_23.symmetric_difference(da_24) #da_23 "^" da_24
#print(symm)

da_24.remove(21)
da_24.remove(63)
#issubset()->checks for all elements present in other set

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))


#disjointset() returns False for sets having common elements
print(da_23.isdisjoint(da_24))


#length od unique student ids in a clasee ,where user can enter first input
#he should be giving number of student_ids ,he will enter student_ids

name=int(input())




























