from BL.Passenger import Passenger


class PassengerUI:
    @staticmethod
    def registrationP(p):
        flag = True
        pName, cnic, pNum, mail, gender, passport = ""
        # Passenger newPassenger = new Passenger()
        print(
            "Main Menu  >   Login    >   Passenger    >    Registration")
        print("---------------------")

        pName = input("Enter your name :- ")
        p.name = pName
        while (flag):
            cnic = input("Enter your CNIC :- ")
            #flag = newPassenger.Cnic(cnic)
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
