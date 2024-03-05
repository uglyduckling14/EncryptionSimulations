from Crypto.Cipher import AES
import json
import time
from base64 import b64encode

from Crypto.Util.Padding import pad, unpad

from base64 import b64decode
from numpy import random

def encryptAES(bytes):
    startE = time.time()
    data = bytes

    key = random.bytes(16)

    cipher = AES.new(key, AES.MODE_CBC)

    ct_bytes = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')

    ct = b64encode(ct_bytes).decode('utf-8')

    result = json.dumps({'iv':iv, 'ciphertext':ct})

    decrypt(key, result)
    return (time.time()-startE)* 1000

def decrypt(key, json_input):
    try:

        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])

        ct = b64decode(b64['ciphertext'])

        cipher = AES.new(key, AES.MODE_CBC, iv)

        pt = unpad(cipher.decrypt(ct), AES.block_size)

        ##print("The message was: ", pt)

    except (ValueError, KeyError):

        print("Incorrect decryption")