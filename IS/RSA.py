# Implementation of RSA algorithm
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def modinv(a, m):
	m0, x0, x1 = m, 0, 1
	while a > 1:
		q = a // m
		m, a = a % m, m
		x0, x1 = x1 - q * x0, x0
	return x1 + m0 if x1 < 0 else x1

def encrypt(m, e, n):
	return pow(m, e, n)

def decrypt(c, d, n):
	return pow(c, d, n)

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)
for e in range(2, phi):
	if gcd(e, phi) == 1:
		break
d = modinv(e, phi)
m = int(input("Enter message: "))
c = encrypt(m, e, n)
print("Encrypted message:", c)
print("Decrypted message:", decrypt(c, d, n))
