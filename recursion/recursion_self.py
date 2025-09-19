#example#
#factorial

# import sys
# sys.setrecursionlimit(10000)   to set recursion limit

# def factorial(n):
#     assert n>=0 and int(n)==n, 'The number must be positive integer only!'       #constraints
#     if n in [0,1]:                      #base case
#         return 1
#     else:
#         return n * factorial(n-1)       #recursive case
    
# print(factorial(1.5 ))                    



#fibonacci numbers example

def fibonacci(n):
    assert n>=0 and int(n)==n, 'The number should be a positive integer only!'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))


#find the largest element in an array
def findMaxNumRec(sampleArray, n):
    if n ==1:
        return sampleArray[0]
    return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1))

print(findMaxNumRec([-13,-12, -4,],3))
