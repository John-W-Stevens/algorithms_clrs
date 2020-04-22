


def partition(arr,p,r):
    """
    The key to quicksort is the partition sub-routine, which rearranges
    the subarray arr[p..r] in place
    """
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quicksort(arr,p,r):
    """
    Input: arr (array), p (starting index), r (ending index)
    Method: Divide and Conquer
        a. Divide - Partition (rearrange) the array arr[p..r] into two (possibly empty)
           subarrays arr[p..q-1] and arr[q+1..r] such that each element of arr[p..q-1] is
           less than or equal to arr[q], which is, in turn, less than or equal to each
           element of arr[q+1..r]. Compute the index of q as part of this partitioning procedure.
        b. Conquer - Sort the two subarrays arr[p..q-1] and arr[q+1..r] by recursive calls to quicksort.
        c. Combine - Because the subarrays are already sorted, no work is needed to combine them:
           the entire array arr[p..r] is now sorted
    Time complexity: theta(n^2).
        note: Despite the thest(n^2) worse case running time, quicksort is "remarkably efficient
              on average."
    * The above description is a quotation from CLRS, pgs 170 - 171 *
    """
    if p < r:
        q = partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)

# test array:
alist = [14,12,15,11,19,23,18,16,7,20,5,8]

# call quicksort() on alist:
quicksort(alist,0,len(alist)-1)

# get output:
print(alist) # [5, 7, 8, 11, 12, 14, 15, 16, 18, 19, 20, 23]