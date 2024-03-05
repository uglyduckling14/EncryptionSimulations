from aes import encryptAES
from des import encryptDES
from des3 import encryptDES3
from rsa import encryptRSA
from numpy import random


def KB50():
    try:
        # Open the file in binary mode and read the content
        with open("50KB.txt", 'rb') as file:
            # Read the entire content of the file as bytes
            file_bytes = file.read()
            return file_bytes
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def MB1():
    try:
        # Open the file in binary mode and read the content
        with open("1MB.txt", 'rb') as file:
            # Read the entire content of the file as bytes
            file_bytes = file.read()
            return file_bytes
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def MB2():
    try:
        # Open the file in binary mode and read the content
        with open("2MB.txt", 'rb') as file:
            # Read the entire content of the file as bytes
            file_bytes = file.read()
            return file_bytes
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    aes_avg =0
    des_avg =0
    des3_avg =0
    rsa_avg =0
    print("50KB times")
    for i in range(100):
        aes_avg += encryptAES(KB50())
        des_avg += encryptDES(KB50())
        des3_avg += encryptDES3(KB50())
        rsa_avg += encryptRSA(KB50())
    print(f"{aes_avg/100} AES avg time")
    print(f"{des_avg/100} DES avg time")
    print(f"{des3_avg/100} DES3 avg time")
    print(f"{rsa_avg/100} RSA avg time")
    aes_avg =0
    des_avg =0
    des3_avg =0
    rsa_avg =0
    print("1MB times")
    for i in range(100):
        aes_avg += encryptAES(MB1())
        des_avg += encryptDES(MB1())
        des3_avg += encryptDES3(MB1())
        rsa_avg += encryptRSA(MB1())
    print(f"{aes_avg/100} AES avg time")
    print(f"{des_avg/100} DES avg time")
    print(f"{des3_avg/100} DES3 avg time")
    print(f"{rsa_avg/100} RSA avg time")
    aes_avg =0
    des_avg =0
    des3_avg =0
    rsa_avg =0
    print("2MB times")
    for i in range(100):
        aes_avg += encryptAES(MB2())
        des_avg += encryptDES(MB2())
        des3_avg += encryptDES3(MB2())
        rsa_avg += encryptRSA(MB2())
    print(f"{aes_avg/100} AES avg time")
    print(f"{des_avg/100} DES avg time")
    print(f"{des3_avg/100} DES3 avg time")
    print(f"{rsa_avg/100} RSA avg time")

    
if __name__== "__main__":
    main()
