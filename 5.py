# Assignment : 5
# Name : Nikita Sopan Tipule
# MIS : 111903051

# Implement extended Euclidian algorithm to find the multiplicative inverse of n mod m. Take n and m from user.

# •Find the execution time for various values of n.
# Make the comments on the results.


t1, t2 = 0, 1

def extendedGCD(n1, n2):
    global t1, t2
 
    if (n1 == 0):
        t1 = 0
        t2 = 1
        return n2

    gcd = extendedGCD(n2 % n1, n1)
    x1 = t1
    y1 = t2

    t1 = y1 - (n2 // n1) * x1
    t2 = x1
 
    return gcd
 
 
def modInverse(n, m):
 
    g = extendedGCD(n, m)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        res = (t1 % m + m) % m
        print("multiplicative inverse is ", res)
 
 
# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the value of n : "))
    m = int(input("Enter the value of m : "))

    modInverse(n, m)

    print("\nTime complexity of this algorithm is O(log m) from time complexity analysis")
    print("but based on number of steps required in extended euclid algorithm time might vary")
 