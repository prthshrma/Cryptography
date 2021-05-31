file = open("inputPlaintexts.txt", "w")
file2 = open("plainTexts.txt", "w")

string = "cryptoEngineers"
file.write("{}\n".format(string))
file.write("{}\n".format(string))
file.write("{}\n".format("5"))
file.write("{}\n".format("go"))
file.write("{}\n".format("wave"))
file.write("{}\n".format("dive"))
file.write("{}\n".format("go"))
file.write("{}\n".format("read"))

for i in range(1,128):
    for j in range(8):
        b = bin(i)[2:].zfill(8)
        b1 = b[0:4]
        b2 = b[4:]
        c1 = chr(int(b1,2) + 102)
        c2 = chr(int(b2,2) + 102)

        text=""

        if(j==0):
            text = c1+c2+"ffffffffffffff"
        if (j == 1):
            text = "ff" + c1 + c2 + "ffffffffffff"
        if (j == 2):
            text = "ffff" + c1 + c2 + "ffffffffff"
        if (j == 3):
            text = "ffffff" + c1 + c2 + "ffffffff"
        if (j == 4):
            text = "ffffffff" + c1 + c2 + "ffffff"
        if (j == 5):
            text = "ffffffffff" + c1 + c2 + "ffff"
        if (j == 6):
            text = "ffffffffffff" + c1 + c2 + "ff"
        if (j == 7):
            text = "ffffffffffffff" + c1 + c2

        file.write("{}\n".format(text))
        file.write("{}\n".format("c"))

        file2.write("{}\n".format(text))

file.write("{}\n".format("back"))
file.write("{}\n".format("exit"))