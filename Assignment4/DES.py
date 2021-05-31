S = [
[14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7,
  0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
  4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0,
  15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13 ,
],[
  15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10,
  3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
  0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15,
  13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9,
],[
  10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8,
  13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
  13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7,
  1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
],[
  7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
  13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
  10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4,
  3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,

],[
  2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
  14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
  4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
  11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,
],[
  12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11,
  10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
  9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
  4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
],[
  4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
  13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
  1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
  6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
  ],[
  13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7,
  1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
  7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
  2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

E =[32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21,
  29, 12, 28, 17,
  1, 15, 23, 26,
  5, 18, 31,10,
  2, 8, 24, 14,
  32, 27, 3, 9,
  19, 13, 30, 6,
  22, 11, 4, 25,]

INV_P=[ 9, 17, 23, 31,
	    13, 28, 2, 18,
	    24, 16, 30, 6,
	    26, 20, 10, 1,
    	8, 14, 25, 3,
	    4, 29, 11, 19,
    	32, 12, 22, 7,
    	5, 27, 15, 21    ]

RFP = [8,40,16,48,24,56,32,64,
  7, 39,15,47,23,55,31,63,
  6,38,14,46,22,54,30,62,
  5,37,13,45, 21,53,29,61,
  4,36,12,44,20,52,28,60,
  3, 35, 11,43,19,51,27,59,
  2, 34, 10, 42,18, 50,26,58,
  1,33,9,41, 17, 49, 25,57,]

IP = [
    58,50,42, 34,26,18,10,2,
  60,52,44,36,28,20,12,4,
  62,54, 46, 38, 30, 22, 14,6,
  64, 56, 48, 40,32,24, 16, 8,
  57, 49, 41, 33,25,17, 9,1,
  59, 51,43,35,27,19,11,3,
  61,53,45,37,29,21,13, 5,
  63,55, 47,39,31,23,15,7
]

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

PC1 = [57, 49, 41, 33, 25, 17, 9,
  1, 58, 50, 42, 34, 26, 18,
  10,  2, 59, 51, 43, 35, 27,
  19, 11,  3, 60, 52, 44, 36,
  63, 55, 47, 39, 31, 23, 15,
  7, 62, 54, 46, 38, 30, 22,
  14,  6, 61, 53, 45, 37, 29,
  21, 13,  5, 28, 20, 12,  4]

shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

file = open("possibleKeys.txt",'r')
plain = open("inputPlaintexts.txt","r")     ## these cipherTexts and plainTexts should be corresponding to same characteristics
cipher = open("cipherTexts.txt","r")
possKeys = file.readlines()

plainText = plain.readlines()[4][0:16]  # if level 4 progress get reset then replace [4] with [19]

cipherText = cipher.readline()[0:16]

cipherB = []
for c in cipherText:
    n = ord(c) - 102
    cipherB.append(str(bin(n)[2:].zfill(4)))

cipherB = "".join(cipherB)

plainB = []
for c in plainText:
    n = ord(c) - 102
    plainB.append(str(bin(n)[2:].zfill(4)))

plainB = "".join(plainB)
plainB = "".join([plainB[IP[i] - 1] for i in range(64)])

K = ""

# checking each possible 56 bit key
for id,key in enumerate(possKeys):

    K = key[0:56]
    key = list(key[0:56])

    L = plainB[0:32]
    R = plainB[32:]

    for r in range(6):
        #subkey = list(key)
        for sh in range(shift[r]):
            t1 = key[0]
            t2 = key[28]
            for j in range(27):
                key[j] = key[j+1]
                key[j +28] = key[j + 29]

            key[27] = t1
            key[55] = t2


        subkey = "".join([key[PC2[i]-1] for i in range(48)])

        RE = "".join([R[E[i]-1] for i in range(48)])

        sbox = int(RE,2) ^ int(subkey,2)

        sboxIn = bin(sbox)[2:].zfill(48)

        sboxOut = []

        for box in range(8):

            sbits = sboxIn[(box)*6:(box)*6+6]

            sbits = sbits[0]+sbits[5]+sbits[1:5]

            sout = S[box][int(sbits,2)]
            sboxOut.append(bin(sout)[2:].zfill(4))

        sboxOut = "".join(sboxOut)

        pOut = "".join([sboxOut[P[i]-1] for i in range(32)])

        Ltemp = L
        L = R
        R = int(Ltemp,2)^int(pOut,2)

        R = bin(R)[2:].zfill(32)

    generateCipher = L + R

    generateCipher = "".join([generateCipher[RFP[i]-1] for i in range(64)])

    '''print(generateCipher)
    print(len(generateCipher))
    print(id)'''
    if generateCipher==cipherB:
        print(K)
        break


key64 = ['X' for i in range(64)]

for i,p in enumerate(PC1):
    key64[p-1] = K[i]



finalKey = []
for g in range(8):
    temp = 0
    for t in range(8):
        if t<7:
            temp=temp^int(key64[g*8+t],2)
            finalKey.append(key64[g*8+t])
    finalKey.append(str(temp^1))

finalKey = "".join(finalKey)

print(finalKey)
print(hex(int(finalKey,2)))









