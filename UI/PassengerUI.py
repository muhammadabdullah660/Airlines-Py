from BL.Passenger import Passenger


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
        p.trip = input("Trip Type :- ")
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
