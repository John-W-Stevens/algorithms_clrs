
def insertion_sort(arr):
    """ From Introduction to Algorithms by Corman, et al
    pgs. 16-22. Sorts elements in place
    wosrt case running time: theta(n^2) """
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
            arr[i+1] = key
    return arr

### Test ###
alist = [5,3,8,2,1,9,7,2,6,4]
print(insertion_sort(alist))