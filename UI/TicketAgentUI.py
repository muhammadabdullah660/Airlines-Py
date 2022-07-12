from operator import indexOf
from os import stat
from BL.Passenger import Passenger
from DL.FlightDL import FlightDL
from BL.Flight import Flight
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
        print("5- Ordered Passengers  ")
        print("6- Exit")
        option = int(input('Your Option..'))
        return option

    @staticmethod
    def viewPassengersData():
        print(
            "Main Menu  >   Login    >   Admin >   View Passengers Data")
        print("---------------------")
        print(
            "Name \t CNIC \t Passport \t Phone \t Email \t Gender \t Total")
        for i in (PassengerDL.passengersList):
            print(
                f"{i.name}, {i.cnic}, {i.passportNo},  {i.contactNum}, {i.eMail}, {i.gender}, {i.total}")

    @staticmethod
    def viewPassengersFlights():
        print(
            "Main Menu  >   Login    >   Admin >   View Passengers travel Data")
        print("---------------------")
        print(
            "Departure \t Arrival \t Trip \t Date \t Time \t Class \t Price \t Seats ")
        for p in (PassengerDL.passengersList):
            for i in p.flight:
                print(
                    f"{i.departCity}, {i.arrCity}, {i.tripType},  {i.departDate}, {i.departTime}, {i.flightClass}, {i.price} , {i.seats}")
            print("---------------------")

    @staticmethod
    def viewSortedPassengersData():
        print(
            "Main Menu  >   Login    >   Admin >   View Ordered Passengers Data")
        print("---------------------")
        print(
            "Name \t CNIC \t Passport \t Phone \t Email \t Gender \t Total")
        for i in (PassengerDL.sortedPassengersList):
            print(
                f"{i.name}, {i.cnic}, {i.passportNo},  {i.contactNum}, {i.eMail}, {i.gender}, {i.total}")

    @staticmethod
    def addFlights():
        newFlight = Flight()
        print(
            "Main Menu  >   Login    >   Admin    >   Add new flights")
        print("---------------------")
        newFlight.departCity = input("Departure from :- ")
        newFlight.arrCity = input("Arrival To :- ")
        newFlight.tripType = input("Trip Type :- ")
        newFlight.departDate = input("Depart Date :-")
        newFlight.departTime = input("Depart Time :- ")
        newFlight.seats = int(input("No. of seats :- "))
        newFlight.price = int(input("Ticket Price :-"))
        newFlight.flightClass = input("Class :- ")
        return newFlight

    @staticmethod
    def viewFlights():
        print(
            "Main Menu  >   Login    >   Admin >   View Flights")
        print("---------------------")
        print(*FlightDL.flightsList, sep="\n")
