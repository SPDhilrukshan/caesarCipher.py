# File: CaeserCipher.py

text = str(input("please enter the text you want to cipher"))
ctext=""
alphabet="abcdefghijklmnopqrstuvwxyz"
key=3

for L in text:
	if L in alphabet:
		ctext += alphabet[(alphabet.index(L) + key)%26]
	else:
		ctext += L

print("your ciphered text is :" + ctext)

