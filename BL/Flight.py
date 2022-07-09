class Flight:
    arrCity = ""
    departCity = ""
    tripType = ""
    departDate = ""
    departTime = ""
    seats = 0
    price = 0
    flightClass = ""

    def __init__(self, *args):
        if len(args > 4):
            self.departCity = args[0]
            self.arrCity = args[1]
            self.tripType = args[2]
            self.departDate = args[3]
            self.departTime = args[4]
            self.seats = args[4]
            self.price = args[5]
            self.flightClass = args[6]
        elif len(args <= 4):
            self.departCity = args[0]
            self.arrCity = args[1]
            self.tripType = args[2]
            self.departDate = args[3]

    def checkFlight(self, arrCity, departCity, tripType, departDate):
        if self.arrCity == arrCity and self.departCity == departCity and self.tripType == tripType and self.departDate == departDate:
            return True
        return False
