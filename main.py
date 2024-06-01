# main program

from functions.fun_get_object_type import getObjectType
from functions.fun_get_file_values import getFileValues
from functions.fun_string_to_float import getFloats
from functions.fun_get_points import getPoints
from functions.fun_check_points import checkPoints
from functions.fun_check_point_x import checkPointX
from functions.fun_get_diagonal import getDiagonal
from functions.fun_check_square import checkSquare


# get chosen object type:
pathToData = getObjectType('1')

# get values from file 2d - OK, 3d?:
returnedValues = getFileValues(pathToData)

returnedStrArr = returnedValues["strArr"]
flagObject = returnedValues["flagObject"]
# convert ints tu floats:
returnedfloatArr = getFloats(returnedStrArr)

# get points from float array?
returnedPointsArr = getPoints(returnedfloatArr, flagObject)

# check do points belong to rectangle?
returnedValue = checkPoints(returnedPointsArr, flagObject)

# if it is not a rectangle, show message and exit.
if not returnedValue:
    
    if flagObject == '1':

        print("This is not a rectangle.")
    else:

        print("This is not a cube.")        

    print("Bye, bye...")
    print("")
    exit()

# does point X exists in the rectangle?
returnedMessageX = checkPointX(returnedPointsArr, flagObject)
   
print(returnedMessageX)

# calculate diagonal?
returnedMsgDiagonal = getDiagonal(returnedPointsArr, flagObject)

print(returnedMsgDiagonal)

# find out is this square or cube?
returnedMsg = checkSquare(returnedPointsArr, flagObject)

print(returnedMsg)
print("")
