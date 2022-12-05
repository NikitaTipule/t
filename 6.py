import timeit
 
def swap2Parts(data):
    return (data << 4 | data >> 4) & 0xff
 
def leftShift(key_array):
        ans = [None] * key_size
        ans[0:9] = key_array[1:10]
        ans[4] = key_array[0]
        ans[9] = key_array[5]
        return ans

def perm(input, permTable):
    output = 0
    for i in range(len(permTable)):
        elem = permTable[i]
        if i >= elem:
            output |= (input & (128 >> (elem - 1))) >> (i - (elem - 1))
        else:
            output |= (input & (128 >> (elem - 1))) << ((elem - 1) - i)
    return output
 
def initialPermutation(data):
    return perm(data, IPtable)
 
def finalPermutation(data):
    return perm(data, FPtable)

def generateKeys(key):
    keyList = list(map(int,bin(key)[2:]))

    if(len(keyList) < key_size):
        keyList = ([0]*(key_size - len(keyList))) + keyList

    permKeyList = [None] * key_size
    for i, elem in enumerate(P10table):
        permKeyList[i] = keyList[elem - 1]
    shiftedOnceKey = leftShift(permKeyList)
    shiftedTwiceKey = leftShift(leftShift(shiftedOnceKey))
    subKey1 = subKey2 = 0
    
    for i, elem in enumerate(P8table):
        subKey1 += (128 >> i) * shiftedOnceKey[elem - 1]
        subKey2 += (128 >> i) * shiftedTwiceKey[elem - 1]
    return (subKey1, subKey2)
 
def fk(subKey, inputData):
    def F(sKey, rightNibble):
        aux = sKey ^ perm(swap2Parts(rightNibble), EPtable)
        i1 = ((aux & 0x80) >> 4) + ((aux & 0x40) >> 5) + ((aux & 0x20) >> 5) + ((aux & 0x10) >> 2)
        i2 = ((aux & 0x08) >> 0) + ((aux & 0x04) >> 1) + ((aux & 0x02) >> 1) + ((aux & 0x01) << 2)
        sboxOutputs = swap2Parts((S0table[i1] << 2) + S1table[i2])
        return perm(sboxOutputs, P4table)
 
    leftNibble, rightNibble = inputData & 0xf0, inputData & 0x0f
    return (leftNibble ^ F(subKey, rightNibble)) | rightNibble
 
def encrypt(key, plaintext):
    keys = generateKeys(key)
    text = initialPermutation(plaintext)
    text = fk(keys[0], text)
    text = swap2Parts(text)
    print("ciphertext after 1st round is:", text)
    text = fk(keys[1], text)
    print("ciphertext after 2nd round is:", text)
    text = finalPermutation(text)
    print("ciphertext after final permutation is:", text)
    return text 

def decrypt(key, ciphertext):
    keys = generateKeys(key)
    text = initialPermutation(ciphertext)
    text = fk(keys[1], text)
    text = swap2Parts(text)
    print("text after 1st round of decryption is:", text)
    text = fk(keys[0], text)
    print("text after 2nd round of decryption is:", text)
    text = finalPermutation(text)
    print("text after final permutation of decryption is:", text)
    return text 

#encrpyt without printing intermediate results
def encrypt_2(key, plaintext):
    keys = generateKeys(key)
    text = initialPermutation(plaintext)
    text = fk(keys[0], text)
    text = swap2Parts(text)
    text = fk(keys[1], text)
    text = finalPermutation(text)
    return text 
 
#decrpyt without printing intermediate results
def decrypt_2(key, ciphertext):
    keys = generateKeys(key)
    text = initialPermutation(ciphertext)
    text = fk(keys[0], text)
    text = swap2Parts(text)
    text = fk(keys[1], text)
    text = finalPermutation(text)
    return text 
 
 
key_size = 10
IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)

   
def message_length_analysis():
    plain_text_array = [0b10101010]*8
    key = 0b1111111111

    for i in range(len(plain_text_array)):
        p_text = plain_text_array[:i+1]

        initial_time = timeit.default_timer()
        c_text = []
        for block in p_text:
            c_text.append(encrypt_2(key, block))
        final_time = timeit.default_timer()
        print("message length =", 8*len(p_text), "bits")
        print("Time taken for encryption in", (final_time - initial_time) * 1000,"ms")

        initial_time = timeit.default_timer()
        p_text_2 = []
        for block in c_text:
            p_text_2.append(decrypt_2(key, block))
        final_time = timeit.default_timer()
        print("Time taken for decryption in", (final_time - initial_time) * 1000, "ms\n")

p_text = 0b11101110
key = 0b1110011100
print("plaintext =",bin(p_text)[2:],"\n")

initial_time = timeit.default_timer()
c_text = encrypt(key, p_text)
final_time = timeit.default_timer()
print("ciphertext after encryption=",bin(c_text)[2:])
print("Time taken ", (final_time - initial_time) * 1000, "ms\n")

initial_time = timeit.default_timer()
p_text_2 = decrypt(key, c_text)
final_time = timeit.default_timer()
print("plaintext after decryption=",bin(p_text_2)[2:])
print("Time taken ", (final_time - initial_time) * 1000, "ms\n")

message_length_analysis()