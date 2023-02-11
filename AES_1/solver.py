# solver : 
# from Crypto.Cipher import AES
# def decrypt(plaintext,key,IV):

#     cipher = AES.new(key, AES.MODE_CBC,IV)
#     encrypted = cipher.decrypt(plaintext)
#     return encrypted
# Encrypted_flag=bytes.fromhex("f2700cb3c12085660d8787764df568a4f8bb38bcfe5da7f20180c1a383de7110add1cc71afdf0f28173839c5fbd275f2b9ea77905872cb55b60bc4c9cbd8a6b6ad900ff33f6413f590e6b97add1bd3c87113743508cb0560724dc33a4ac8fbb0")

# key=b"here's your flag"
# IV=Encrypted_flag[:16]
# Encrypted_flag=Encrypted_flag[16:]
# print(decrypt(Encrypted_flag,key,IV))