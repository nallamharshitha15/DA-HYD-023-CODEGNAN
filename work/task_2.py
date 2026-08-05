'''
#task 1 string->slicing,striding
name='sreeharshitha'
print(name[:])#sreeharshitha
print(name[:9])#sreeharsh
print(name[2:])#eeharshitha
print(name[1:8])#reehars
print(name[3:10])
print(name[:20]) #it will print entire string
print(name[30:])#no op
print(name[9:1])#no op

#-ve
print(name[-13:])#sreeharshitha
print(name[:-2])#sreeharshit
print(name[-10:-3])#eharshi
print(name[3:-4])#eharsh
print(name[-4:5])#no op

#striding
name='sreeharshitha'
print(name[1:13:2])#reasih
print(name[::3])#seria
print(name[::-1])#ahtihsraheers
print(name[3::2])#easih
print(name[:6:])#sreeha
print(name[-13:-2:2])

'''
print(ord('Z'))
#Task 2:A -Z
#use loops and strings to return A-Z same line

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in letters:
    print(letter, end=" ")

#or
for i in range(65, 91):
    print(chr(i), end=" ")
#or
for i in range(26):
    print(chr(ord('A') + i),end=" ")
    


