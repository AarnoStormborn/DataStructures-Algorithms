# worst O(n^2)
# space O(1)

import numpy as np
import time as tm

def insert_sort(a):
    l = len(a)
    for i in range(1,l):
        key = a[i]
        j = i-1
        while j>=0 and key<a[j]:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key 
    return a

def check(a): 
    l = len(a) 
    if l <= 1:
        return 
    for i in range(l-1): 
        if a[i] > a[i+1]:
            return False
    return True 


n = int(input("Enter array size: "))
a = np.random.random(n)
start = tm.time()
arr = insert_sort(a)
end = tm.time()-start
if not check(arr):
    print("Array is not sorted")
else: 
    print("Array is sorted")
    print("Time taken:",end)
