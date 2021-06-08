## written with version 3.9.5
import random

ST_base = ['J','Z','I','H','G','F','E','D','C','B','A']
FG_base = ['R','Q','P','N','M','L','K','X','W','U','T']

weight = [2,7,6,5,4,3,2]

def isValidNric(nric = ""):
    if len(nric) != 9:
        return False
    if nric[len(nric)-1] != getCheckDigit(nric):
        return False
    return True


def getCheckDigit(nric = ""):

    digits = nric[1:len(nric)-1]
    sum = 0
    idx = 0
    for digit in digits:
        sum += (int(digit) * weight[idx])
        idx+=1

    if nric[0].upper() in "TG":
       sum += 4

    if nric[0].upper() in "FG":
        return FG_base[sum%11]

    if nric[0].upper() in "ST":
        return ST_base[sum%11]


def generateNric(prefixz="", digitz=""):

    digits = digitz
    while(len(digits)!=7):
        digits = digits + str(random.randint(0, 9))

    if not prefixz:
        rnd = random.randint(0,4)
        if rnd == 0:
            prefixz = "S"
        elif rnd == 1:
            prefixz = "T"
        elif rnd == 1:
            prefixz = "F"
        else:
            prefixz = "G"
    else:
        prefixz = prefixz[0].upper()
    nricPart = prefixz + digits
    return nricPart + getCheckDigit(nricPart)
