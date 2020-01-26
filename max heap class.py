
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

class max_heap(object):
    """ Class converts input array into a max-heap object where each parent node is >= to its children.
    Takes an array as input. Does not mutate array.
    Class can:
        - return the heap
        - return a maximum value in the heap
        - extract the maximum value in the heap (return and remove it)
        - increase the value of a key 
        - insert a new key
        - return a sorted array with heap sort
    Functions are based on material in Introduction to Algorithm by CLRS,
    chapter 6, pages 150 -169 """

    def build_max_heap(self,arr):
        """ Takes as input an unordered array and returns a max-heap
        The -1 in the heapsize eq accounts for Python indexing (starting at 0 not 1)
        All elements in arr[n/2....n] are leaves, have no children, therefore satisfying the max-heap property
        This algorithm iterates over nodes, arr[n/2....0], calling max_heapify on each node
        Running time: O(n) linear """
        
        heapsize = len(arr)-1
        for i in range(heapsize//2,-1,-1):
            self.max_heapify(arr,i,heapsize)

    def max_heapify(self,arr,i,heapsize):

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
            self.max_heapify(arr,largest,heapsize)

    def __init__(self,array):
        self.array = array[:] # Remove [:] IOT mutate input array
        self.build_max_heap(self.array)
    
    def parent(self,i):
        """ returns the parent index position for a child """
        if i == 0:
            return i
        return (i-1)//2

    def get_heap(self):
        """ returns the heap as an array """
        return self.array

    def get_heap_maximum(self):
        """ Returns the max value of the heap but doesn't remove it """
        return self.array[0]

    def extract_heap_maximum(self):
        """ Removes and returns the a maximum value in the heap """
        heapsize = len(self.array)-1
        if heapsize < 1:
            raise Exception ("Heap Overflow")
        maximum = self.array[0]
        self.array[0] = self.array[heapsize]
        self.array.__delitem__(-1)
        heapsize -= 1
        max_heapify(self.array,0,heapsize)
        return maximum

    def heap_increase_key(self,i,key):
        """ Takes as input i, the index position of the key we wish to increase
        and key, the new value for i.
            - Changes value of i to key
            - Then moves i, if necessary, towards the root in order to satisfy the max heap principle """
        if key < self.array[i]:
            raise Exception ("New key is smaller than current key")
        self.array[i] = key
        while i > 0 and self.array[self.parent(i)] < self.array[i]:
            self.array[i],self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)

    def max_heap_insert(self,key):
        """ Takes as input a new key to be added to the heap
        Appends numpy -Inf as a sentinal, then calls heap_increase_key """ 
        from numpy import Inf
        self.array.append(-Inf)
        self.heap_increase_key(len(self.array)-1,key)

    def heap_sort(self):
        """ Running time: O (n lg n) """
        heapsize = len(self.array)-1
        for i in range(len(self.array)-1,0,-1):
            self.array[0],self.array[i] = self.array[i],self.array[0]
            heapsize -= 1
            self.max_heapify(self.array,0,heapsize)

test = [1,2,3,4,5,6,7,8,9,19]

# create an instance
example = max_heap(test)

# print out heap:
print("The heap looks like:", example.get_heap())

# print out heap maximum:
print("The heap maximum is", example.get_heap_maximum())

# extract heap maximum:
print("Extracting the heap maximum returns", example.extract_heap_maximum(), "and the new heap looks like:", example.get_heap()) # Showing the extracted maximum was removed

# increase the value of a key:
example.heap_increase_key(7,11)
print("Increasing the key for heap[7] to a value of 11 returns", example.get_heap())
# print(example.get_heap())

# insert a new key into the heap:
example.max_heap_insert(12)
print("Inserting a new key with the value of 12 returns", example.get_heap())

# use heap sort
print("Calling heap_sort method returns", example.heap_sort(), example.get_heap())

