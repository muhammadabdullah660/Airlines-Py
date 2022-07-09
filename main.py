# including Libraries

from UI.MUserUI import MUserUI
from collections import UserList
import os.path
from tkinter.messagebox import NO
#from BL.MUser import MUser
from BL.Passenger import Passenger
from BL.TicketAgent import TicketAgent
from DL.TicketAgentDL import TicketAgentDL
from BL.Flight import Flight
from DL.MUserDL import MUserDL
from DL.FlightDL import FlightDL
from DL.PassengerDL import PassengerDL
from time import sleep

from UI.PassengerUI import PassengerUI
# Defining Main


def main():
    path = "MUser.txt"
    MUserDL.readDataFromFile(path)
    option, optionP, optionT = 0, 0, 0
    while (option != 3):
        os.system("cls")
        option = MUserUI.menu()
        if(option == 1):
            # sign in
            os.system("cls")
            userX = MUserUI.TakeInputWithOutRole()
            user = MUserDL.signIn(userX)
            # print(f"{len(MUserDL.userList)}")
            # print(f"{(user.userName)}")
            # sleep(2)
            if(user != None):
                # print("f")
                # sleep(2)
                if(user.isAdmin()):
                    # This is Admin menu
                    a = TicketAgentDL.isValidTicketAgent(user)
                    # print("f")
                    # sleep(2)
                else:
                    # This is Passenger Menu
                    # print(len(PassengerDL.passengersList))
                    # sleep(5)
                    p = PassengerDL.isValidPassenger(user)
                    while optionP < 6:
                        os.system("cls")
                        optionP = PassengerUI.passengerMenu()
                        if optionP == 1:
                            PassengerUI.registrationP(p)
                        elif optionP == 2:
                            PassengerUI.flightP(p)
            else:
                print("User doesn't Exist")
                sleep(5)

        elif (option == 2):
            # signUp
            os.system("cls")
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
