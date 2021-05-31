import copy
import numpy as np
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

# calculating EAEAE encrypted value
def EAEAEcrypt(tempA,tempE,tempN):

    for i in range(8):
        tempN[i] = Exp(tempN[i], E[i])

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



inputFile = open('plainTexts.txt', 'r')
cipherFile = open('cipherTexts.txt','r')
pTexts = inputFile.readlines()
cTexts = cipherFile.readlines()

pairs = [[],[],[],[],[],[],[],[]]

# generating possible pairs of e and a(diagonal elements) for every byte value
for i in range(8):
    p = pTexts[i]
    N = []
    N = charToInt(p)
    #print(N)

    c = cTexts[i]
    C = []
    C = charToInt(c)
    #print(C)

    for e in range(1,127):
        for a in range(1,128):

            n = Exp(N[i],e)
            n = F.Multiply(n,a)
            n = Exp(n,e)
            n = F.Multiply(n,a)
            n = Exp(n,e)

            if n==C[i]:
                #print("yes")
                P = []
                P.append(e)
                P.append(a)
                pairs[i].append(P)

for i in range(8,96):
    p = pTexts[i]
    id = i % 8
    N = []
    N = charToInt(p)
    # print(N)

    c = cTexts[i]
    C = []
    C = charToInt(c)
    # print(C)

    newPair= []

    for e,a in pairs[id]:
        n = Exp(N[id],e)
        n = F.Multiply(n, a)
        n = Exp(n,e)
        n = F.Multiply(n, a)
        n = Exp(n,e)

        if n == C[id]:
            P = []
            P.append(e)
            P.append(a)
            newPair.append(P)

    pairs[id].clear()
    pairs[id] = newPair

# three pairs of e and a for each byte get generated
#print(pairs)

final1 = []
aii = [0]*7

for i in range(7):
    for e1,a1 in pairs[i]:
        for e2,a2 in pairs[i+1]:
            for a_ii in range(1,128):
                f=0
                for traverse in range(127):
                    p1 = pTexts[traverse*8+i]
                    N1 = []
                    N1 = charToInt(p1)

                    c1 = cTexts[traverse*8+i]
                    C1 = []
                    C1 = charToInt(c1)

                    n = Exp(N1[i],e1)

                    A1 = F.Multiply(n, a1)
                    A_1 = F.Multiply(n, a_ii)

                    E1 = Exp(A1,e1)
                    E_1 = Exp(A_1,e2)

                    A2 = F.Multiply(E1, a1)
                    A_2 = F.Multiply(E1, a_ii) ^ F.Multiply(E_1, a2)

                    E2 = Exp(A2,e1)
                    E_2 = Exp(A_2,e2)

                    if E_2 != C1[i + 1]:
                        f=1
                        break

                if f==0:
                    pairs[i].clear()
                    pairs[i+1].clear()
                    pairs[i].append([e1,a1])
                    pairs[i+1].append([e2,a2])
                    aii[i]=a_ii

# got the diagonal elements of A and elements of E

A = [[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
E = [0,0,0,0,0,0,0,0]

for id,p in enumerate(pairs):
    E[id] = p[0][0]
    A[id][id] = p[0][1]
    if id>0:
        A[id][id-1] = aii[id-1]

tempA = [[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]

# finding non diagonal elements of A
for rep in range(6):
    i = rep+2
    k = 0
    tempA = copy.deepcopy(A)
    while i<8:
        for a_ii in range(1, 128):
            f = 0

            for traverse in range(127):
                p1 = pTexts[traverse * 8 + k]
                N1 = []
                N1 = charToInt(p1)

                c1 = cTexts[traverse * 8 + k]
                C1 = []
                C1 = charToInt(c1)

                tempA[i][k] = a_ii
                N = EAEAEcrypt(tempA,E,N1)

                if N[i] != C1[i]:
                    f = 1
                    break

            if f == 0:
                A[i][k] = a_ii

        i+=1
        k+=1


print("A = ")
for a in A:
    print(a,"\n")

print("E = ")
print(E)


