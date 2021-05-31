import copy

from pyfinite import ffield
F = ffield.FField(7)

def charToInt(p):
    N = []
    for j in range(0, 16, 2):
        b1 = bin(ord(p[j]) - 102)[2:].zfill(4)
        b2 = bin(ord(p[j + 1]) - 102)[2:].zfill(4)

        B = int(b1 + b2, 2)
        N.append(B)

    return N

# Calculating Exponent
def Exp(b,e):
    ans = 1
    for i in range(e):
        ans = F.Multiply(ans,b)
    return ans

A = [[84, 0, 0, 0, 0, 0, 0, 0],
    [112, 70, 0, 0, 0, 0, 0, 0],
    [26, 26, 43, 0, 0, 0, 0, 0],
    [99, 27, 0, 12, 0, 0, 0, 0],
    [100, 63, 1, 112, 112, 0, 0, 0],
    [19, 45, 28, 51, 96, 11, 0, 0],
    [11, 123, 0, 99, 28, 83, 27, 0],
    [64, 8, 75, 27, 18, 72, 1, 38]]

E = [22, 106, 42, 74, 87, 44, 25, 27]


# calculating EAEAE transformation
def EAEAEcrypt(tempA,tempE,tempN):

    for i in range(8):
        tempN[i] = Exp(tempN[i],E[i])

    temp = [0]*8

    for i in range(8):
        for j in range(8):
            temp[i] = temp[i] ^ F.Multiply(tempA[i][j],tempN[j])

    tempN = temp
    for i in range(8):
        tempN[i] = Exp(tempN[i], E[i])

    temp = [0] * 8

    for i in range(8):
        for j in range(8):
            temp[i] = temp[i] ^ F.Multiply(tempA[i][j], tempN[j])

    tempN = temp
    for i in range(8):
        tempN[i] = Exp(tempN[i], E[i])

    return tempN


password = "gsmpmhfkmphtlrfuhlmogsirfpgojshk"

# dividing into 2 halves
pass1 = password[0:16]
pass2 = password[16:]

c1 = pass1
C1 = []
C1 = charToInt(c1)

possibleInput = [0]*8
plain1 = [0]*8
for i in range(8):
    possibleInput = copy.deepcopy(plain1)
    for j in range(128):
        possibleInput[i] = j

        tempInput = copy.deepcopy(possibleInput)
        output = EAEAEcrypt(A,E,tempInput)

        if output[i] == C1[i]:
            plain1[i]=j
            break


c2 = pass2
C2 = []
C2 = charToInt(c2)

possibleInput = [0]*8
plain2 = [0]*8
for i in range(8):
    possibleInput = copy.deepcopy(plain2)
    for j in range(128):
        possibleInput[i] = j

        tempInput = copy.deepcopy(possibleInput)
        output = EAEAEcrypt(A,E,tempInput)

        if output[i] == C2[i]:
            plain2[i]=j
            break

#print(plain1)
#print(plain2)

finalPassword = ""

for n in plain1:
    finalPassword += chr(n)

for n in plain2:
    finalPassword += chr(n)

print("Decrypted Password : ",finalPassword)





