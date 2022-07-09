from BL.MUser import MUser


class Passenger:
    name = ""
    passportNo = ""
    cnic = ""
    eMail = ""
    gender = ""
    contactNum = ""
    flight = []
    id = MUser()
    total = 0.0

    def __init__(self, id):
        self.id = id

    def cancelBookedFlight(self, myFlight):
        self.flight.remove(myFlight)

    def calculatePrice(self, item,  myFlight,  Adult,  Child,  Infant):
        x = ((Adult * item.Price) + (Child * (item.Price)) /
             2 + (Infant * (item.Price) / 4))
        x += myFlight.Seats * self.checkClass(myFlight)
        return x

    def checkClass(myFlight):
        if myFlight.FlightClass == "Business":
            return myFlight.Price * 10
        return 1

    def calculateTotal(self):
        self.total = 0
        for item in self.flight:
            self.total += item.Price

    def bookFlight(self, myFlight):
        self.flight.append(myFlight)
