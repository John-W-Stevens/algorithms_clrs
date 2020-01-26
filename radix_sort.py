
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

A = [150,993,999,12,18,756,456,98,3]
print (radix_sort(A,10))
# Output: [3, 12, 18, 98, 150, 456, 756, 993, 999]