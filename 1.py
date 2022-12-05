# Ceasar cipher Code in Python

# Function to find all possible outputs
def brute_force_attack(cipher_text):
    print("All possible outputs : \n")
    for key in range(1, 27):
        output_text = []
        for i in plain_text:
            if(ord(i) < 91):
                output_text.append(chr(((ord(i) + key - 65) % 26 + 65)))
            else:
                output_text.append(chr(((ord(i) + key - 97) % 26 + 97)))

        output_text = ''.join(output_text)
        print(output_text)


# Function to Encrypt a plain text to cipher text
def encrypt_using_ceaser_cipher(plain_text, key):
    output_text = []
    for i in plain_text:
        if(ord(i) < 91):
            output_text.append(chr(((ord(i) + key - 65) % 26 + 65)))
        else:
            output_text.append(chr(((ord(i) + key - 97) % 26 + 97)))

    output_text = ''.join(output_text)
    print("Cipher text : ", output_text)
    print("\n")
    brute_force_attack(output_text)


if __name__ == "__main__":
    plain_text = input("Enter plain text : ")
    key = int(input("Enter key/shift : "))
    encrypt_using_ceaser_cipher(plain_text, key)
