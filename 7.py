import math
import timeit


# 1)check whether the given number is prime or not?
def isPrime(number):
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


#2)find GCD (Greatest Common Divisor) of given two numbers.
def Findgcd(a,b):
	if(b == 0):
		return a
	else:
		return Findgcd(b, a % b)


# 3)check whether given numbers are relatively prime or not?
def isRelativelyPrime(a, b):
    if(Findgcd(a, b) == 1):
        print("Numbers are relatively Prime")
    else:
        print("Numbers are not relatively Prime")


# 4)find multiplicative inverse of given two numbers
def multiplicativeInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1


# return totient for two prime numbers
def totient(p, q):
	return (p-1)*(q-1)


# e = encryption key
# m = totient function
def decryption_key(e, m):
	return multiplicativeInverse(e,m)
 
# performs encrytion on text
def encrypt_text(text, e, n):
    cipher_text = []
    for letter in str(text):
        letter = int(float(letter.strip()))
        c = pow(letter, e) % n
        cipher_text.append(str(c))
    return cipher_text

def eValue(t):
    for k in range(2,t): 
        if Findgcd(k,t)== 1: 
            return k


# perorms decryption on entered text
def decrypt_text(text, d, n):
    decrypted_text = ""
    for letter in text:
        letter = int(float(letter.strip()))
        p = pow(letter, d) % n
        decrypted_text += str(p)
    return decrypted_text


def RSA():
    p = int(input("Enter value of p : "))
    q = int(input("Enter value of q : "))
    e = int(input("Enter the value of e : "))
    text = input("Enter text : ")
    n = p*q
    m = totient(p, q)
    d = decryption_key(e, m)

    start = timeit.default_timer()
    cipher_text = encrypt_text(text, e, n)
    deciphered_text = decrypt_text(cipher_text, d, n)
    end = timeit.default_timer()
    print(f"e = {e} and d= {d}")
    print("Cipher text = ", "".join(cipher_text))
    print("Deciphered text = ", deciphered_text)
    print("Time Requied: ", (end - start))


if __name__ == "__main__":
    n = 0
    while(1):
        print("1. Check where number is prime or not\n")
        print("2. Calculate GCD of two numbers \n")
        print("3. Check whether given numbers are relatively prime or not\n")
        print("4. Calculate multiplicative inverse of given two numbers \n")
        print("5. RSA algorithm for encryption and decryption \n")
        print("6. Quit\n\n")
        n = int(input("Enter number : "))
        if(n == 1):
            num = int(input("Enter number to check if it is prime or not : "))
            isPrime(num)
        elif(n == 2):
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            gcd = Findgcd(n1, n2)
            print("GCD of given two numbers is ", gcd)
        elif(n == 3):
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            isRelativelyPrime(n1, n2)
        elif(n == 4):
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            print("Multiplicative inverse of two numbers is : ", multiplicativeInverse(n1, n2))
        elif(n == 5):
            RSA()
        elif(n == 6):
            break
        else:
            continue