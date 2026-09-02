'''
File handling in python->Files are mainly used to store the data
It supports ->(r,w,a),read,write,append,using (open)

#first lets understand how can we access.txt file using python

import os
if os.path.exists('py.txt'):
    file=open('py.txt','r')
    print("File is loaded sucessfully")
else:
    print("file not found")
'''
#now let us access the content from file
#file=open('py.txt','r')
#print(file)
#print(file.read())#reads the entire content from file
#print(type(file.read()))
#a=file.read()
#print(a)
#print(len(a)) #it shows the length of the string
'''hello codegnan
da-hyd-023 batch
Sree Harshitha

47'''
#readline(),readlines()
#print(file)
#print(file.readline()) #it reads single from from the file
'''hello codegnan'''
#print(file.readlines()) #it reads all lines from the file in a list
'''['hello codegnan\n', 'da-hyd-023 batch\n', 'Sree Harshitha\n']'''

#'W' mode->It automatically creats a new file, if the file is exsisting it overrides the
#content in it
'''
file=open('data.txt','w')
print(file)
#as the file is automatically created lets write data in it
file.write("hi sree harshitha,How are you?")
file.write("today is wed")
file.close()

#we can also with keyword to avoid close()
with open('data.txt','w')as f:
    f.write("now checking wt happen")


#lets go with append->'a'->is also automatically creats a file,but if the file is already
#existing it appends the content to the previous file
with open('data.txt','a') as g:
    g.write("\n let us se how its going")

#+->read and write
with open('data.txt','r+')as h:
    #print(h.read())
    h.write("hello harhsitha\n")
    print(h.read())

#in the above case we can perform both read and write operations    
'''
#File operations size and path
import os
file=open('data.txt','r')
#file='data.txt'
if os.path.exists('data.txt'):
    print("file size is",os.path.getsize('data.txt'),"Bytes")
    print("File path is",os.path.abspath('data.txt'))
else:
    print("File not found")

    




