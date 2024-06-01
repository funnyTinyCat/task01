# retnurn array

def getArr(strPart, delimiter):

    tmpArr02 = []

    tmpArr = strPart.split(delimiter)

    for t in tmpArr:

        tmp = str(t.strip().strip("\n"))
        tmpArr02.append(tmp)

    return tmpArr02