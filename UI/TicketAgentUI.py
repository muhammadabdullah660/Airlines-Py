from operator import indexOf
from os import stat
from BL.Passenger import Passenger
from DL.FlightDL import FlightDL
from DL.PassengerDL import PassengerDL


class TicketAgentUI:
    @staticmethod
    def ticketAgentMenu():
        option = 0
        print("Main Menu  >   Login    >   Admin ")
        print("---------------------")
        print("Select one of the following options...")
        print("1- View Passengers Data")
        print("2- View Passengers travel Data")
        print("3- Add new flights ")
        print("4- View flights ")
        print("5- Allot Seats  ")
        print("6- Ordered Passengers  ")
        print("7- Exit")
        option = int(input('Your Option..'))
        return option

    @staticmethod
    def viewPData():
        print(
            "Main Menu  >   Login    >   Admin >   View Passengers Data")
        print("---------------------")
        print(
            "Name \t CNIC \t Passport \t Phone \t Email \t Gender \t Total")
        for i in (PassengerDL.passengersList):
            print(
                f"{i.name}, {i.cnic}, {i.passportNo},  {i.contactNum}, {i.eMail}, {i.gender}, {i.total}")
