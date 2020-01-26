
import time

### These are solutions for a 1d peak finding problem

it_numsteps = 0
rec_numsteps = 0

arr = list(range(1,10000000))
arr[-1] = 95

def iterative_peak_finder(arr):
    """ running time: theta(n) """
    # special cases:
    # first and last index positions only have one neighbor
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[-1] >= arr[-2]:
        return arr[-1]
    # main:
    for i in range(1,len(arr)-1):
        global it_numsteps
        it_numsteps += 1
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]

def peak_finder_1d(arr):
    """ Finds a peak recursively 
    running time: theta(log2n) """
    n = len(arr)
    global rec_numsteps
    rec_numsteps += 1
    # base cases
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0],arr[1])
    if arr[n//2] >= arr[n//2+1] and arr[n//2] >= arr[n//2-1]:
        return arr[n//2]

    # if both neighbors are larger than arr[n//2], pick the largest
    if arr[n//2] < arr[n//2+1] and arr[n//2] < arr[n//2-1]:
        if arr[n//2+1] > arr[n//2-1]:
            return peak_finder_1d(arr[n//2::][:])
        else:
            return peak_finder_1d(arr[0:n//2][:])
    # pick the right (if n//2 + 1 is larger)
    if arr[n//2] < arr[n//2+1]:
        return peak_finder_1d(arr[n//2+1::][:])
    # pick the left (if n//2 - 1 is larger)
    if arr[n//2] < arr[n//2-1]:
        return peak_finder_1d(arr[0:n//2][:])    

start = time.time()
print(iterative_peak_finder(arr), "found in", it_numsteps, "found in", (time.time() - start), "seconds")
# 9999998 found in 9999997 found in 2.371116876602173 seconds

start1 = time.time()
print(peak_finder_1d(arr), "found in", rec_numsteps, "found in", (time.time() - start1), "seconds")
# 9999998 found in 22 found in 0.1861588954925537 seconds