import numpy as np 
from time import time

def selectionSort(lis):
    
    for i in range(len(lis)):
        min = i
        for j in range(i+1, len(lis)):
            if lis[j]<lis[min]:
                min = j
        
        temp = lis[min]
        lis[min] = lis[i]
        lis[i] = temp
    return lis

n = int(input('Enter size of list: '))
inp_lis = np.random.random(n)
start = time()
selectionSort(inp_lis)
print(f"Time taken: {time()-start:.6f}")

