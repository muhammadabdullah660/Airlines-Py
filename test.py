from collections import UserList
import os.path
from tkinter.messagebox import NO
from BL.MUser import MUser
from BL.Passenger import Passenger
from BL.Flight import Flight
from DL.MUserDL import MUserDL
from DL.FlightDL import FlightDL
from DL.PassengerDL import PassengerDL
from time import sleep


def takeInputUserReg():
    print("Main Menu  >   Login")
    print("---------------------")
    name = input("Enter username :- ")
    password = input("Enter password :- ")
    newUser = MUser(name, password)
    return newUser


def loginMenu():
    user = takeInputUserReg()
    for storedUser in MUserDL.userList:
        if storedUser.name == user.name and storedUser.password == user.password:
            return storedUser
    return None


def createaccount():
    flag = True
    c = 0, x
    ch = ''
    user, password, role = ""
    user = input("Enter the username: ")
    while(flag):
        password = input("Enter the password: ")
        c = 0
        for i in range(len(password)):
            ch = password[i]
            x = ch
            if password[i] >= 48 and password[i] <= 57:
                c += 1
        if c == 0 or len(password) < 2:
            flag = True
            print("Password Should Contain a Number and should be more than 1 character")
        else:
            flag = False
    role = input("Enter the role ( Admin Or User ): ")
    newUserReg = MUser(user, password, role)
    return newUserReg


def passengerMenu():
    optionP = 0
    print("Main Menu  >   Login    >   Passenger")
    print("---------------------")
    print("Select one of the following options...")
    print("1- Registration")
    print("2- Enter Flight Details")
    print("3- Book from available Flights")
    print("4- See booked Flights ")
    print("5- Cancel A flight  ")
    print("6- Exit  ")
    optionP = input("Your Option..")
    return optionP


def flightP():
    flagx = True
    departCity, arrCity, trip, departDate, pClass = ""
    adult, child, infant, totalSeats = 0
    print("Main Menu  >   Login    >   Passenger    >    Enter Flight Details")
    print("---------------------")
    departCity = input("Departure from :- ")
    arrCity = input("Arrival To :- ")
    trip = input("Trip Type :- ")
    departDate = print("Depart Date :-")
    print("---------Passengers----------")
    while flagx:
        adult = int(input("No of Passengers (Adult) :- "))
        if adult < 0:
            print("Enter again")
            flagx = True
        else:
            flagx = False
    flagx = True
    while flagx:
        child = int(input("No of Passengers (Child) :- "))
        if (child < 0):
            print("Enter again")
            flagx = True
        else:
            flagx = False
    flagx = True
    while flagx:
        infant = int(input("No of Passengers (Infant) :- "))
        if (infant < 0):
            print("Enter again")
            flagx = True
        else:
            flagx = False
    print("---------Class---------")
    pClass = input("Enter Class :- ")
    totalSeats = adult + child


