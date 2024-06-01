# get object type from properties?
from functions.helpers.fun_get_properties import getProperties

def getObjectType(flag):

    properties = getProperties()

    if flag == '1':

        returnValue = properties["path2D"]

    elif flag == '2':

        returnValue = properties["path3D"]

    return returnValue


