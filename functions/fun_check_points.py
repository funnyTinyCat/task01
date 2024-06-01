# check rectangle points:

def checkPoints(pointsArr, flagObject):

    returnValue = False

    a = pointsArr[0]
    b = pointsArr[1]
    c = pointsArr[2]

# check if these are rectangle points:
    if flagObject == '1':

        if (b["y"] == a["y"]) and (c["x"] == a["x"]):

            if (b["x"] > a["x"]) and (c["y"] > a["y"]):

                returnValue = True
            else:

                returnValue = False
        else:

            returnValue = False

    else:

        d = pointsArr[3]

        if ((b["y"] == a["y"]) and (b["z"] == a["z"])) and ((c["x"] == a["x"]) and (c["z"] == a["z"])) and ((d["x"] == a["x"]) and (d["y"] == a["y"])):

            if (b["x"] > a["x"]) and (c["y"] > a["y"]) and (d["z"] > a["z"]):

                returnValue = True
            else:

                returnValue = False
        else:

            returnValue = False


    return returnValue

