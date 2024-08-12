# -*- coding: utf-8 -*-
"""Insetionmerge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-iBlYDaWyl0wpg6Llcq-a-euetbnBz8O
"""

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Insertion sort"""

def insertionSort(arr):

    for i in range(1, len(arr)): # Traverse through array from index 1

        key = arr[i] # Pick up value at each index starting from index 1

        j = i-1 # j is to present the indexes before the key index
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            # While the elements before the key are greater than the key
            # Move elements one to the right
        arr[j + 1] = key
        # Once the element is smaller than the key
        # Insert the key to the right of that element
    return arr

"""Merge sort"""

def merge(arr1, arr2):
    i = j = 0
    sorted_arr = []
    while (i != len(arr1) and j != len(arr2)):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sorted_arr.append(arr2[j])
            j += 1
        else:
            sorted_arr.append(arr1[i])
            sorted_arr.append(arr2[j])
            i += 1
            j += 1
    while i != len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j != len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

"""Hybrid Sort"""

def hybridSort(arr,S):
    if len(arr)<=1:
        return arr

    if len(arr) > S:
        m = len(arr)//2 # Find midpoint m

        # Sort first and second halves
        arr[:m] = hybridSort(arr[:m],S)
        arr[m:] = hybridSort(arr[m:],S)
        arr = merge(arr[:m], arr[m:])

        return arr
    else:
        arr = insertionSort(arr)
        return arr

arr = [3,6,8,9,2,1,4,5,10,7,12,11,3,3,3]
a = hybridSort(arr,4)
print(a)
type(a)

"""Generate input data"""

arrSizes = []

for i in range(10):
    arrSizes.append(1000*(i+1))
    arrSizes.append(10000*(i+1))
    arrSizes.append(100000*(i+1))
    arrSizes.append(1000000*(i+1))

arrSizes = list(dict.fromkeys(arrSizes))
arrSizes.sort()
print(arrSizes)

arrOfArrays = []


for siz in arrSizes:
    arr = np.random.randint(1000, size=siz)
    arrOfArrays.append(arr)

print(arrOfArrays[0])

"""Analyse time complexity

Count key comparison
"""

def insertionSort2(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        if j > 0 :
            comparisons += 1
        arr[j + 1] = key
    return arr, comparisons

def merge2(arr1, arr2):
    comparisons = 0
    i = j = 0
    sorted_arr = []
    while (i != len(arr1) and j != len(arr2)):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sorted_arr.append(arr2[j])
            j += 1
        else:
            sorted_arr.append(arr1[i])
            sorted_arr.append(arr2[j])
            i += 1
            j += 1
        comparisons += 1
    while i != len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j != len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr, comparisons

def hybridSort2(arr,S):
    comparisons = 0
    if len(arr)<=1:
        return arr, comparisons

    if len(arr) > S:

        m = len(arr)//2

        arr[:m], first_half_comparisons = hybridSort2(arr[:m],S)
        comparisons += first_half_comparisons

        arr[m:], second_half_comparisons = hybridSort2(arr[m:],S)
        comparisons += second_half_comparisons

        arr, merge_comparisons = merge2(arr[:m], arr[m:])
        comparisons += merge_comparisons

        return arr, comparisons

    else:

        arr, comparisons = insertionSort2(arr)
        return arr, comparisons

# def hybridSort3(arr, S):
#     comparisons = 0
#     if len(arr) <=1:
#         return arr, comparisons
#     # Mergesort if Arr > size S
#     if len(arr) > S:
#         # Finding the mid of the array
#         mid = len(arr)//2

#         # Sorting the first half of the array
#         arr[:mid], temp = hybridSort2(arr[:mid], S)
#         comparisons += temp

#         # Sorting the second half of the array
#         arr[mid:], temp = hybridSort2(arr[mid:], S)
#         comparisons += temp

#         i = 0
#         j = mid

#         # Merge 2 halves of the array
#         while i < j and j < len(arr):
#             if arr[i] <= arr[j]:
#                 i += 1
#             else:
#                 item = arr[j]
#                 arr[i+1:j+1] = arr[i:j]
#                 arr[i] = item
#                 i += 1
#                 j += 1
#             comparisons += 1

#         return arr, comparisons
#     else:
#         arr, comparisons = insertionSort2(arr)
#         return arr, comparisons

"""With s fixed, plot key comparisons with different sizes of n"""

from random import seed
from random import randint

np.random.seed(22)
arrSize = []

for i in range(1000):
    arrSize.append(i)

s = 10

if __name__ == '__main__':
    sizeComparisons = []
    for siz in arrSize:
        arr = np.random.randint(10000, size=siz)
        arr, comparisons = hybridSort2(arr,s)
        sizeComparisons.append(comparisons)

import math

theorectical_comparisons = []
for siz in arrSize:
    if siz == 0:
        theorectical_comparisons.append(0)
    else:
        c = siz * math.log2(siz/s) - (siz/s - 1) + siz/s * (s-1) * (s+2)/4
        theorectical_comparisons.append(c)

f = plt.figure(figsize=(20,20))
ax = f.add_subplot(211)
ax.plot(arrSize, sizeComparisons)
ax.plot(arrSize, theorectical_comparisons)
ax.set_xlabel("Array Size, n")
ax.set_ylabel("Key Comparisons")
ax.set_title("Key Comparisons against Array Size")

"""N is fixed different S"""

np.random.seed(22)
if __name__ == '__main__':
 sValues = range(0,100)
 arraySize = 10000 # Set array size to 10000
 sComparisons = []
 for s in sValues:
    arr = np.random.randint(10000,size = arraySize)
    arr, comparisons = hybridSort2(arr,s)
    sComparisons.append(comparisons)

theorectical_comparisons = []
for s in sValues:
    if s == 0:
        theorectical_comparisons.append(0)
    else:
        a = arraySize * math.log2(arraySize/s) - (arraySize/s - 1) + arraySize/s * (s-1) * (s+2)/4
        theorectical_comparisons.append(a)

f = plt.figure(figsize=(20,20))
ax = f.add_subplot(211)
ax.plot(sValues,sComparisons)
ax.plot(sValues,theorectical_comparisons)
ax.set_xlabel("Threshold Values, S")
ax.set_ylabel("Key Comparisons")
ax.set_title("Key Comparisons against Threshold Values, S")

"""Determine optimal S

