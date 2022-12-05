# Assignment : 4
# Name : Nikita Sopan Tipule
# MIS : 111903051

# Find the different values of n which have totient value Φ(n) = "m".
# m should be given by the user. 


def isPrime(n):
    if(n<=1):
        return 0

    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1


# returns list of n such that Φ(n) = m
def inverseTotient(m):
    if(m%2==1):
        return []
        
    factors_list = []
    for i in range(1,int(m**0.5)+1):
        if(m%i==0):
            factors_list.append([i,m//i])

    res=[]
    for pair in factors_list:
        if(pair[0]==1):
            if(isPrime(pair[1]+1)):
                res.append(pair[1]+1)
                res.append((pair[1]+1)*2)

        elif(isPrime(pair[0]+1) and isPrime(pair[1]+1)):
           res.append((pair[0]+1)*(pair[1]+1))
           res.append((pair[0]+1)*(pair[1]+1)*2)

    return res


m = int(input("Enter the number(m): "))    
ans = inverseTotient(m)

if(len(ans) > 0):
    ans.sort()
    print("Values of n such that Φ(n) = m are:")
    for number in ans:
        print(number)
else:
    print("No such value of n exist")