def key_generation(plaintext,key):
    for i in range(len(plaintext)-len(key)):
        key+=key[i]
    return key

def vignere(plaintext,key):
    encrypttext=[]
    for i in range(len(plaintext)):
        x=(ord(plaintext[i])+ord(key[i]))%26
        x+=ord('A')
        encrypttext.append(chr(x))
    return (''.join(encrypttext))

message=input("Enter message: ")
key=input("Enter key: ")
key_new=key_generation(message,key)
print(vignere(message,key_new))