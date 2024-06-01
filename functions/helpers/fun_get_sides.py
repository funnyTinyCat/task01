# count and get sides

def getSides(pointsArr, flagObject):

    sides = {"a": 0, "b": 0, "c": 0}

    a = pointsArr[0]
    b = pointsArr[1]
    c = pointsArr[2]
  
    if flagObject == '1':

        aSide = b["x"] - a["x"]  
        bSide = c["y"] - b["y"]

        sides['a'] = aSide
        sides['b'] = bSide
    else:

        d = pointsArr[3]

        aSide = b["x"] - a["x"]
        bSide = c["y"] - b["y"]
        cSide = d["z"] - a["z"]

        sides['a'] = aSide
        sides['b'] = bSide
        sides['c'] = cSide


    return sides

