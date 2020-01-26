
def bubble_sort(array):
    """ This is a horribly inefficient sorting algorithm """
    for i in range(0,len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j - 1]:
                array[j],array[j-1] = array[j-1],array[j]
    return array

import time
test = list(range(1000,0,-1))
start = time.time()
sorted_array = bubble_sort(test)
elapsed = (time.time() - start)
print("Bubble sort algorithm sorted an array of",len(test),"elements in", elapsed, "seconds")
# Bubble sort algorithm sorted an array of 1000 elements in 0.12065720558166504 seconds