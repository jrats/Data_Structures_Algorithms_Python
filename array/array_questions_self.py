#QUESTION 1
# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5

#Solution 1

def missing_number(arr, n):
    # TODO
    for i in range (1, n-1):
        if arr[i] != arr[i-1]+1:
            return arr[i-1]+1
        
# Solution 2

def missing_number(arr, n):
    # TODO
    total = n*(n+1)//2
    sum_arr = sum(arr)
    missing_number = total - sum_arr
    return missing_number

# QUESTION 2

# TWO SUM LEETCODE

#brute force
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i]+nums[j] == target:
                return i, j

#two pointer approach
def two_sum(nums, target):
    nums.sort()
    i = 0
    j = len(nums)-1
    while i!=j:
        if nums[i]+nums[j] == target:
            return [i, j]
        elif nums[i]+nums[j] > target:
            j= j-1
        else:
            i= i+1

# hashmap/dict approach
def two_sum_hashmap(nums, target):
    check = {}
    for i in range(len(nums)):
        if (nums[i]) not in check:
            check[target-nums[i]] = i
        else:
            return check[nums[i]], i

        
nums = [2,7,11,15]
target= 9
ans = two_sum_hashmap(nums, target)
print(ans)


#Question 3 
# How to find if an array has a given element or not

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findNumber(arr, ele):
    for i in range(len(arr)):
        if arr[i] ==ele:
            return i 

idx = findNumber(myArray, 20)
print(idx)


#Question 4
# Permutation 
def permutation(l1, l2):
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else: 
        return False
    
l1=[1,6,2,7,4,3]
l2=[1,3,2,6,7,4]
ans=permutation(l1, l2)
print(ans)







