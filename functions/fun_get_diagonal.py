# count diagonal    
import math
from functions.helpers.fun_get_sides import getSides

def getDiagonal(pointsArr, flagObject):

    message = ""
    returnedSides = getSides(pointsArr, flagObject)

    if flagObject == '1':
        
        diagonal = math.sqrt(pow(returnedSides['a'], 2)  + pow(returnedSides['b'], 2))
        message = "Diagonal is " + str(diagonal)
    else: 

        diagonal = math.sqrt(pow(returnedSides['a'], 2) + pow(returnedSides['b'], 2) + pow(returnedSides['c'], 2))
        message = "Spatial diagonal is " + str(diagonal)

    return message

