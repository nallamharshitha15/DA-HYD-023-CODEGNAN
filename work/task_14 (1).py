'''#Task1
marks = []

# Take 3 marks from the user
for i in range(3):
    mark = int(input("Enter the  marks: "))
    marks.append(mark) #append at end 
print("Marks:", marks)
marks.insert(0, 90)
marks.extend([75, 85])
print("After adding values:", marks)
if 75 in marks:
    marks.remove(75)
removed = marks.pop()
print("Removed marks:", removed)

print("Final marks:", marks)
print("Length of marks:", len(marks))
 #op=Enter the  marks: 76
Enter the  marks: 45
Enter the  marks: 98
Marks: [76, 45, 98]
After adding values: [90, 76, 45, 98, 75, 85]
Removed marks: 85
Final marks: [90, 76, 45, 98]
Length of marks: 4


#task2

numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print("Ascending order:", numbers)
numbers.reverse()
print("Descending order:", numbers)
search = int(input("Enter a number to search: "))
if search in numbers:
    print("Number found")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("Number not found")
print("Smallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total value:", sum(numbers))

0p=Ascending order: [10, 20, 20, 20, 30, 40]
Descending order: [40, 30, 20, 20, 20, 10]
Enter a number to search: 20
Number found
Count: 3
First index: 2
Smallest value: 10
Largest value: 40
Total value: 140

#task3
numbers = [10, 15, 20, 25, 30, 35]
even = []
odd = []
for num in numbers:
    if num % 2 == 0: 
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
backup = numbers.copy()
numbers.clear()
print("Original list:", numbers)
print("Backup list:", backup)

op=Even numbers: [10, 20, 30]
Odd numbers: [15, 25, 35]
First three: [10, 15, 20]
Last three: [25, 30, 35]
Original list: []
Backup list: [10, 15, 20, 25, 30, 35]'

#task4

names = ["sri", "harshitha", "sree", "sravani", "minnu"]
name = set(names)
print("After removing duplicates:", name)
name.add("navya")
print("After adding navya:", name)
name.update(["ntr", "arjun"])
print("After adding ntr and arjun:", name)
if "sri" in name:
    name.remove("sri")
name.discard("raju")
print("Final names:", name)
for i in name:
    print(i)
#op After removing duplicates: {'sree', 'sri', 'harshitha', 'sravani', 'minnu'}
After adding navya: {'sree', 'sri', 'harshitha', 'sravani', 'navya', 'minnu'}
After adding ntr and arjun: {'ntr', 'sree', 'arjun', 'sri', 'harshitha', 'sravani', 'navya', 'minnu'}
Final names: {'ntr', 'sree', 'arjun', 'harshitha', 'sravani', 'navya', 'minnu'}
ntr
sree
arjun
harshitha
sravani
navya
minnu
'''
#task5


python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

union = python_students.union(da_students)
print("Union:", union)

common = python_students.intersection(da_students)
print("Intersection:", common)

differ = python_students.difference(da_students)
print("Difference:", differ)

symmetric_differ = python_students.symmetric_difference(da_students)
print("Symmetric Difference:", symmetric_differ)

subset = da_students.issubset(python_students)
print("Subset:", subset)

superset = python_students.issuperset(da_students)
print("Superset:", superset)

disjoint = python_students.isdisjoint(da_students)
print("Both are Disjoint:", disjoint)

print("All students:")
for i in union:
    print(i)

print("Common students:")
for i in common:
    print(i)
