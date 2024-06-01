# get points

def getPoints(floatArr, flagObject):

    if flagObject == '1':

        aX = floatArr[0]
        aY = floatArr[1]

        bX = floatArr[2]
        bY = floatArr[3]

        cX = floatArr[4]
        cY = floatArr[5]

        xX = floatArr[6]
        xY = floatArr[7]


        a = {"x": aX, "y": aY}
        b = {"x": bX, "y": bY}
        c = {"x": cX, "y": cY}
        x = {"x": xX, "y": xY}

        resultValue = [a, b, c, x]
    
    else:

        aX = floatArr[0]
        aY = floatArr[1]
        aZ = floatArr[2]

        bX = floatArr[3]
        bY = floatArr[4]
        bZ = floatArr[5]

        cX = floatArr[6]
        cY = floatArr[7]
        cZ = floatArr[8]

        dX = floatArr[9]
        dY = floatArr[10]
        dZ = floatArr[11]

        xX = floatArr[12]
        xY = floatArr[13]
        xZ = floatArr[14]


        a = {"x": aX, "y": aY, "z": aZ}
        b = {"x": bX, "y": bY, "z": bZ}
        c = {"x": cX, "y": cY, "z": cZ}
        d = {"x": dX, "y": dY, "z": dZ}
        x = {"x": xX, "y": xY, "z": xZ}

        resultValue = [a, b, c, d, x]

    return resultValue

