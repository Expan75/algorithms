import numpy as np

trial = [9,6,8,9,3,4,1,11,3,4,9,0]

def insertionSort(A, *args, **kwargs):
    res = A
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted seq A[1..j-1]
        i = j-1
        while (i >= 0) and (A[i] > key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return res

print(insertionSort(trial))

