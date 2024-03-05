from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time
from base64 import b64encode
from Crypto.Cipher import AES
import json
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
from numpy import random

def encryptRSA(bytes):
    startE = time.time()
    data = bytes

    key = random.bytes(16)
    encrypt_key = RSA.generate(1024)
    encryptedKey = PKCS1_OAEP.new(encrypt_key.public_key()).encrypt(key)

    cipher = AES.new(key, AES.MODE_CBC)

    ct_bytes = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')

    ct = b64encode(ct_bytes).decode('utf-8')

    result = json.dumps({'iv':iv, 'ciphertext':ct})

    decrypt(encryptedKey, result, encrypt_key)
    return (time.time()-startE)* 1000

def decrypt(encryptedKey, json_input, encrypt_key):
    try:

        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])

        ct = b64decode(b64['ciphertext'])

        cipher_rsa = PKCS1_OAEP.new(encrypt_key)
        key = cipher_rsa.decrypt(encryptedKey)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        pt = unpad(cipher.decrypt(ct), AES.block_size)

        ##print("The message was: ", pt)

    except (ValueError, KeyError):

        print("Incorrect decryption")