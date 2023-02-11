from Crypto.Cipher import AES
# urandom generate  random bytes
from os import  urandom

def encrypt(plaintext:bytes,key:bytes):
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}
    IV=urandom(16)
    cipher = AES.new(key, AES.MODE_CBC,IV)
    encrypted = cipher.encrypt(plaintext)
    return IV+encrypted
flag=b"here's your flag: ??????????????????????????????????????????"

key=flag[:16]
print(f"Encrypted flag: {encrypt(flag,key).hex()}")

# Encrypted flag: f2700cb3c12085660d8787764df568a4f8bb38bcfe5da7f20180c1a383de7110add1cc71afdf0f28173839c5fbd275f2b9ea77905872cb55b60bc4c9cbd8a6b6ad900ff33f6413f590e6b97add1bd3c87113743508cb0560724dc33a4ac8fbb0



