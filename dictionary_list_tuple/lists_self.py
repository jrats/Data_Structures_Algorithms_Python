import numpy as np
myList= [2,56,34,23,86, 45, 23, 70, 60, 40]
print(myList)
# myList.insert(3, 15)
# print(myList)

# myList.append(90)
# print(myList)

# myList2 = [15,29,45,84]
# myList.extend(myList2)
# print(myList)

# myList = ['a','b','c','d','e','f']
# myList[0:2] = ['x', 'y']
# print(myList[0:2])

# print(myList.pop(3))
# print(myList)

# del myList[2:]
# print(myList)

# myList.remove('c')
# print(myList)

# target = 40
# if target in myList:
#     print('Found')
# else:
#     print('Not found')


# #Linear Search 

# def linear_search(p_list, p_target):
#     for i, val in enumerate(p_list):
#         if val == p_target :
#             return (f'Element found at index {i}')
#     return ('Element not found')

# print(linear_search(myList, target))

# Operators/ Functions

# a = [1,2,3]
# b = [4,5,6]
# c = a + b    # concatenate operator
# print(c)

# print(a*4)  # star operator

# print(len(a))

# print(max(b))

# print(min(b))

# print(sum(b))

# print(sum(b)/len(b))

# l = []
# while(True):
#     inp = (input("Enter the number here"))
#     if inp == 'Done':
#         break 
#     l.append(float(inp))
# avg = sum(l)/len(l)
# print(avg)

a = 'spam'
b = list(a)
print(b)

a = "What a beautiful day"
b = a.split()
print(b)

a = "How, nice, of you"
b = a.split(',')
print(b)

print(','.join(b))

# myList = myList.sort()  # won't work

# myList.sort()
# myList.insert(3, 56)
# print(myList)

# new_list = sorted(myList)   # sorted doesn't change the list in place

# print(new_list)

# print(myList)

# Arrays vs List

myArray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5]

print (myArray/2)
# print(myList/2)  # doesn't work


#List Comprehension 
#for loop

prev_list = [1,2,3]
# new_list = []
# for i in prev_list:
#     multiply_2 = i*2
#     new_list.append(multiply_2)
# print(new_list)

new_list = [item*2 for item in prev_list]
print(new_list)

# list comprehension with strings
var = "Python"
l = [x for x in var]
print (l)

def lis_function(x):
    if x > 0:
        x = -1 * x
        return x
    else:
        return 0


#Conditional list comprehension

prev_list = [-1, -2, 4, 5, 6, -7, 8, -9]
new_list = [i*2 for i in prev_list if i>0]
new_list2 = [i*i if i>0 else 0 for i in prev_list]
new_list3 = [lis_function(i) for i in prev_list]
print(prev_list)
print(new_list)
print(new_list2)
print(new_list3)

sentence = "My name is Juhi"

consonants = [ i for i in sentence if i.isalpha() and i.lower() not in 'aeiou']
print(consonants)



















