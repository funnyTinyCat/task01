# check does point x is inside the rectangle?

def checkPointX(pointsArr, flagObject):

    message = ""

    a = pointsArr[0]
    b = pointsArr[1]
    c = pointsArr[2]


    if flagObject == '1':

        x = pointsArr[3]


        if ((x["x"] >= a["x"]) and (x["y"] >= a["y"])) and ((x["x"] <= b["x"])) and ( (x["y"] <= c["y"]) ):
            
            message = "X point is inside the rectangle."
        else:
            message = "X point is outside the rectangle."

    else:

        d = pointsArr[3]
        x = pointsArr[4]

        if ((x["x"] >= a["x"]) and (x["y"] >= a["y"]) and (x["z"] >= a["z"])) and ((x["x"] <= b["x"])) and ((x["y"] <= c["y"])) and ((x["z"] <= d["z"])):
            
            message = "X point is inside the 3D object."
        else:
            message = "X point is outside the 3D object."


    return message

