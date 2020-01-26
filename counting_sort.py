

def counting_sort(A,k=None):
    """ From CLRS 8.2, pg. 194.    

    Assumes that each of the n input elements is an integer in the range 0 to k,
    for some integer k. When k = O(n), the sort runs in theta(n) time.
    A - the array to be sorted.
    k - the largest term in the array 
    Returns B, a sorted array without mutating A """
    
    # If no key is supplied then k = max integer in array
    if not k:
        k = max(A)

    # B - array to hold the sorted output
    # C - array providing temporary working storage
    
    B = [None] * len(A) 
    C = [0 for i in range(k+1)]

    # Get C[i] to contain the number of elements == i
    for j in range(0,len(A)):
        C[A[j]] += 1
 
    # Get C[i] to contain the number of element <= i
    for i in range(1,k+1):
        C[i] += C[i-1]

    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1

    return B

def test():
    import time
    start = time.time()
    test_array = [2,5,3,0,2,3,0,3]

    print(f"{counting_sort(test_array,5)} found in {time.time()-start} seconds")
    # Output with key: [0, 0, 2, 2, 3, 3, 3, 5] found in 1.621246337890625e-05 seconds

    print(f"{counting_sort(test_array)} found in {time.time()-start} seconds")
    # Output without key: [0, 0, 2, 2, 3, 3, 3, 5] found in 7.915496826171875e-05 seconds

test()

test_array = [2,5,3,0,2,3,0,3]

