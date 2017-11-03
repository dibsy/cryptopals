a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
encoded = '746865206b696420646f6e277420706c6179'
output = ''

c=zip(a,b)

for i,j in c:
	 output=output+(hex(int(i,16)^int(j,16)))

output = output.replace('0x','')
print output == encoded
