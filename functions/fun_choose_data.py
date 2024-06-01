# simple manu

def chooseData():


    flag = True

    while flag:
        print("")
        print("")
        print("If you want 2d object, press [1] and [enter].")
        print("If you want 3d object, press [2] and [enter].")
        print("If you want to exit, type [exit] and press [enter].")        
        enteredValue = input("Please, enter the choice: ")

        if enteredValue == 'exit':
            print("Bye, bye...")
            exit()

        if (enteredValue == '1') or (enteredValue == '2'):
            flag = False


    return enteredValue

