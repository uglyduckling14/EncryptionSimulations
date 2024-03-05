from Crypto.Cipher import DES
import json
import time
from base64 import b64decode
from numpy import random
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad

def encryptDES(bytes):
    startE = time.time()
    data = bytes

    key = random.bytes(8)

    cipher = DES.new(key, DES.MODE_CBC)

    ct_bytes = cipher.encrypt(pad(data, DES.block_size))

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

        cipher = DES.new(key, DES.MODE_CBC, iv)

        pt = unpad(cipher.decrypt(ct), DES.block_size)

    except (ValueError, KeyError):

        print("Incorrect decryption")
