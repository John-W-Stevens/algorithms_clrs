
def karatsuba(a,b):
    a,b = f"{a}",f"{b}"

    # base case
    if len(a) == 1 and len(b) == 1: return int(a) * int(b)
    
    while len(a) < len(b): a = "0" + a
    while len(b) < len(a): b = "0" + b
    
    n, i = len(a), len(a)//2
    if (n % 2) != 0: i += 1

    a, b, c, d = int(a[:i]), int(a[i:]), int(b[:i]), int(b[i:])
    ac, bd, k = karatsuba(a,c), karatsuba(b,d), karatsuba(a+b,c+d)

    A = int(f"{ac}" + "".join(["0" for m in range((n-i)*2)]))
    B = int(f"{k-ac-bd}" + "".join(["0" for n in range(n-i)]))
    
    return A + B + bd

## Test case:
print(karatsuba(6798388973894729874762487625,242342342342338)) # Output: 1647537508087972583852481980654958238567250
print(6798388973894729874762487625 * 242342342342338)          # Output: 1647537508087972583852481980654958238567250