"""

def mergeSort(arr):
    comparisons = 0
    if len(arr)<=1:
        return arr, comparisons
    else:
        m = len(arr)//2
        arr[:m], first_half_comparisons = mergeSort(arr[:m])
        comparisons += first_half_comparisons
        arr[m:], second_half_comparisons = mergeSort(arr[m:])
        comparisons += second_half_comparisons
        arr, merge_comparisons = merge2(arr[:m], arr[m:])
        comparisons += merge_comparisons

        return arr, comparisons

np.random.seed(22)
if __name__ == '__main__':
 optimalS = 0
 arraySize = range(0,20)
 mergeComparisons = []
 insertionComparisons = []
 mergeComparison = 0
 for s in arraySize:
    arr = np.random.randint(10000,size = s)
    arr2 = arr.copy()
    arr,mergeComparison = mergeSort(arr)
    arr2, insertionComparison = insertionSort2(arr2)
    if insertionComparison < mergeComparison:
        optimalS = s
    mergeComparisons.append(mergeComparison)
    insertionComparisons.append(insertionComparison)

f = plt.figure(figsize=(20,20))
ax = f.add_subplot(211)
ax.plot(arraySize,mergeComparisons, label="MergeSort")
ax.plot(arraySize, insertionComparisons, label = "InsertionSort")
ax.set_xlabel("Array Size")
ax.set_ylabel("Key Comparisons")
ax.set_title("Key Comparisons against Array Size for Merge/Insertion Sort")
ax.legend()

print('Optimal S is:', optimalS)

"""Compare with orginal merge sort

"""

np.random.seed(22)
if __name__ == '__main__':
        arr10mil = []
        arr10mil = np.random.randint(10000000,size =10000000)
        arr10mil_2 = arr10mil.copy()

        start_time1 = time.time()
        arr10mil, hybridComparisons = hybridSort2(arr10mil, 7)
        end_time1 = (time.time() - start_time1)

        start_time2 = time.time()
        arr10mil_2, mergeComparisons = mergeSort(arr10mil_2)
        end_time2 = (time.time() - start_time2)

print("CPU Time for Hybrid Sort is:", end_time1)
print("CPU Time for Merge Sort is:", end_time2)
print("Key Comparisons for Hybrid Sort is:", hybridComparisons)
print("Key Comparisons for Merge Sort is:", mergeComparisons)