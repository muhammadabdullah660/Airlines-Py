from operator import indexOf
from os import stat
from BL.Passenger import Passenger
from DL.FlightDL import FlightDL
from DL.PassengerDL import PassengerDL


class PassengerUI:
    @staticmethod
    def passengerMenu():
        option = 0
        print("Main Menu  >   Login    >   Passenger")
        print("---------------------")
        print("Select one of the following options...")
        print("1- Registration")
        print("2- Enter Flight Details")
        print("3- Book from available Flights")
        print("4- See booked Flights ")
        print("5- Cancel A flight  ")
        print("6- Exit  ")
        option = int(input('Your Option..'))
        return option

    @staticmethod
    def registrationP(p):
        flag = True
        pName, cnic, pNum, mail, gender, passport = "", "", "", "", "", ""
        # Passenger newPassenger = new Passenger()
        print(
            "Main Menu  >   Login    >   Passenger    >    Registration")
        print("---------------------")

        pName = input("Enter your name :- ")
        p.name = pName
        while (flag):
            cnic = input("Enter your CNIC :- ")
            if len(cnic) < 13 or len(cnic) > 13:
                print("Enter CNIC again of 13 characters")
                flag = True
            else:
                flag = False
                p.cnic = cnic

        p.passportNo = input("Enter your passport no. :- ")
        p.contactNum = input("Enter your Phone Number :- ")
        p.eMail = input("Enter your email :- ")
        p.gender = input("Enter your Gender :- ")

    def flightP(p):
        flag = True
        # departCity, arrCity, trip, departDate, pClass = ""
        adult, child, infant, totalSeats = 0, 0, 0, 0
        print("Main Menu  >   Login    >   Passenger    >    Enter Flight Details")
        print("---------------------")
        p.departCity = input("Departure from :- ")
        p.arrCity = input("Arrival To :- ")
        p.tripType = input("Trip Type :- ")
        p.departDate = input("Depart Date :-")
        print("---------Passengers----------")
        # Validation on number of seats
        while (flag):
            adult = int(input("No of Passengers (Adult) :- "))
            if (adult < 0):
                print("Enter again")
                flag = True
            else:
                flag = False
                p.adult = adult
        flag = True
        while (flag):
            child = int(input("No of Passengers (Child) :- "))
            if (child < 0):
                print("Enter again")
                flag = True
            else:
                flag = False
                p.child = child
        flag = True
        while (flag):
            infant = int(input("No of Passengers (Infant) :- "))
            if (infant < 0):
                print("Enter again")
                flag = True
            else:
                flag = False
                p.infant = infant
        print("---------Class---------")
        p.pClass = input("Enter Class :- ")
        p.totalSeats = adult + child+infant

    @staticmethod
    def bookP(p):
        listf = []
        print("Main Menu  >   Login    >   Passenger    >   Book from available Flights")
        print("---------------------")
        for i in (FlightDL.flightsList):
            if (i.checkFlight(p.arrCity, p.departCity, p.tripType,  p.departDate)):
                listf.append(i)
                print(
                    f"{i.arrCity}, {i.departCity}, {i.tripType},  {i.departDate}, {i.departTime}, {i.flightClass},{i.price}")
            else:
                print("No flights available!!")
        option = int(input("Enter your option"))
        p.bookFlight(listf[option+1])
        p.flight[listf[option+1]].price = p.adult*600+p.child*450
        p.flight[listf[option+1]].seats = p.adult+p.child
        return option

    @staticmethod
    def invoice(p):
        print("--------Expenditures---------")
        print(f"No of Passengers (Adult)(600$) ")
        print(f"No of Passengers (Child) (450$)")
        print(f"No of Passengers (Infant)(0$)  ")
        print("Departure\tArrival\tTrip\tDate\tTime\tClass\tPrice\tSeats")
        for pa in p.flight:
            print(
                f"{pa.departCity} \t {pa.arrCity} \t {pa.tripType}  \t {pa.departDate}  \t {pa.departTime}  \t {pa.flightClass}  \t {pa.price}  \t {pa.seats}")
            p.total += pa.price
        print(f"Your Total Expenditure :-  {p.total}$")

    @staticmethod
    def seeBookedFlights(p):
        print("Departure\tArrival\tTrip\tDate\tTime\tClass\tPrice\tSeats")
        if len(p.flight) > 0:
            for pa in p.flight:
                print(
                    f"{pa.departCity} \t {pa.arrCity} \t {pa.tripType}  \t {pa.departDate}  \t {pa.departTime}  \t {pa.flightClass}  \t {pa.price}  \t {pa.seats}")
        else:
            print("No booked flights yet!!")
