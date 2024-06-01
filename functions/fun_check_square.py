# check is this square?
from functions.helpers.fun_get_sides import getSides


def checkSquare(pointsArr, flagObject):

    message = ""

    sides = getSides(pointsArr, flagObject)

    if flagObject == '1':

        if sides['a'] == sides['b']:

            message = "It is a square."
        else:

            message = "It is a rectangle."
    else:
        
        if (sides['a'] == sides['b']) and (sides['c'] == sides['a']):

            message = "It is a cube that consists of the same sides."
        else:

            message = "It is a cube that has different sides."


    return message
