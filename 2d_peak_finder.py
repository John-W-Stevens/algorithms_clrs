# In an mxn matrix where n = rows and m = columns,
# peak exists wherever a point (m,n) in the graph meet this condition:
# (m,n) >= (m-1,n) and (m,n) >= (m+1,n) and (m,n) >= (m,n+1) and (m,n) >= (m,n-1)

# Methodology:
# 1: Pick a middle column j = m/2
# 2: Find global maximium on column j at (i,j)
# 3: Compare (i,j-1), (i,j), (i,j+1)
# 4: Pick left columns if (i,j-1) > (i,j)
# 5: Pick right columns if (i,j+1) > (i,j)
# 6: else: return (i,j)

import random
import numpy as np 

# Counts number of times peak_finder_2d calls itself
num_steps = 0

def peak_finder_2d(matrix):
    """ Finds a peak in a 2d array recursively.
    Process:
     - Choose center column
     - Choose global max in center column at index (i,j)
     - Checks if (i,j-1) <= (i,j) >= (i,j+1)
     - If so, (i,j) is a peak, returns (i,j)
     - If not, check which is larger, (i,j-1) or (i,j+1)
     - If (i,j-1) is larger, repeat process, first removing all columns larger than j
     - If (i,j+1) is larger, repeat process, first removing all columns less than j 
     
     running time: theta( n log2 m ) """

    global num_steps
    num_steps += 1

    n = len(matrix) # number of rows
    m = len(matrix[0]) # number of columns

    j = m//2

    mid_col = list(matrix[:,j])
    j_max = max(mid_col)
    i = mid_col.index(j_max)
    start = matrix[i,j]

    # base case:
    if start >= matrix[i,j+1] and start >= matrix[i,j-1]:
        return (start,i,j)

    # both sides are larger, choose the largest    
    if start < matrix[i,j+1] and start < matrix[i,j-1]:
        if matrix[i,j+1] > matrix[i,j-1]:
            # go right
            for i in range(j,0,-1):
                matrix = np.delete(matrix,0,1)
            return peak_finder_2d(matrix)
        else:
            # go left
            for i in range(j+1,len(matrix[0])):
                matrix = np.delete(matrix,j+1,1)
            return peak_finder_2d(matrix)

    if start < matrix[i,j+1]:
        # go right
        for i in range(j,0,-1):
            matrix = np.delete(matrix,0,1)
        return peak_finder_2d(matrix)
    else:
        # go left
        for i in range(j+1,len(matrix[0])):
            matrix = np.delete(matrix,j+1,1)
        return peak_finder_2d(matrix)

### Passes test cases where test is solved in one step and test1 is solved in 2 steps ###
# A step is counted each time peak_finder_2d() is called 

test = [[70, 82, 76, 88, 71],
 [58, 80, 53, 76, 58],
 [66, 50, 42, 67, 78],
 [84, 78, 82, 67, 97],
 [54, 91, 90, 87, 68]]
test = np.array(test)

test1 = [[21, 70, 82, 76, 88, 71, 70],
 [22, 58, 80, 53, 76, 58, 57],
 [43, 66, 50, 42, 67, 78, 77],
 [26, 84, 78, 82, 67, 97, 96],
 [13, 68, 87, 90, 91, 92, 99]]
test1 = np.array(test1)

# print(test1)
# ans = peak_finder_2d(test1)
# print(ans, "found in", num_steps, "steps")

def test_function(num_trials,m,n,to_print=False):
    solutions = {}
    for trial in range(0,num_trials):
        matrix = [ [random.randint(500,600) for j in range(0,m)] for i in range(0,n)]
        global num_steps
        num_steps = 0
        mxn = np.array(matrix)
        ans = peak_finder_2d(mxn)
        try:
            solutions[num_steps] += 1
        except KeyError:
            solutions[num_steps] = 1
    steps = list(solutions.keys())
    if to_print:
        for k in steps:
            print("Solutions found in", k, "steps is", solutions[k])

    print("Trials completed")
    return
test_function(3000,100,100,to_print=True)

# test_function(3000,100,100,to_print=True) returns:
    # Solutions found in 1 steps is 2961
    # Solutions found in 2 steps is 38
    # Solutions found in 3 steps is 1