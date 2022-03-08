


print("ASCII\tCharacter")

for i in range(256):
    ch = chr(i)
    print(i, "\t\t", ch)
    if i > 2:
        fileName = ch + '.txt'
        fileName = fileName.replace("/", "SLASHF")
        fileName = fileName.replace("\\", "SLASHB")
        print(fileName)
        fp = open(fileName, 'x')
        fp.close()