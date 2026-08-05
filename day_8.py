'''# Strings
#sequence-> strings,lists,sets,tuples,mapping(dict)

#Strings->group og characters, we use single od double,triple quotes
#Strings are immutable,oredered,Indexed collection

a='python' #" ",""" """,' '
print(a)
print(type(a))
print(len(a)) #len->return the no:of items in container

#index()-> fetch the object(position) ->starts with 0 and ends at len(obj)-1(n-1)
#we use [] representaion 
print(a[0])#s
#print(a[25])#indexerror-< out of range
print(a[-1]) #it return last char
print(a[-4])
#print([-20])->inderxerror
#print(a[:2])

#slice-> we can access group of char(group)
#we use [start:end] #start default-->0,start is included ,end is excluded

print(a[:])
print(a[0:])
print(a[:3])
print(a[0:2])
print(a[6:])
print(a[3:7]) #accepts lower->higher
#print(a[7:3]) # not applicable higher->lower
print(a[:45])#3returns till end of the string #[45:]->no op
print(a[-2:])
print(a[-4:-1])


print(a[1:-2])
print(a[2:])

#observe +ve+ve,-ve-ve,+ve -ve
#striding->[start:end:step]
course='dataAnalysis'
print(course[::-2])
print(course[1:5:2])

print(course[2::3])
print(course[::4])

name='sri'
name[1]='w' #string is immutable


#operation on string-> repetaion,concatetination,indexing
n='sri'
print(n*3)#3repetations
print('%'*20)

data='sri' + 'sree' + ' ' + 'sri sree'
print(data)
print('m'*2)

for i in 'sri':
    #print(i) #this case we get every char line by line 
    print(i,end='')#side by side

#built-in function->len(),min(),max(),sorted()
name="sreeHarsh"
print(len(name))
print(min(name))
print(max(name))
print(ord('A'))
print(ord('a'))
print(chr(120))
print(sorted(name)) #return a list by sorting all elements

'''
#methods on strings-->case-conversion,finding,searching,
name='sri sree'
#case-conversion->upper(),lower().title(),capatalize()
a=name.upper()
print(a)
c=name.lower()
print(c)

d=name.capitalize()
print(d)
e=name.title()
print(e)















