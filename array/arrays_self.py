import array

# my_array = array.array('i')
# print(my_array)
# my_array1 = array.array('i', [1,2,3,4])
# print(my_array1)

import numpy as np 
# np_array = np.array([], dtype = int)
# print(np_array)
np_array1 = np.array([1,2,3,4])
np_array2 = np.array([10, 12])
print(np_array1)

# my_array1.insert(2,6)
# print(my_array1)

# new_array = np.insert(np_array1, 3, 6)
# print(new_array)

# combined_array = np.insert(np_array1, 2, np_array2)
# print(combined_array)

# def traverse_array(arr):
#     for i in arr:
#         print (i)

# traverse_array(np_array1)  
# def linear_search(arr, ele):
#     for i in range(len(arr)):
#         if arr[i]==ele:
#             return i
#     return("Element not present in array")

# idx = linear_search(np_array1, 4)
# print(idx)

# new_arr=np.delete(np_array1, 3)

# print(new_arr)


def delete_ele(arr, ele):    #deleting an element from scratch in an array
    found = False
    n= len(arr)
    for i in range(len(arr)):
        if found:
            arr[i-1]=arr[i]
        if arr[i] == ele:
            found = True
    n = n-1 

    for i in range(n):
        print(arr[i], end =' ')

delete_ele(np_array1, 3)