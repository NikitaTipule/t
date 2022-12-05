import random 
import itertools

sample_space = {
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p"
}

str = "lmnop"
str = ''.join(random.sample(str,len(str)))

sample_space["l"] = str[0]
sample_space["m"] = str[1]
sample_space["n"] = str[2]
sample_space["o"] = str[3]
sample_space["p"] = str[4]

# Function to encrypt a text using monoalphabetic cipher
def encryption_using_monoaplhabetic_cipher(plain_text):
    cipher_text = []
    for i in plain_text:
        cipher_text.append(sample_space[i])

    cipher_text = "".join(cipher_text)
    return cipher_text


# Function to find all possible output plain text
def brute_force_approch(cipher_text):
    nums = list(cipher_text)
    permutations = list(itertools.permutations(nums))
    print("\nAll Possible outputs : \n")
    print([''.join(permutation) for permutation in permutations])
    print("\n")


if __name__ == "__main__":
    print("Sample space : l, m, n, o, p")
    
    while(1):
        plain_text = input("Enter Plain Text : ")
        cipher_text = encryption_using_monoaplhabetic_cipher(plain_text)
        print("Cipher text = ", cipher_text)
        brute_force_approch(cipher_text)
        inp = input("Enter y to continue or n to exit : ")
        if(inp == "n"):
            break
        else:
            continue
