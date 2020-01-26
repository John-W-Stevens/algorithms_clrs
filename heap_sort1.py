# We will use the heap abstract data type (ADT)
# This ADT is used to model priority queues
# This structure implements a set, 'S', of elements, each element being associated with a key

# Operations we can do on a priority queue:
    # insert (S,x) - insert element x into set S
    # max(S) - return max element x (the element with the largest key)
    # extract_max(S) - returns element with largest key AND removes it from S
    # increase_key(S,x,k) - increase value of x's key to the new value of k

# Hea
# Implementation of a priority queue
# It is an array, visualized as a nearly complete binary tree
    # Example: suppose we have an array of 10 elements:
        # arr = [16,15,23,7,18,4,6,9,11]
        # The root of the the tree is arr[0]
        # arr[0] has two children, arr[1] and arr[2]
        # arr[1] has two children, arr[3] and arr[4]
        # arr[2] has two children, arr[5] and arr[6]
        # and so on until for all the elements of the array
        # Note, we can think of each element as a node, starting at node1 (16, which is arr[0])

# Heap as a tree (Definition of a basic heap structure)
    # Note, 'i' below refers to the node, starting at 1
# Root of tree is the first element (i = 1)
# parent(i) = i//2
# left_child(i) = 2i
# right_child(i) = 2i+1

# Max heap property: The key of a node is >= the keys of its children
    # This structure can trivially handle max(S):
        # however, it cannot handle extract_max(S) trivially

# Min heap property: The key of a node is <= the keys of its children

# How do we maintain the max heap property while extracting max from the heap

# Heap operations:

# Build max heap 
# max heapify

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

################ Test cases ######################
# test = [16,4,10,14,7,9,3,2,8,1]
# max_heapify(test,1,len(test)) 
# test[1] is the node we believe is violating our max-heap property
# output: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] a corrected heap
################ Test cases ######################

def build_max_heap(arr):
    """ Takes as input an unordered array and returns a max-heap
    The -1 in the heapsize eq accounts for Python indexing (starting at 0 not 1)
    All elements in arr[n/2....n] are leaves, have no children, therefore satisfying the max-heap property
    This algorithm iterates over nodes, arr[n/2....0], calling max_heapify on each node
    Running time: O(n) linear """
    
    heapsize = len(arr)-1
    for i in range(heapsize//2,-1,-1):
        max_heapify(arr,i,heapsize)

################ Test cases ######################
# test1 = [1,2,4,8,7,9,3,10,14,16]
# build_max_heap(test1)
# output: [16,14,9,10,7,4,3,1,8,2]

# import random
# test2 = [random.randint(1,50) for n in range(1,25)]
# print(test2) # [8, 25, 21, 19, 5, 1, 47, 14, 23, 33, 18, 12, 36, 32, 34, 13, 26, 6, 49, 38, 24, 15, 1, 5]
# build_max_heap(test2)
# print(test2) # [49, 38, 47, 26, 33, 36, 34, 25, 23, 24, 18, 12, 1, 32, 21, 13, 14, 6, 19, 5, 8, 15, 1, 5]
################ Test cases ######################

def heap_sort(arr):
    """ Takes as input an array,
    Running time: O (n lg n) """
    heapsize = len(arr)-1
    build_max_heap(arr)
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapsize -= 1
        max_heapify(arr,0,heapsize)

################ Test cases ######################
# test = [16,14,10,8,7,9,3,2,4,1]
# heap_sort(test)
# print(test) # Output: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

# test2 = [5,13,2,25,7,17,20,8,4]
# heap_sort(test2)
# print(test2) # Output: [2, 4, 5, 7, 8, 13, 17, 20, 25]
################ Test cases #######################