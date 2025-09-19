import numpy as np

twod_arr = np.array([[12, 23,56, 43],[12,37,63,24],[12,49,52,92],[91,32,62,23]])
print(twod_arr)

# insert_arr = np.insert(twod_arr, 3, [[1,2,3,4]], axis = 0)  #axis =1 for coloums , 0 for rows

# print(insert_arr)

#to append row/col at the end of the 2d array

# append_arr = np.append(twod_arr, [[0],[5],[3],[2]], axis=1 )
# print(append_arr)

def access_ele(arr, row, col):
    if row>=len(arr) or col>=len(arr[0]):
        print ("Indexes out of range")
    print(arr[row][col])

access_ele(twod_arr, 2, 3)

def traverse_arr(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            print (arr[i][j])

traverse_arr(twod_arr)

def search_ele(arr, ele):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==ele:
                return f"element present at {i} row and {j} column"
            

print(search_ele(twod_arr, 52))

    
new_arr= np.delete(twod_arr, 3, axis =0)
print(new_arr)

