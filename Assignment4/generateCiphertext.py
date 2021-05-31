import re

f1=open('outputCipher.txt','r')
f2=open('cipherTexts.txt','w')
count=0
for lines in f1:
	cipher=re.findall(r'^\t\t[fghijklmnopqrstu]{16,16}\n',lines)
	if len(cipher)!=0:
		f2.write(cipher[0][2:])
		count+=1
print(f"{count} known Plaintext-Ciphertext generated Successfully ")		
