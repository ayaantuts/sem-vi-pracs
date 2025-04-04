# SHA-1 from scratch
import struct
from math import sin

# SHA-1 Constants
h0, h1, h2, h3, h4 = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1_padding(message):
    original_byte_len = len(message)
    message += b'\x80'
    while (len(message) + 8) % 64 != 0:
        message += b'\x00'
    message += struct.pack('>Q', original_byte_len * 8)
    return message

def sha1(message):
    global h0, h1, h2, h3, h4
    message = sha1_padding(message)
    
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset: chunk_offset + 64]
        w = list(struct.unpack('>16I', chunk)) + [0] * 64
        for i in range(16, 80):
            w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4
        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            a, b, c, d, e = temp, a, left_rotate(b, 30), c, d
        
        h0, h1, h2, h3, h4 = [(x + y) & 0xFFFFFFFF for x, y in zip([h0, h1, h2, h3, h4], [a, b, c, d, e])]
    
    return ''.join(f'{x:08x}' for x in [h0, h1, h2, h3, h4])

# Example Usage
sha1_hash = sha1(input_text.encode())
print("SHA-1 Hash: ", sha1_hash)
