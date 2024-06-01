# get properties

def getProperties():

    tmpArr = []
    returnValue = ""

    properties = {"path2D": "", "path3D": ""}

    try:
        file = open("config\properties.ini", "r")

        try:
            for f in file:

                tmpArr = f.split("=")

                if tmpArr[0] == "path2D":

                    properties["path2D"] = tmpArr[1].strip()

                elif tmpArr[0] == "path3D":

                    properties["path3D"] = tmpArr[1].strip()

        except:
            print("Došlo je do greške pri pokušaju čitanja fajla.")
        finally:
            file.close()

    except:
        print("Došlo je do greške pri pokušaju otvaranja dokumenta.")

    return properties

