# including Libraries

from UI.MUserUI import MUserUI
from collections import UserList
import os.path
from tkinter.messagebox import NO
from BL.MUser import MUser
from BL.Passenger import Passenger
from BL.TicketAgent import TicketAgent
from DL.TicketAgentDL import TicketAgentDL
from BL.Flight import Flight
from DL.MUserDL import MUserDL
from DL.FlightDL import FlightDL
from DL.PassengerDL import PassengerDL
from time import sleep
# Defining Main


def main():
    path = "MUser.txt"
    MUserDL.readDataFromFile(path)
    option = 0
    while (option != 3):
        os.system("cls")
        option = MUserUI.menu()
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
            if (not user.isAdmin()):
                p = Passenger(user)
                PassengerDL.addPassengerIntoList(p)
            else:
                a = TicketAgent(user)
                TicketAgentDL.addTicketAgentIntoList(a)

            MUserDL.storeDataInFile(user, path)


if __name__ == "__main__":
    main()
