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

inverseRFP =   [57,49,41,33,25,17,9,1,
                59,51,43,35,27,19,11,3,
                61,53,45,37,29,21,13,5,
                63,55,47,39,31,23,15,7,
                58,50,42,34,26,18,10,2,
                60,52,44,36,28,20,12,4,
                62,54,46,38,30,22,14,6,
                64,56,48,40,32,24,16,8,]

INV_P=[ 9, 17, 23, 31,
	    13, 28, 2, 18,
	    24, 16, 30, 6,
	    26, 20, 10, 1,
    	8, 14, 25, 3,
	    4, 29, 11, 19,
    	32, 12, 22, 7,
    	5, 27, 15, 21    ]

E =[32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

file = open('cipherTexts.txt', 'r')    # these cipherTexts should be corresponding to first characteristics
texts = file.readlines()

cipherTexts = []
for s in texts:
    cipher = s[0:16]

    cipherB = []
    for c in cipher:
        n = ord(c) - 102
        cipherB.append(str(bin(n)[2:].zfill(4)))

    cipherB = "".join(cipherB)
    cipherBinary = "".join([cipherB[inverseRFP[i] - 1] for i in range(64)])
    cipherTexts.append(cipherBinary)


sboxKeys = [[],[],[],[],[],[],[],[]]
keyFrequency = {"":0}
t=0
while t<len(cipherTexts):
    cipherText1 = cipherTexts[t]
    cipherText2 = cipherTexts[t+1]

    cipherXOR = int(cipherText1,2) ^ int(cipherText2,2)

    cipherXOR = str(bin(cipherXOR)[2:].zfill(64))

    cipherXOR_right = cipherXOR[32:]
    cipherXOR_left = cipherXOR[0:32]

    SboxOutXOR = "".join([cipherXOR_right[INV_P[i] - 1] for i in range(32)])
    SboxInXOR = "".join([cipherXOR_left[E[i] - 1] for i in range(48)])

    expandcipherText2 = "".join([cipherText2[E[i] - 1] for i in range(48)])

    for box in [2,5,6,7,8]:
        sbox_in = int(SboxInXOR[(box-1)*6:(box-1)*6+6], 2)
        sbox_out = int(SboxOutXOR[(box-1)*4:(box-1)*4+4], 2)

        expandcipherBits = int(expandcipherText2[(box-1)*6:(box-1)*6+6], 2)

        for outPair1 in range(16):
            outPair2 = sbox_out ^ outPair1

            possibleInput1 = []
            possibleInput2 = []

            for i in range(64):
                if outPair1 == S[box-1][i]:
                    row = int(i/16)
                    col = i%16

                    row = str(bin(row)[2:].zfill(2))
                    col = str(bin(col)[2:].zfill(4))

                    num = row[0]+col+row[1]
                    possibleInput1.append(num)

                if outPair2 == S[box - 1][i]:
                    row = int(i / 16)
                    col = i % 16

                    row = str(bin(row)[2:].zfill(2))
                    col = str(bin(col)[2:].zfill(4))

                    num = row[0] + col + row[1]
                    possibleInput2.append(num)


            inputs = []
            for in1 in possibleInput1:
                for in2 in possibleInput2:
                    if int(in1,2)^int(in2,2) == sbox_in:
                        inputs.append(int(in1,2))



            for i in inputs:
                k = i^expandcipherBits
                sboxKeys[box-1].append(k)

    t = t + 2

#print(len(sboxKeys[1]))
#print(len(sboxKeys[4]))
#print(len(sboxKeys[5]))
#print(len(sboxKeys[6]))
#print(len(sboxKeys[7]))

freq2 = {"":0}
freq5 = {"":0}
freq6 = {"":0}
freq7 = {"":0}
freq8 = {"":0}
for k2 in sboxKeys[1]:
    k="".join([bin(k2)[2:].zfill(6)])
    if k in freq2:
        freq2[k] += 1
    else:
        freq2[k] = 1

for k2 in sboxKeys[4]:
    k="".join([bin(k2)[2:].zfill(6)])
    if k in freq5:
        freq5[k] += 1
    else:
        freq5[k] = 1

for k2 in sboxKeys[5]:
    k="".join([bin(k2)[2:].zfill(6)])
    if k in freq6:
        freq6[k] += 1
    else:
        freq6[k] = 1

for k2 in sboxKeys[6]:
    k="".join([bin(k2)[2:].zfill(6)])
    if k in freq7:
        freq7[k] += 1
    else:
        freq7[k] = 1

for k2 in sboxKeys[7]:
    k="".join([bin(k2)[2:].zfill(6)])
    if k in freq8:
        freq8[k] += 1
    else:
        freq8[k] = 1


K = list(freq2.keys())
V = list(freq2.values())

max2 = K[V.index(max(V))]
print("{}: {}".format(max2, freq2[max2]))

K = list(freq5.keys())
V = list(freq5.values())

max5 = K[V.index(max(V))]
print("{}: {}".format(max5, freq5[max5]))

K = list(freq6.keys())
V = list(freq6.values())

max6 = K[V.index(max(V))]
print("{}: {}".format(max6, freq6[max6]))

K = list(freq7.keys())
V = list(freq7.values())

max7 = K[V.index(max(V))]
print("{}: {}".format(max7, freq7[max7]))

K = list(freq8.keys())
V = list(freq8.values())

max8 = K[V.index(max(V))]
print("{}: {}".format(max8, freq8[max8]))


#print(cipherTexts)

