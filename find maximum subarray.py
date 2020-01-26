
# Import numpy to use Inf
from numpy import Inf

def find_max_crossing_subarray(arr,low,mid,high):
    """ From CLRS pgs. 70-74
    "Takes as input an array and indices low,mid,high
    Returns a tuple containing the indicies demarcating
    a maximum sub-array that crosses the midpoint, along with
    the sum of the values in a maximum sub-array." 
    Running time: linear """
    
    # Look at the left   
    left_sum = -Inf
    sm = 0 # sm for sum
    for i in range(mid,low-1,-1):
        sm += arr[i]
        if sm >= left_sum:
            left_sum = sm
            max_left = i
    
    # Look at the right
    right_sum = -Inf
    sm = 0
    for j in range(mid+1,high+1):
        sm += arr[j]
        if sm >= right_sum:
            right_sum = sm
            max_right = j

    return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(arr,low,high):
    """ From CLSR pgs. 70-74
    Input is an array, arr. low and high are index positions in arr that function as bounds for searching.
    Returns a tuple containing indicies for maximum sub-array along with the sum of sub-array.
    Running time: theta(n lg n) where 'lg n' stands for log2n """
    
    # Base case
    if high == low:
        return (low,high,arr[low])
    
    else:
        # find middle point of array
        mid = (low + high)//2

        # find a max sub-array in left sub-array
        left_low,left_high,left_sum = find_maximum_subarray(arr,low,mid)

        # find a max sub-array in right sub-array
        right_low,right_high,right_sum = find_maximum_subarray(arr,mid+1,high)

        # find a max sub-array that crosses the mid-point
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(arr,low,mid,high)

    # test if left sub-array contains a sub-array with the maximum sum
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low,left_high,left_sum)

    # test if right sub-array contains a sub-array with the maximum sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low,right_high,right_sum)

    # if neither left nor right sub-arrays contain a sub-array with the maximum sum,
    # then a maximum sub-array must cross the mid-point
    else:
        return (cross_low,cross_high,cross_sum)

test = [17, -25, 6, 18, -23, 8, 28, 6, 34, 31, -50, 3, 46, -33, -45, -26, 14, -23, 45, -24, 21, -31, 19, -41, 49, 
47, 29, -11, 16, 12, -9, -14, 26, -46, -11, 39, -41, -13, -11, 8, -19, -13, -9, -25, -15, 27, 30, 8, 10]

print(find_maximum_subarray(test,0,len(test)-1))
# Output: (24, 32, 145) the maximum subarray exists at test[24:33] and the sum of this subarray is 145