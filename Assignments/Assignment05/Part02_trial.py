import string
import random

def encrypt(encrypt_key, plaintext):
    ciphertext = ""
    for ch in plaintext:
        if ch in string.ascii_letters:
            ciphertext+=encrypt_key[ch]
        else:
            ciphertext+=ch
    return ciphertext

def decrypt(decrypt_key, ciphertext):
    plaintext = ""
    for ch in ciphertext:
        if ch in string.ascii_letters:
            plaintext+=decrypt_key[ch]
        else:
            plaintext+=ch
    return plaintext

def generate_keys():
    chars = string.ascii_letters
    codes = random.sample(chars,len(chars))
    decrypt_key = dict(zip(codes,chars))
    encrypt_key = dict(zip(chars,codes))
    return decrypt_key, encrypt_key

def print_instructions():
    print("This program encrypts and decrypts files using a word scramble cipher")
    print("  Usage:")
    print("    To get help:")
    print("         python crypt.py -h")
    print("    To create a key file:")
    print("         python crypt.py -c filename")
    print("    To encrypt a file:")
    print("         python crypt.py -e keyfile inputfile outputfile")
    print("    To decrypt a file:")
    print("         python crypt.py -d keyfile inputfile outputfile")
def print_error():
    print("ERROR: Invalid command line arguments!")


import sys
import json

if len(sys.argv)==2 and sys.argv[1]=='-h': # if only two arguments this can only be help, so if we don't have -h then we have incorrect input
    print_instructions()
elif len(sys.argv)==3 and sys.argv[1]=='-c': # if there are 3 args, this can only be create new key file, if we don't have -c we have incorrect input
    print("creating keyfile " + sys.argv[2]) # replace this and insert create keyfile code here
    encrypt_key, decrypt_key = generate_keys()
    with open(sys.argv[2], "w") as fout:
        json.dump({"encrypt_key":encrypt_key, "decrypt_key":decrypt_key}, fout)
elif len(sys.argv)==5 and sys.argv[1]=='-e': # if there are 5 args, this can only be encrypt or decrypt -- with "-e" argument, it's encrypt
    print("Encrypting inputfile",sys.argv[3],"to output file", sys.argv[4], "using key file", sys.argv[2])
    # read key from key file
    with open(sys.argv[2], "r") as fkey:
        keys =json.load(fkey)
        encrypt_key = keys["encrypt_key"]
        decrypt_key = keys["decrypt_key"]
    # read the file that will be encrypted
    with open(sys.argv[3], "r") as fin:
        plain_text = fin.read()
    # encrypt the data from the input file
    cipher_text = encrypt(encrypt_key, plain_text)
    # store the encrypted data into the output file
    with open(sys.argv[4], "w") as fout:
        fout.write(cipher_text)
elif len(sys.argv)==5 and sys.argv[1]=='-d': # if there are 3 args, this can only be create new key file, if we don't have -c we have incorrect input
    print("Decrypting inputfile",sys.argv[3],"to output file", sys.argv[4], "using key file", sys.argv[2])
    # read key from key file
    with open(sys.argv[2], "r") as fkey:
        keys =json.load(fkey)
        encrypt_key = keys["encrypt_key"]
        decrypt_key = keys["decrypt_key"]
    # read the file that will be decrypted
    with open(sys.argv[3], "r") as fin:
        cipher_text = fin.read()
    # decrypt the data from the input file
    plain_text = decrypt(decrypt_key, cipher_text)
    # store the decrypted data into the output file
    with open(sys.argv[4], "w") as fout:
        fout.write(plain_text)
else:
    print_error()
    print_instructions()