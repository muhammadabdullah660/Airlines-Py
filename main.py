# including Libraries
from DL.MUserDL import MUserDL
from UI.MUserUI import MUserUI
import os
from time import sleep
# Defining Main


def main():
    path = "test.txt"
    MUserDL.readDataFromFile(path)
    option = 0
    while (option != 3):
        os.system("cls")
        option = MUserUI.menue()
        if(option == 1):
            # sign in
            user = MUserUI.TakeInputWithOutRole()
            user = MUserDL.signIn(user)
            if(user != None):
                if(user.isAdmin()):
                    print("This is Admin")
                    # Admin code
                else:
                    print("This is User")
                    # user Code
                sleep(3)
            else:
                print("user doesn't Exsists")

        elif (option == 2):
            # signUp
            user = MUserUI.TakeInputFromConsole()
            MUserDL.addUserInList(user)
            MUserDL.storeDataInFile(user, path)


if __name__ == "__main__":
    main()