def bookP():
    print("Main Menu  >   Login    >   Passenger    >   Book from available Flights")
    print("---------------------")
    for i in range(len(FlightDL.flightsList)):
        flightClass checkF = flightsList[i]
            if (checkF.checkflightExist(pDepartCity[entry_count], pArrCity[entry_count], pDepartDate[entry_count]))
                    print($"1- From \t  pDepartCity[entry_count]  \t To \t   pArrCity[entry_count] \t at \t flightsList[i].aDepartTime \t \t pDepartDate[entry_count]")
                    optionF[entry_count] = .Parse(Console.ReadLine())
                    return optionF[entry_count]
                else
                    print("No flights available!!")
                    optionF[entry_count] = 0
            return optionF[entry_count]
        // Expenditures
         void invoice()

            print(
                  "Departure\tArrival\tTrip\tDate\tAdults\tChild\tInfants\tClass ")

            print($"pDepartCity[entry_count] \t pArrCity[entry_count] \t pTrip[entry_count]  \t pDepartDate[entry_count]  \t adult[entry_count]  \t child[entry_count]  \t infant[entry_count]  \t pClass[entry_count]")

            print(
                 "--------Expenditures---------")

            print($"No of Passengers (Adult)(600$) :- adult[entry_count]")
            print($"No of Passengers (Child) (450$):- child[entry_count]")
            print($"No of Passengers (Infant)(0$) :-  infant[entry_count]")

            total[entry_count] = (adult[entry_count] * 600) +
                                (child[entry_count] * 450)
            if (pClass[entry_count] == "Business" | | pClass[entry_count] == "business")

                total[entry_count] = total[entry_count] + 400

            print($"Your Total Expenditure :-  total[entry_count]$")

        // See booked Flights
         void bookedFlightsP()

             i = 0
            print("Main Menu  >   Login    >   Passenger    >   See booked Flights")
            print("---------------------")
            print("Your Flights...")
            for (j=0  j < userList.Count  j++)

                if (userList[j].role == "admin")

                    i--

                else if (userList[j].name == name)

                    i=j + i
                    // print($"i j entry_count")


                    if (optionF[i] == 1)

                        print($"1- From \t  pDepartCity[i]  \t To \t  pArrCity[i]   \t at \t 12:00 \t \t  pDepartDate[i]")
                        print($"Your Total Expenditure :-  total[i]$")

                    else if (optionF[i] == 0)

                        print("No booked flights yet!!")




        // Cancel Flights
         void cancelFlights()

             i=0
             cancel
            print("Main Menu  >   Login    >   Passenger    >   Cancel A flight")
            print("---------------------")
            print("Your Flights...")

            for (j=0  j < userList.Count  j++)

                if (userList[j].role == "admin")

                    i--

                else if (userList[j].name == name)

                    i=j + i
                    if (optionF[i] == 1)

                        print($"1- From \t  pDepartCity[i]  \t To \t  pArrCity[i]   \t at \t 12:00 \t \t  pDepartDate[i]")
                        print($"Your Total Expenditure :-  total[i]$")
                        print("Your Option..")
                        cancel=.Parse(Console.ReadLine())
                        if (cancel == 1)

                            print("Flight has been canceled!!")
                            optionF[entry_count]=0



                    else if (optionF[i] == 0)

                        print("No booked flights yet!!")





        // ADMIN
        // MENU OF ADMIN
          adminMenu()

             optionA
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
            print("Your Option..")
            optionA=.Parse(Console.ReadLine())
            return optionA

        // VIEW PASSENGERS DATA
         void viewPData()

            print("Main Menu  >   Login    >   Admin >   View Passengers Data")
            print("---------------------")
            print(
                "Name \t CNIC \t Passport \t Phone \t Email \t Gender \t Seats \t Total")
            for (i=0  i <= entry_count  i++)

                print($"pName[i]  \t cnic[i]  \t passport[i]  \t pNum[i]  \t mail[i]  \t gender[i]  \t seating[i]  \t total[i]")



        // VIEW PASSENGERS TRAVEL DATA
         void viewPTravelData()

            print("Main Menu  >   Login    >   Admin >   View Passengers travel Data")
            print("---------------------")
            print(
          "Departure \t Arrival \t Trip \t Date \t Adults \t Child \t Infants \t Class ")
            for (i=0  i <= entry_count  i++)

                print($"pDepartCity[i] \t pArrCity[i] \t pTrip[i]  \t pDepartDate[i]  \t adult[i]  \t child[i]  \t infant[i]  \t pClass[i]")


        // ADD FLIGHTS
         flightClass addFlights()

            print(flight_count)
            flightClass flightsX=new flightClass()
            print("Main Menu  >   Login    >   Admin    >   Add new flights")
            print("---------------------")
            print("Departure from :- ")
            flightsX.aDepartCity=Console.ReadLine()
            print("Arrival To :- ")
            flightsX.aArrCity=Console.ReadLine()
            print("Trip Type :- ")
            flightsX.aTrip=Console.ReadLine()
            print("Depart Date :-")
            flightsX.aDepartDate=Console.ReadLine()
            print("Depart Time :- ")
            flightsX.aDepartTime=Console.ReadLine()
            flight_count++
            return flightsX

         void addFlightIntoList(flightClass addFlight)


            flight_count++

            flightsList.Add(addFlight)


         void viewFlightsA()

            print(flightsList.Count)

            print("Main Menu  >   Login    >   Admin >   View Flights")
            print("---------------------")
            print("Departure \t Arrival \t Trip \t DepartDate \t DepartTime")
            for (i=0  i < flightsList.Count  i++)

                print($"flightsList[i].aDepartCity  \t flightsList[i].aArrCity  \t flightsList[i].aTrip  \t flightsList[i].aDepartDate  \t flightsList[i].aDepartTime")


        // ALLOT SEATS
         void seats()

             total=0
            print("Main Menu  >   Login    >   Admin    >   Allot Seats")
            print("---------------------")
            print(
                "Departure \t Arrival \t Trip \t Date \t Adults \t Child \t Infants \t Class ")

            for (i=0  i <= entry_count  i++)

                print($"pDepartCity[i] \t pArrCity[i] \t pTrip[i]  \t pDepartDate[i]  \t adult[i]  \t child[i]  \t infant[i]  \t pClass[i]")

                print($"No of Passengers (Adult) :-  adult[i]")




                print($"No of Passengers (Child) :-  child[i]")




                print($"No of Passengers (Infant) :-  infant[i]")
                total=(adult[i]) + (child[i])

                print("Enter Seat Range :- ")
                seating[i]=Console.ReadLine()


         void clearScreen()

            print("Press any key to continue...")
            Console.ReadKey()
            Console.Clear()


        // SORTED PASSENGERS
         void sorting()

            print("Main Menu  >   Login    >   Admin    >   Ordered Passengers")
            print("---------------------")
            print(
                "Name \t CNIC \t Passport \t Phone \t Email \t Gender \t Seats \t Total")

            for (i=0  i <= entry_count  i++)

                for (j=i + 1  j <= entry_count  j++)

                    if (total[j] > total[i])
                     // sort total
                         temp=total[i]
                        total[i]=total[j]
                        total[j]=temp
                        // sort pName
                         namex=pName[i]
                        pName[i]=pName[j]
                        pName[j]=namex
                        // sort cnic array
                         name1=cnic[i]
                        cnic[i]=cnic[j]
                        cnic[j]=name1
                        // sort passport
                         name2=passport[i]
                        passport[i]=passport[j]
                        passport[j]=name2
                        // sort pNum
                         name3=pNum[i]
                        pNum[i]=pNum[j]
                        pNum[j]=name3
                        // sort mail
                         name4=mail[i]
                        mail[i]=mail[j]
                        mail[j]=name4
                        // sort gender
                         name5=gender[i]
                        gender[i]=gender[j]
                        gender[j]=name5
                        // sort gender
                         name6=seating[i]
                        seating[i]=seating[j]
                        seating[j]=name6



            for (i=0  i <= entry_count  i++)

                print($"pName[i]  \t cnic[i]  \t passport[i]  \t pNum[i]  \t mail[i]  \t gender[i]  \t seating[i]  \t total[i]")







