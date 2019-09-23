#! /usr/bin/env python3

from Crypto.Cipher import AES

plaintext = 'Verschluesselung'.encode("latin_1")
ciphertext = bytes.fromhex('be393d39ca4e18f41fa9d88a9d47a574')

def encrypt(key, plain_text):
    cryptor = AES.new(key, AES.MODE_ECB)
    return cryptor.encrypt(plain_text),key

def decrypt(key, cipher_text):
    cryptor = AES.new(key, AES.MODE_ECB)
    return cryptor.decrypt(cipher_text),key

byts = [0] * 16
keys = []
print("generating keys... this may take a minute...")
for q in range(16):
    for e in range(q,16):
        for w in range(256):
            for r in range(256):
                byts[q] = w
                byts[e] = r
                keystr = ""
                for c in byts:
                    keystr += chr(c)
                keys.append(keystr.encode("latin_1"))
                byts = [0] * 16
print("performing meet-in-the-middle attack...")
enc = dict(encrypt(key, plaintext) for key in keys)
for key in keys:
    dec = decrypt(key, ciphertext)
    if dec[0] in enc:
        print("Keys found!")
        print("Key 1: " + str(enc[dec[0]]))
        print("Key 2: " + str(dec[1]))
        exit()
print("No keys found!")

'''
key1 = b'\x00\x00\x00\xf5\x00\x00\x00\x00\x00\x00\x63\x00\x00\x00\x00\x00'
key2 = b'\x00\x00\x00\x00\x77\x00\x00\x00\xb0\x00\x00\x00\x00\x00\x00\x00'
print(decrypt(key1,decrypt(key2,ciphertext)[0])[0])
'''
