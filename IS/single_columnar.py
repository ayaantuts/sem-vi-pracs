key = 'MONEY'
def transposition_m(plain_text:str) -> list:
	plain_text = plain_text.replace(' ', '').upper()
	rows = len(plain_text) // len(key)
	if len(plain_text) % len(key) != 0:
		rows += 1
	plain_text += (rows * len(key) - len(plain_text)) * 'Z'
	columns = [''] * len(key)
	for i in range(len(key)):
		for j in range(rows):
			columns[i] += plain_text[i + j * len(key)]
	return columns

def encrypt(transposeM:list) -> str:
	cipher_text = ''
	for i in sorted(key):
		cipher_text += transposeM[key.index(i)]
	return cipher_text

def decrypt(transposeM:list) -> str:
	plain_text = ''
	for i in range(len(transposeM[0])):
		for j in range(len(key)):
			plain_text += transposeM[j][i]
	return plain_text

plain_text = 'BUY SOME MILK AND EGGS'
transposeM = transposition_m(plain_text)
print('Transpose M:', transposeM)
cipher_text = encrypt(transposeM)
print('Cipher text:', cipher_text)
plain_text = decrypt(transposeM)
print('Plain text:', plain_text)