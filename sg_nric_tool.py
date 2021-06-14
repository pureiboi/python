## written with version 3.9.5
import random

ST_base = ['J','Z','I','H','G','F','E','D','C','B','A']
FG_base = ['R','Q','P','N','M','L','K','X','W','U','T']

weight = [2,7,6,5,4,3,2]

def isValidNric(nric = ""):
    """
    :param nric: format in XnnnnnnnX, n=number, X=alphabet
    :return: boolean, valid=true, invalid=false
    """
    if len(nric) != 9:
        return False
    if not nric[1:len(nric)-1].isdigit():
        return False
    if nric[len(nric)-1] != getCheckDigit(nric):
        return False
    return True


def getCheckDigit(nric = ""):
    """ generate check digit for last character """
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
    """
    :param prefixz: either S, T, F, G, randomly generated when not provided
    :param digitz: digit to prefix e.g when 87, then X87nnnnnX, when 8954, then X8954nnnX
    :return: 9 characters XnnnnnnnX, n=number, X=alphabet
    """
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
    return nricPart + getCheckDigit(nricPart + "X")


if __name__ == "__main__":

    generationCount = 50
    for x in range(1, generationCount):
        digitz = "9500000"
        digitz = digitz[0:len(digitz) - len(str(x))]
        digitz = f"{digitz}{x}"
        print(generateNric("t", digitz))


