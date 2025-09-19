def linear_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return f'Found at index {i}'
    return -1

def binary_search(arr, ele):
    l = 0
    r = len(arr) -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid] > ele:
            r = mid -1
        else:
            l = mid +1
    return -1
    




print(binary_search([10,20,30,40,50,60],50))


