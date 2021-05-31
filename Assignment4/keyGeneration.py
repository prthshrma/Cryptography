PC2 = [
  14, 17, 11, 24,  1, 5,
  3, 28 ,15,  6, 21, 10,
  23, 19, 12,  4, 26, 8,
  16,  7, 27, 20, 13, 2,
  41, 52, 31, 37, 47, 55,
  30, 40, 51, 45, 33, 48,
  44, 49, 39, 56, 34, 53,
  46, 42, 50, 36, 29, 32
]

subKey6 = "111101111011XXXXXX000111001010011000010001111111"
key = ['X' for i in range(56)]

for i,p in enumerate(PC2):
    key[p-1] = subKey6[i]


shift = [2,2,2,2,1,1]
for s in shift:
    for i in range(s):
        t1 = key[27]
        t2 = key[55]
        for j in reversed(range(27)):
            key[j+1] = key[j]
            key[j+1+28] = key[j+28]

        key[0] = t1
        key[28] = t2


print("".join(key))

# Now, finding all 2^14 possible 56 bit keys

file = open('possibleKeys.txt', 'w')

p = 2**14

for i in range(p):
    possibleKey = []
    b = bin(i)[2:].zfill(14)
    idx=0
    for bit in key:
        if bit=='X':
            possibleKey.append(b[idx])
            idx += 1
        else:
            possibleKey.append(bit)

    k = "".join(possibleKey)
    file.write(k+"\n")
