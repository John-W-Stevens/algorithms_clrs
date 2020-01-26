# From Introduction to Algorithms by Corman, et al. pages 937-938

def extended_euclid(a,b):
    """ From Introduction to Algorithms by Corman, et al. pages 937-938:
    "Returns integer coefficients x and y such that
    d = gcd(a,b) = ax + by
    Note that x and y may be zero or negative. These coefficients
    are useful for computing modual multiplicative inverses.
    Takes as input a pair of nonnegative integers and returns
    a triple of form (d,x,y) that satisfies the above equation" 
    
    Running time: O(log b)
    For a > b > 0, the number of recursive calls is O(log b) """
    
    if b == 0:
        return (a,1,0)
    else:
        d1,x1,y1 = extended_euclid(b, a % b)
        d,x,y = (d1,y1,x1 - a//b * y1)
    return (d,x,y)

# Test case
print(extended_euclid(19,23))

