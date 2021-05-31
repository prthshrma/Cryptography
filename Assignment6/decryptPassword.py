
#hardcoded root which is calculated in smallExpRSA.py
root=4773930458381642785

bin_root = "0" + bin(root)[2:]

password=""

for i in range( 0, len(bin_root), 8):
   password += chr( int( bin_root[i:i+8] , 2) )

print("Final Password is ",password)
