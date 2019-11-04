import numpy as np

trial = [9,3,1]

def insertionSort(A, *args, **kwargs):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted seq A[1..j-1]
        i = j-1
        while (i > 0) and (A[i] > key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

print(insertionSort(trial))
for n in range(1,len(trial)):
    print(n)