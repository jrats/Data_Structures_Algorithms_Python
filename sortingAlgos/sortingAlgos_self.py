import math
import random

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i -1 
        while j >=0 and key<customList[j]:
            customList[j+1] = customList[j]
            j = j-1
        customList[j+1] = key
    return customList

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k+=1

    return customList

def bucketSortNegative(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    minValue = min(customList)
    rangeVal = (maxValue - minValue)/numberofBuckets

    buckets = [[] for _ in range(numberofBuckets)]

    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue)/rangeVal)
            buckets[index_b].append(j)

    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])

    return sorted_array

def mergeSort(customList):
    if len(customList)>1:
        mid = len(customList)//2
        l = customList[:mid]
        r = customList[mid:]

        mergeSort(l)
        mergeSort(r)

        i=j=k=0

        while i<len(l) and j <len(r):
            if l[i] < r[j]:
                customList[k] = l[i]
                i+=1
            else:
                customList[k] = r[j]
                j+=1
            k+=1

        while i <len(l):
            customList[k] = l[i]
            i+=1
            k+=1

        while j <len(r):
            customList[k] = r[j]
            j+=1
            k+=1

    return customList

def pivot(customList,l,r):
    pivot_index = random.randint(l,r)                         #randomised pivot , we can also keep the pivot as the first and last element as well
    customList[l], customList[pivot_index]= customList[pivot_index], customList[l]
    piv = customList[l]
    swap_index = l
    for i in range(l+1, r+1):
        if customList[i]<piv:
            swap_index+=1
            customList[i], customList[swap_index] = customList[swap_index], customList[i]
    customList[l], customList[swap_index] = customList[swap_index], customList[l]
    return swap_index

def quicksort_helper(customList,l,r):
    if l<r:
        pivot_index = pivot(customList, l, r)
        quicksort_helper(customList, l, pivot_index-1)
        quicksort_helper(customList, pivot_index+1, r)
    return customList

def quicksort(customList):
    return quicksort_helper(customList, 0, len(customList)-1)

def heapify(customList, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left<n and customList[left]>customList[largest]:
        largest = left
    if right<n and customList[right]>customList[largest]:
        largest = right

    if largest != i:
        customList[i],customList[largest] = customList[largest], customList[i]
        heapify(customList, n, largest)

def heapSort(customList):
    n = len(customList)

    for i in range((n//2-1), -1, -1):
        heapify(customList, n, i)

    for i in range(n-1, -1, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

    return customList





        






test = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(heapSort(test))