from Crypto.Cipher import AES
def encrypt(text:bytes,key:bytes):
    if len(text) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(text)
    return encrypted
key=b"key are free tdy"

flag=open("flag.txt","rb").read()
len(flag)%16

def decrypt(text:bytes,key:bytes):

    cipher = AES.new(key, AES.MODE_ECB)
    text = cipher.decrypt(text)
    return text
key=b"key are free tdy"
print(f'Encrypted FLAG: {encrypt(flag,key).hex()}')

#Encrypted FLAG: 60bf48f2e31a43518436ceeec28befc059ca21b20418fcdff508d93c33ad9a1f2ef2d8e098e3310d43713bb5eb9705efb71abf4c9ccaf0d0800f67a292a816f9



