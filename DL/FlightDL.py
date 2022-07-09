from collections import UserList
import os.path
from BL.MUser import MUser
from BL.Passenger import Passenger
from time import sleep
from DL.MUserDL import MUserDL
from DL.PassengerDL import PassengerDL


class FlightDL:
    flightsList = []
    requestedFlightsList = []

    @staticmethod
    def addFlightIntoList(newFlight):
        FlightDL.flightsList.append(newFlight)

    @staticmethod
    def addReqFlightIntoList(reqFlight):
        FlightDL.requestedFlightsList.append(reqFlight)

    @staticmethod
    def checkFlight(newFlight):
        for item in FlightDL.flightsList:
            if item.DepartCity == newFlight.DepartCity and item.ArrCity == newFlight.ArrCity and item.TripType == newFlight.TripType and item.DepartDate == newFlight.DepartDate:
                return item
        return None

    @staticmethod
    def cancelFlight(newFlight):
        index = FlightDL.flightsList.index(newFlight)
        FlightDL.flightsList.remove(index)

    @staticmethod
    def deleteRequestedFlight(newFlight):
        index = FlightDL.requestedFlightsList.index(newFlight)
        FlightDL.requestedFlightsList.remove(index)

    @staticmethod
    def editFlightFromList(previous,  updated):
        for item in FlightDL.flightsList:
            if item == previous:
                item.arrCity = updated.arrCity
                item.departCity = updated.departCity
                item.departTime = updated.departTime
                item.departDate = updated.departDate
                item.seats = updated.seats
                item.price = updated.price
                item.tripType = updated.tripType
                item.flightClass = updated.flightClass


#     public static bool loadFromFile(string path, string pathF)
#
#         StreamReader f = new StreamReader(path)
#         string record
#         if (File.Exists(path) & & File.Exists(pathF))
#
#             while ((record=f.ReadLine()) != null)
#
#                 string[] splittedRecord = record.Split(',')
#                 string departCity = splittedRecord[0]
#                 string arrCity = (splittedRecord[1])
#                 string tripType = (splittedRecord[2])
#                 DateTime departDate = DateTime.Parse(splittedRecord[3])
#                 string departTime = (splittedRecord[4])
#                 int seats = int.Parse(splittedRecord[5])
#                 int price = int.Parse(splittedRecord[6])
#                 string flightClass = (splittedRecord[7])
#                 Flight newFlight = new Flight(departCity, arrCity, tripType, departDate, departTime, seats, price, flightClass)
#                 addFlightIntoList(newFlight)
#
#             f.Close()
#             f = new StreamReader(pathF)
#             while ((record=f.ReadLine()) != null)
#
#                 string[] splittedRecord = record.Split(',')
#                 string departCity = splittedRecord[0]
#                 string arrCity = (splittedRecord[1])
#                 string tripType = (splittedRecord[2])
#                 DateTime departDate = DateTime.Parse(splittedRecord[3])
#                 string departTime = (splittedRecord[4])
#                 int seats = int.Parse(splittedRecord[5])
#                 int price = int.Parse(splittedRecord[6])
#                 string flightClass = (splittedRecord[7])
#                 Flight newFlight = new Flight(departCity, arrCity, tripType, departDate, departTime, seats, price, flightClass)
#                 addReqFlightIntoList(newFlight)
#
#             f.Close()
#             return true
#
#         else
#
#             return false
#
#
#     def storeIntoFile(string path, Flight newFlight)
#

#         StreamWriter f = new StreamWriter(path, true)
#         f.WriteLine(newFlight.DepartCity + "," + newFlight.ArrCity + "," + newFlight.TripType + "," + newFlight.DepartDate +
#                     "," + newFlight.DepartTime + "," + newFlight.Seats + "," + newFlight.Price + "," + newFlight.FlightClass)
#         f.Flush()
#         f.Close()
#
#     def storeReqFlightsIntoFile(string path, Flight newFlight)
#

#         StreamWriter f = new StreamWriter(path, true)
#         f.WriteLine(newFlight.DepartCity + "," + newFlight.ArrCity + "," + newFlight.TripType + "," + newFlight.DepartDate +
#                     "," + newFlight.DepartTime + "," + newFlight.Seats + "," + newFlight.Price + "," + newFlight.FlightClass)
#         f.Flush()
#         f.Close()
#
#     def storeAllFlightsIntoFile(string path, string pathF)
#

#         StreamWriter f = new StreamWriter(path)
#         foreach(var newFlight in FlightsList)
#
#             f.WriteLine(newFlight.DepartCity + "," + newFlight.ArrCity + "," + newFlight.TripType + "," + newFlight.DepartDate +
#                         "," + newFlight.DepartTime + "," + newFlight.Seats + "," + newFlight.Price + "," + newFlight.FlightClass)
#
#         f.Flush()
#         f.Close()
#         f = new StreamWriter(pathF)
#         foreach(var newFlight in RequestedFlightsList)
#
#             f.WriteLine(newFlight.DepartCity + "," + newFlight.ArrCity + "," + newFlight.TripType + "," + newFlight.DepartDate +
#                         "," + newFlight.DepartTime + "," + newFlight.Seats + "," + newFlight.Price + "," + newFlight.FlightClass)
#
#         f.Flush()
#         f.Close()
#
#
