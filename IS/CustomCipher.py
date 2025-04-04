# Create your own cipher and implement it in Python.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 1) Transposition Cipher (Simple Columnar Transposition)
def transposition_encrypt(text, key=3):
    return ''.join([text[i::key] for i in range(key)])

def transposition_decrypt(text, key=3):
    num_cols = len(text) // key
    return ''.join(text[i::num_cols] for i in range(num_cols))

# 2) Substitution Cipher (Basic Caesar Cipher Shift)
def substitution_encrypt(text, shift=3):
    return ''.join(chr((ord(char) - 65 + shift) % 26 + 65) for char in text)

def substitution_decrypt(text, shift=3):
    return ''.join(chr((ord(char) - 65 - shift) % 26 + 65) for char in text)

# 3 & 4) RSA Encryption (Asymmetric Key Encryption)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(text, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_text = cipher.encrypt(text.encode())
    return base64.b64encode(encrypted_text).decode()

def rsa_decrypt(encrypted_text, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text))
    return decrypted_text.decode()

# String to encrypt
to_encrypt = "INFORMATIONSECURITY"

# Step 1: Transposition Encryption
transposed = transposition_encrypt(to_encrypt)
# Step 2: Substitution Encryption
substituted = substitution_encrypt(transposed)
# Step 3 & 4: RSA Encryption
private_key, public_key = generate_rsa_keys()
rsa_encrypted = rsa_encrypt(substituted, public_key)

print("Encrypted Text:", rsa_encrypted)

# Decryption Process
rsa_decrypted = rsa_decrypt(rsa_encrypted, private_key)
substituted_decrypted = substitution_decrypt(rsa_decrypted)
transposed_decrypted = transposition_decrypt(substituted_decrypted)

print("Decrypted Text:", transposed_decrypted)