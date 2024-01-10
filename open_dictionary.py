# Our dictionary is organized like a paper dictionary. Each word is exclusively contained in 
# a list composed of words which share the same first letter.

# --- WORD LISTS --- #
# A
with open("Word lists in csv\Aword.csv", "r") as aWords:
    aWordsList = [line.rstrip() for line in aWords]
    aWords.close()
# B
with open("Word lists in csv\Bword.csv", "r") as bWords:
    bWordsList = [line.rstrip() for line in bWords]
    bWords.close()
# C
with open("Word lists in csv\Cword.csv", "r") as cWords:
    cWordsList = [line.rstrip() for line in cWords]
    cWords.close()
# D
with open("Word lists in csv\Dword.csv", "r") as dWords:
    dWordsList = [line.rstrip() for line in dWords]
    dWords.close()
# E
with open("Word lists in csv\Eword.csv", "r") as eWords:
    eWordsList = [line.rstrip() for line in eWords]
    eWords.close()
# F
with open("Word lists in csv\Fword.csv", "r") as fWords:
    fWordsList = [line.rstrip() for line in fWords]
    fWords.close()
# G
with open("Word lists in csv\Gword.csv", "r") as gWords:
    gWordsList = [line.rstrip() for line in gWords]
    gWords.close()
# H
with open("Word lists in csv\Hword.csv", "r") as hWords:
    hWordsList = [line.rstrip() for line in hWords]
    hWords.close()
# I
with open("Word lists in csv\Iword.csv", "r") as iWords:
    iWordsList = [line.rstrip() for line in iWords]
    iWords.close()
# J
with open("Word lists in csv\Jword.csv", "r") as jWords:
    jWordsList = [line.rstrip() for line in jWords]
    jWords.close()
# K
with open("Word lists in csv\Kword.csv", "r") as kWords:
    kWordsList = [line.rstrip() for line in kWords]
    kWords.close()
# L
with open("Word lists in csv\Lword.csv", "r") as lWords:
    lWordsList = [line.rstrip() for line in lWords]
    lWords.close()
# M
with open("Word lists in csv\Mword.csv", "r") as mWords:
    mWordsList = [line.rstrip() for line in mWords]
    mWords.close()
# N
with open("Word lists in csv\\Nword.csv", "r") as nWords:
    nWordsList = [line.rstrip() for line in nWords]
    nWords.close()
# O
with open("Word lists in csv\Oword.csv", "r") as oWords:
    oWordsList = [line.rstrip() for line in oWords]
    oWords.close()
# P
with open("Word lists in csv\Pword.csv", "r") as pWords:
    pWordsList = [line.rstrip() for line in pWords]
    pWords.close()
# Q
with open("Word lists in csv\Qword.csv", "r") as qWords:
    qWordsList = [line.rstrip() for line in qWords]
    qWords.close()
# R
with open("Word lists in csv\Rword.csv", "r") as rWords:
    rWordsList = [line.rstrip() for line in rWords]
    rWords.close()
# S
with open("Word lists in csv\Sword.csv", "r") as sWords:
    sWordsList = [line.rstrip() for line in sWords]
    sWords.close()
# T
with open("Word lists in csv\Tword.csv", "r") as tWords:
    tWordsList = [line.rstrip() for line in tWords]
    tWords.close()
# U
with open("Word lists in csv\\Uword.csv", "r") as uWords:
    uWordsList = [line.rstrip() for line in uWords]
    uWords.close()
# V
with open("Word lists in csv\Vword.csv", "r") as vWords:
    vWordsList = [line.rstrip() for line in vWords]
    vWords.close()
# W
with open("Word lists in csv\Wword.csv", "r") as wWords:
    wWordsList = [line.rstrip() for line in wWords]
    wWords.close()
# X
with open("Word lists in csv\Xword.csv", "r") as xWords:
    xWordsList = [line.rstrip() for line in xWords]
    xWords.close()
# Y
with open("Word lists in csv\Yword.csv", "r") as yWords:
    yWordsList = [line.rstrip() for line in yWords]
    yWords.close()
# Z
with open("Word lists in csv\Zword.csv", "r") as zWords:
    zWordsList = [line.rstrip() for line in zWords]
    zWords.close()


# --- LIST RETRIEVAL HELPER --- #

def find_wordslist(char):
    if char == "a":
        return aWordsList
    elif char == "b":
        return bWordsList
    elif char == "c":
        return cWordsList
    elif char == "d":
        return dWordsList
    elif char == "e":
        return eWordsList
    elif char == "f":
        return fWordsList
    elif char == "g":
        return gWordsList
    elif char == "h":
        return hWordsList
    elif char == "i":
        return iWordsList
    elif char == "j":
        return jWordsList
    elif char == "k":
        return kWordsList
    elif char == "l":
        return lWordsList
    elif char == "m":
        return mWordsList
    elif char == "n":
        return nWordsList
    elif char == "o":
        return oWordsList
    elif char == "p":
        return pWordsList
    elif char == "q":
        return qWordsList
    elif char == "r":
        return rWordsList
    elif char == "s":
        return sWordsList
    elif char == "t":
        return tWordsList
    elif char == "u":
        return uWordsList
    elif char == "v":
        return vWordsList
    elif char == "w":
        return wWordsList
    elif char == "x":
        return xWordsList
    elif char == "y":
        return yWordsList
    elif char == "z":
        return zWordsList
    else:
        print("char must be a lowercase alphabetical character")
        return None

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
