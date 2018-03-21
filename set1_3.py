import binascii
encoded = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

for key in range(256):
		output = ''
		for char in encoded:
				output = output + chr(ord(char) ^ key)
 		print output
