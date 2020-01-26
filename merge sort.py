
# Import numpy to use Inf as a sentinal
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

### Test Case:
alist = [14,12,15,11,19,23,18,16,7,20,5,8]
merge_sort(alist, 0, len(alist) - 1)

print(alist) # [5, 7, 8, 11, 12, 14, 15, 16, 18, 19, 20, 23]