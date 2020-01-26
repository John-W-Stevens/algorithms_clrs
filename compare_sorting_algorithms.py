
def insertion_sort(arr):
    """ From Introduction to Algorithms by Corman, et al
    pgs. 16-22. Sorts elements in place
    Running time: O(n) linear """
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
            arr[i+1] = key
    return arr

from numpy import Inf 

def merge_sort(array, left, right):
    
    """ From Introduction to Algorithms by Corman, et al pgs. 30-37.
    Complexity: theta(n lg n) where 'lg n' stands for log2n  
    Parameters:
        - array = array to be sorted
        - left = starting index (choose 0)
        - right = ending index (choose length of array - 1) 
        ex: merge_sort(alist,0,len(alist)-1) """

    if left < right:
        # find middle index
        mid = (left + right) // 2

        # sort left half with merge sort
        merge_sort(array, left, mid)

        # sort right half with merge sort
        merge_sort(array, mid + 1, right)

        # merge both halves
        merge(array, left, mid, right)

def merge(array, left, mid, right):
    """ Merges two sorted sequences. """

    # length of left half of array
    n1 = mid - left + 1
    # length of right half of array
    n2 = right - mid

    # create two empty arrays which will be filled in
    # L for left, R for right
    L = [0] * n1 + [0] # Add an extra spot for sentinal
    R = [0] * n2 + [0] # Add an extra spot for sentinal

    # copy left half of array into L
    for i in range(0, n1):
        L[i] = array[left + i]

    # copy right half of array into R
    for j in range(0, n2):
        R[j] = array[mid + 1 + j]

    # put infinity as sentinel value at the end of Both L and R
    L[n1] = Inf
    R[n2] = Inf

    # compare elements in L and R, adding 
    # the smallest values in array[k]
    i,j = 0,0

    for k in range(left, right + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

def radix_sort(A,r,k=None):
    """ 
    Implemenation based off CLRS pgs 194-199 and https://brilliant.org/wiki/radix-sort/

    A - the array to be sorted
    k - the max value in the array. If k=None, function will assign k = max(A)
    r - the base of the number system we want to use 
    
    Returns (and mutates) a sorted A
    """

    import math
    # If no k is specified, k = max value in the array
    if not k:
        k = max(A)

    def counting_sort(A,d,r):
        """ This sub-routine has been modified to support radix-sorting
        A - the array to be sorted.
        d - the digit we want to sort by
        r - the base of the number system we want to use 
        Returns B, a sorted array without mutating A """
        
        # B - array to hold the sorted output
        # C - array providing temporary working storage        
        B = [0] * len(A) 
        C = [0] * int(r)

        # get number of occurances for each digit in A
        for i in range(len(A)):
            digit = int((A[i]/r**d)%r)
            C[digit] = C[digit]+1
        
        # C[i] = cumulative number of digits <= C[i] in A
        for j in range(1,r):
            C[j] += C[j-1]

        for k in range(len(A)-1,-1,-1):
            digit = int((A[k]/r**d)%r)
            C[digit] = C[digit] - 1
            B[C[digit]] = A[k]

        return B
    
    # compute the number of digits needed to represent k
    digits = int(math.floor(math.log(k,r)+1))

    # call counting sort sub-routine repeatedly
    for i in range(digits):
        A = counting_sort(A,i,r)

    return A

### Test Function ####

def compare_sorting_algorithms(array_size):
    import random
    import time    
    
    test_array = list(range(array_size,0,-1))

    print(f"Results for an array of {array_size} elements.")
    if array_size <= 10000:
        start_time_insertion_sort = time.time()
        s_array = insertion_sort(test_array[:])
        print(f"Insertion sort algorithm sorted an array of {array_size} elements in {time.time()-start_time_insertion_sort} seconds.")

    start_time_merge_sort = time.time()
    merge_sort(test_array[:],0,len(test_array)-1)
    print(f"Merge sort algorithm sorted an array of {array_size} elements in {time.time()-start_time_merge_sort} seconds.")
    
    start_time_radix_sort = time.time()
    radix_sort(test_array[:],10,array_size)
    print(f"Radix sort algorithm sorted an array of {array_size} elements in {time.time()-start_time_radix_sort} seconds.")

compare_sorting_algorithms(1000000)

# Results for an array of 5,000 elements:
# Insertion sort algorithm sorted an array of 5000 elements in 2.8907358646392822 seconds.
# Merge sort algorithm sorted an array of 5000 elements in 0.024238109588623047 seconds.
# Radix sort algorithm sorted an array of 5000 elements in 0.021738052368164062 seconds.

# Results for an array of 10,000 elements:
# Insertion sort algorithm sorted an array of 1,000,000 elements in 11.553338289260864 seconds seconds.
# Merge sort algorithm sorted an array of 1,000,000 elements in 0.04891705513000488 seconds.
# Radix sort algorithm sorted an array of 1,000,000 elements in 0.05282187461853027 seconds.

# Results for an array of 100,000 elements:
# Merge sort algorithm sorted an array of 100000 elements in 0.5599691867828369 seconds.
# Radix sort algorithm sorted an array of 100000 elements in 0.6624329090118408 seconds.

# Results for an array of 1,000,000 elements.
# Merge sort algorithm sorted an array of 1000000 elements in 6.440006971359253 seconds.
# Radix sort algorithm sorted an array of 1000000 elements in 7.048583984375 seconds.
