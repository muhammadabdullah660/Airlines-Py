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
    adult = 0
    child = 0
    infant = 0
    totalSeats = 0
    tripType = ""
    pClass = ""

    def __init__(self, id):
        self.id = id

    def cancelBookedFlight(self, myFlight):
        self.flight.remove(myFlight)

    def calculatePrice(self, item,  myFlight):
        x = ((self.adult * item.Price) + (self.child * (item.Price)) /
             2 + (self.infant * (item.Price) / 4))
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

    def viewBookedFlights(self):
        self.total = 0.0
        for pa in self.flight:
            print(
                f"{pa.departCity} \t {pa.arrCity} \t {pa.tripType}  \t {pa.departDate}  \t {pa.departTime}  \t {pa.flightClass}  \t {pa.price}  \t {pa.seats}")
            self.total += pa.price
