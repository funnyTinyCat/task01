# file handling
from functions.helpers.fun_get_arr import getArr


def getFileValues(pathToData):

    tmp = ""
    tmpArr = []
    tmpLength = 0
    returnValues = {"strArr": [], "flagObject": "0"}

    try:
        file = open(pathToData, "r")

        try:
            for f in file:
                tmpArr02 = getArr(f, ',')
                tmpArr += tmpArr02
                tmpLength = len(tmpArr02)

        except:
            print("Došlo je do greške pri pokušaju čitanja fajla.")
        finally:
            file.close()

    except:
        print("Došlo je do greške pri pokušaju otvaranja dokumenta.")

    returnValues["strArr"] = tmpArr

    if tmpLength == 2:

        returnValues["flagObject"] = '1'
    else:

        returnValues["flagObject"] = '2'

    return returnValues

