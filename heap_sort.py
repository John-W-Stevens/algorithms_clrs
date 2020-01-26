############### Basic Heap Sort Algorithms #################
# These three functionars are all that is necessary to take
# an array, convert it into a max-heap, and run heap sort on it

def max_heapify(arr,i,heapsize):

    """ Takes as input an array, an index position, and the heapsize.
    i represents the node we suspect of violating the max-heap property
    
    Assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps,
    but that arr[i] might be smaller than its children (violating the max-heap property).

    max_heapify lets the value at arr[i] "float down" in the max-heap so that the subtree
    rooted at index i obeys the max-heap property. 
    
    Corrects a single violation of the max heap property in a sub-tree's root

    Running time: O (lg n) """
    
    # print(arr)

    # left child for node i
    left = 2 * i + 1 
    # right child for node i
    right = 2 * i + 2

    if left <= heapsize and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right <= heapsize and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,heapsize)

def build_max_heap(arr):
    """ Takes as input an unordered array and returns a max-heap
    The -1 in the heapsize eq accounts for Python indexing (starting at 0 not 1)
    All elements in arr[n/2....n] are leaves, have no children, therefore satisfying the max-heap property
    This algorithm iterates over nodes, arr[n/2....0], calling max_heapify on each node
    Running time: O(n) linear """
    
    heapsize = len(arr)-1
    for i in range(heapsize//2,-1,-1):
        max_heapify(arr,i,heapsize)

def heap_sort(arr):
    """ Takes as input an array,
    Running time: O (n lg n) """
    heapsize = len(arr)-1
    build_max_heap(arr)
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapsize -= 1
        max_heapify(arr,0,heapsize)

############### Basic Heap Sort Algorithms #################