def main():

            MUserDL.loadFromFile("MUser.txt")
            // FlightDL.loadFromFile("prod.txt")
             option=0, optionP=0, optionA=0

            while (option < 4)

                MenuUI.header()
                option=MenuUI.mainMenu()
                if (option == 1)

                    MenuUI.header()
                    MUser user=MUserUI.signInMenu()
                    MUser whatUser=MUserDL.isValid(user)
                    if (whatUser != null)

                        // Passenger
                        if (!whatUser.isAdmin())

                            optionP=0
                            while (optionP < 6)

                                MenuUI.header()
                                optionP=passengerMenu()
                                // REGISTRATION
                                if (optionP == 1)

                                    MenuUI.header()
                                    registrationP()
                                    clearScreen()

                                // Enter Flight Details
                                else if (optionP == 2)

                                    MenuUI.header()
                                    flightP()
                                    clearScreen()

                                // Book from available Flights
                                else if (optionP == 3)

                                    MenuUI.header()
                                    optionF[entry_count]=bookP()
                                    if (optionF[entry_count] == 1)

                                        invoice()

                                    clearScreen()

                                // View booked flights
                                else if (optionP == 4)

                                    MenuUI.header()
                                    bookedFlightsP()
                                    clearScreen()

                                // Cancel booked flights
                                else if (optionP == 5)

                                    MenuUI.header()
                                    cancelFlights()
                                    clearScreen()




                        // ADMIN
                        else if (whatUser.isAdmin())

                            optionA=0
                            while (optionA < 7)

                                MenuUI.header()
                                optionA=adminMenu()
                                // View Passengers Data
                                if (optionA == 1)

                                    MenuUI.header()
                                    viewPData()
                                    clearScreen()

                                // View Passengers travel Data
                                else if (optionA == 2)

                                    MenuUI.header()
                                    viewPTravelData()
                                    clearScreen()

                                // Add new flights
                                else if (optionA == 3)

                                    MenuUI.header()
                                    flightsList.Add(addFlights())
                                    flightClass newFlight=addFlights()
                                    addFlightIntoList(newFlight)
                                    clearScreen()


                                else if (optionA == 4)

                                    MenuUI.header()
                                    viewFlightsA()
                                    clearScreen()


                                // Allot Seats
                                else if (optionA == 5)

                                    MenuUI.header()
                                    seats()
                                    clearScreen()


                                // Ordered Passengers
                                else if (optionA == 6)

                                    MenuUI.header()
                                    sorting()
                                    clearScreen()




                    else if (whatUser == null)

                        print("Please Sign Up first with role i.e Admin OR User")
                        clearScreen()



                if (option == 2)

                    MenuUI.header()
                    print("Main Menu  >   Sign Up ")
                    print("---------------------")
                    MUser newUser=createaccount()
                    addUserIntoList(newUser)
                    storeCred()
                    clearScreen()

                else if (option == 3)

                    MenuUI.header()
                    print("Main Menu  >   Details ")
                    print("---------------------")
                    print("Developed By :- Muhammad Abdullah")
                    print("Registration No :- 2021-CS-82")
                    print("Section :- CS-B")
                    print("Submitted To :- DR.AWAIS")
                    clearScreen()


            storeFlight()
            storeData()

        // END OF MAIN FUNCTION
