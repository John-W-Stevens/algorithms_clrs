
class heap(object):
    """ Class converts input array into a heap object. 
    Default settings create a max-heap object where each parent node is >= to its children.
    if MIN=True is specified, then class will create a min-heap object where each parent node is <= to its children.
    
    Takes an array as input. Does not mutate array.

    Class has the following methods for both min and max heap objects:
        - return the heap
        - return a extreme (max or min) value in the heap
        - extract the extreme (max or min) value in the heap (return and remove it)
        - change the value of a key
        - insert a new key
        - sort heap
            - for a min-heap, heap is sorted in descending order
            - for a max-heap, heap is sorted in ascending order
    
    Functions are based on material from Introduction to Algorithm by CLRS,
    chapter 6, pages 150 -169 """

    def build_heap(self,arr):
        """ Takes as input an unordered array and returns a heap
        All elements in arr[n/2....n] are leaves, have no children, and therefore satisfy the max-heap property
        This algorithm iterates over nodes, arr[n/2....0], calling heapify on each node
        Running time: O(n) linear """
        
        heapsize = len(arr)-1
        for i in range(heapsize//2,-1,-1):
            self.heapify(arr,i,heapsize)

    def heapify(self,arr,i,heapsize):

        """ Takes as input an array, an index position, and the heapsize.
        i represents the node we suspect of violating the applicable max or min-heap property
        
        Assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are max or min heaps (whichever applies),
        but that arr[i] might be smaller or larger than its children (violating the max or min-heap property).

        heapify lets the value at arr[i] "float down" in the max-heap and "float up" in the min-heap 
        so that the subtree rooted at index i obeys the the applicable max or min-heap property. 
        
        Corrects a single violation of the max or min-heap property in a sub-tree's root

        Running time: O (lg n) """
        
        # print(arr)

        # left child for node i
        left = 2 * i + 1 
        # right child for node i
        right = 2 * i + 2

        if not self.MIN:
            if left <= heapsize and arr[left] > arr[i]:
                largest = left
            else:
                largest = i
            if right <= heapsize and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i],arr[largest] = arr[largest],arr[i]
                self.heapify(arr,largest,heapsize)
        if self.MIN:
            if left <= heapsize and arr[left] < arr[i]:
                largest = left
            else:
                largest = i
            if right <= heapsize and arr[right] < arr[largest]:
                largest = right
            if largest != i:
                arr[i],arr[largest] = arr[largest],arr[i]
                self.heapify(arr,largest,heapsize)

    def __init__(self,array,MIN=False):
        self.array = array[:] # Remove [:] IOT mutate input array
        self.MIN = MIN
        self.build_heap(self.array)
    
    def parent(self,i):
        """ returns the parent index position for a child """
        if i == 0:
            return i
        return (i-1)//2

    def get_heap(self):
        """ returns the heap as an array """
        return self.array

    def get_heap_extreme(self):
        """ Returns the max value of the heap but doesn't remove it """
        return self.array[0]

    def extract_heap_extreme(self):
        """ Removes and returns the a maximum value in the heap """
        heapsize = len(self.array)-1
        if heapsize < 1:
            raise Exception ("Heap Overflow")
        maximum = self.array[0]
        self.array[0] = self.array[heapsize]
        self.array.__delitem__(-1)
        heapsize -= 1
        self.heapify(self.array,0,heapsize)
        return maximum

    def heap_change_key(self,i,key):
        """ Takes as input i, the index position of the key we wish to change
        and key, the new value for i.
            - Changes value of i to key
            - Then moves i, if necessary, towards or away from the root in order to satisfy 
            the applicable max or min heap principle """
        if not self.MIN:
            if key < self.array[i]:
                raise Exception ("New key is smaller than current key")
            self.array[i] = key
            while i > 0 and self.array[self.parent(i)] < self.array[i]:
                self.array[i],self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
                i = self.parent(i)
        if self.MIN:
            self.array[i] = key
            while i > 0 and self.array[self.parent(i)] > self.array[i]:
                self.array[i],self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
                i = self.parent(i)


    def heap_insert(self,key):
        """ Takes as input a new key to be added to the heap
        Appends numpy -Inf as a sentinal, then calls heap_change_key """ 
        from numpy import Inf
        self.array.append(-Inf)
        self.heap_change_key(len(self.array)-1,key)

    def heap_sort(self):
        """ Calling heap_sort on a min-heap returns an array in decreasing order
        Calling heap_sort on a max-heap returns an array in ascending order
        Running time: O (n lg n) """
        heapsize = len(self.array)-1
        for i in range(len(self.array)-1,0,-1):
            self.array[0],self.array[i] = self.array[i],self.array[0]
            heapsize -= 1
            self.heapify(self.array,0,heapsize)


######### Tests for heap class ##########

############################## Test for min-heap ##############################
print("Test for min-heap")
print()
import random
test1 = [random.randint(1,100) for n in range(1,50)]
print(test1)
print()

# create an instance of a min-heap
example = heap(test1,MIN=True)

# print out heap:
print("The heap looks like:", example.get_heap())
print()

# print out heap extreme (max or min):
print("The heap extreme is", example.get_heap_extreme())
print()

# extract heap extreme:
print("Extracting the heap extreme returns", example.extract_heap_extreme(), "and the new heap looks like:", example.get_heap()) # Showing the extracted maximum was removed
print()

# insert a new key into the heap:
example.heap_insert(12)
print("Inserting a new key with the value of 12 returns", example.get_heap())
print()
# use heap sort
example.heap_sort()
print("Calling heap_sort method returns", example.get_heap())
print()
############################## Test for min-heap ##############################


############################## Test for max-heap ##############################
print("Test for max-heap")
print()
import random
test1 = [random.randint(1,100) for n in range(1,50)]
print(test1)
print()

# create an instance of a max-heap
example = heap(test1)

# print out heap:
print("The heap looks like:", example.get_heap())
print()

# print out heap extreme (max or min):
print("The heap extreme is", example.get_heap_extreme())
print()

# extract heap extreme:
print("Extracting the heap extreme returns", example.extract_heap_extreme(), "and the new heap looks like:", example.get_heap()) # Showing the extracted maximum was removed
print()

# insert a new key into the heap:
example.heap_insert(12)
print("Inserting a new key with the value of 12 returns", example.get_heap())
print()
# use heap sort
example.heap_sort()
print("Calling heap_sort method returns", example.get_heap())
print()
############################## Test for max-heap ##############################
