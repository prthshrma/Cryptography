import random

inverseIP = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9, 49, 17, 57, 25 ]


file = open("inputPlaintexts.txt", "w")

#xor = "4008000004000000"    # change characteristics accordingly
xor = "0020000800000400"
scale = 16

xorBinary = bin(int(xor,scale))[2:].zfill(64)


'''characters = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
plainText1 = []
for i in range(16):
    plainText1.append(random.choice(characters))

plainText1 = "".join(s for s in plainText1)
print(plainText1)'''

string = "cryptoEngineers"
file.write("{}\n".format(string))
file.write("{}\n".format(string))
file.write("{}\n".format("4"))
file.write("{}\n".format("read"))
# on entering read command, if not reaching to magical screen (i.e. level 4 progress get reset)
# then un-comment below lines (i.e. we have to enter these commands again)
'''
file.write("{}\n".format("go"))
file.write("{}\n".format("dive"))
file.write("{}\n".format("dive"))
file.write("{}\n".format("back"))
file.write("{}\n".format("pull"))
file.write("{}\n".format("back"))
file.write("{}\n".format("back"))
file.write("{}\n".format("enter"))
file.write("{}\n".format("wave"))
file.write("{}\n".format("back"))
file.write("{}\n".format("back"))
file.write("{}\n".format("thrnxxtzy"))
file.write("{}\n".format("read"))
file.write("{}\n".format("3608528850368400786036725"))
file.write("{}\n".format("c"))
file.write("{}\n".format("read"))
'''

for n in range(1000):
    plain1Array = []
    for i in range(64):
        plain1Array.append(random.randint(0,1))


    plain1Binarybefore = "".join(str(s) for s in plain1Array)

    plain2Binary = int(plain1Binarybefore,2) ^ int(xorBinary,2)

    plain2Binarybefore = str(bin(plain2Binary)[2:].zfill(64))


    plain1Binary = "".join([plain1Binarybefore[inverseIP[i] - 1] for i in range(64)])
    plain2Binary = "".join([plain2Binarybefore[inverseIP[i] - 1] for i in range(64)])

    plainText1 = []
    plainText2 = []

    i=0
    while i < 64:
        character1 = plain1Binary[i:i+4]
        character2 = plain2Binary[i:i+4]

        character1 = int(character1, 2)
        character2 = int(character2, 2)

        plainText1.append(chr(102+character1))
        plainText2.append(chr(102+character2))

        i = i+4

    plainText1 = "".join(s for s in plainText1)
    plainText2 = "".join(s for s in plainText2)

    file.write("{}\n".format(plainText1))
    file.write("{}\n".format("c"))
    file.write("{}\n".format(plainText2))
    file.write("{}\n".format("c"))

file.write("{}\n".format("back"))
file.write("{}\n".format("exit"))

'''print(plain1Binary)
    print(plainText1)
    print(plain2Binary)
    print(plainText2)
    print(type(plain2Binary))'''