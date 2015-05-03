def perevod(numSym, i, x, y, cut):
    newX = x + 4247
    newY = y + 5991
    print ("Alp[" + str(numSym) + "].x[" + str(i) +"] = " + str(newX) + "; Alp[" + str(numSym) + "].y[" + str(i) +"] = " \
           + str(newY) + "; Alp[" + str(numSym) + "].cut[" + str(i) +"] = " + str(cut) + ";")

def fileTranslate(num):
    f = open('alphabet.plt', 'r')
    i = 0
    for line in f:
        if(line[0:2] == "PU"):
            perevod(num, i, int(line[2:7]), int(line[8:13]), 0)
            i += 1
        elif(line[0:2] == "PD"):
            perevod(num, i, int(line[2:7]), int(line[8:13]), 1)
            i += 1
