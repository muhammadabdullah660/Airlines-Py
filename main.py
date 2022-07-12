# including Libraries

from UI.MUserUI import MUserUI
from UI.mainMenuUI import MenuUI
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
from UI.TicketAgentUI import TicketAgentUI
# Defining Main


def main():
    path = "MUser.txt"
    MUserDL.readDataFromFile(path)
    option, optionP, optionT = 0, 0, 0
    while (option < 4):
        os.system("cls")
        option = MenuUI.mainMenu()
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
                    while optionT < 6:
                        os.system("cls")
                        optionT = TicketAgentUI.ticketAgentMenu()
                        if optionT == 1:
                            os.system("cls")
                            TicketAgentUI.viewPassengersData()
                        elif optionT == 2:
                            os.system("cls")
                            TicketAgentUI.viewPassengersFlights()
                        elif optionT == 3:
                            os.system("cls")
                            newFlight = Flight()
                            newFlight = TicketAgentUI.addFlights()
                            FlightDL.addFlightIntoList(newFlight)
                        elif optionT == 4:
                            os.system("cls")
                            TicketAgentUI.viewFlights()
                        elif optionT == 5:
                            os.system("cls")
                            PassengerDL.sortPassengersByTotal()
                            TicketAgentUI.viewSortedPassengersData()

                    # print("f")
                    # sleep(2)
                else:
                    # This is Passenger Menu
                    # print(len(PassengerDL.passengersList))
                    # sleep(5)
                    p = PassengerDL.isValidPassenger(user)
                    while optionP < 7:
                        os.system("cls")
                        optionP = PassengerUI.passengerMenu()
                        if optionP == 1:
                            os.system("cls")
                            PassengerUI.registrationP(p)
                        elif optionP == 2:
                            os.system("cls")
                            PassengerUI.flightP(p)
                        elif optionP == 3:
                            os.system("cls")
                            newFlight = Flight()
                            newFlight = PassengerUI.bookP(p)
                            p.bookFlight(newFlight)
                            # Calculate total and assign to respective flight price of passenger
                            p.flight[newFlight].price = p.adult*600+p.child*450
                            # Calculate total seats and assign to respective flight seats of passenger
                            p.flight[newFlight].seats = p.adult+p.child
                            # subtract total seats of flight
                            FlightDL.flightsList[newFlight].seats -= p.adult+p.child
                        elif optionP == 4:
                            os.system("cls")
                            PassengerUI.seeBookedFlights(p)
                        elif optionP == 5:
                            os.system("cls")
                            p.cancelBookedFlight(PassengerUI.cancelFlight(p))
                        elif optionP == 6:
                            os.system("cls")
                            PassengerUI.viewFlights()

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

            #MUserDL.storeDataInFile(user, path)


if __name__ == "__main__":
    main()
