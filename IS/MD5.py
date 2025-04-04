import struct
from math import sin

# Constants for MD5
s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
K = [int(abs(2**32 * abs(sin(i + 1)))) for i in range(64)]
init_vals = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def left_rotate(x, c):
    return (x << c) | (x >> (32 - c))

def md5_padding(message):
    original_byte_len = len(message)
    message += b'\x80'
    while (len(message) + 8) % 64 != 0:
        message += b'\x00'
    message += struct.pack('<Q', original_byte_len * 8)
    return message

def md5(message):
    message = md5_padding(message)
    a, b, c, d = init_vals
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset: chunk_offset + 64]
        M = list(struct.unpack('<16I', chunk))
        A, B, C, D = a, b, c, d
        for i in range(64):
            if i < 16:
                f = (B & C) | (~B & D)
                g = i
            elif i < 32:
                f = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                f = C ^ (B | ~D)
                g = (7 * i) % 16
            f = (f + A + K[i] + M[g]) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + left_rotate(f, s[i])) & 0xFFFFFFFF
        a, b, c, d = [(v + nv) & 0xFFFFFFFF for v, nv in zip([a, b, c, d], [A, B, C, D])]
    return ''.join(f'{x:08x}' for x in [a, b, c, d])

# Example Usage
input_text = "INFORMATIONSECURITY"
md5_hash = md5(input_text.encode())
print("MD5 Hash: ", md5_hash)