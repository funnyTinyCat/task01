# convert string values to floats
import os

def getFloats(strArr):

    returnValuesArr = []

    for f in strArr:

        if f.isdecimal():
            
            tmp = float(f)
            returnValuesArr.append(tmp)
        else:

            print("One coordinate has an element that is not a number.")
            print("Bye, bye...")
            print("")
            os._exit(os.EX_OK)

    return returnValuesArr
    
