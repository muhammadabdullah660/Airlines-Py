from collections import UserList
import os.path
from BL.MUser import MUser
from BL.Passenger import Passenger
from time import sleep

from DL.MUserDL import MUserDL


class PassengerDL:
    passengersList = []
    sortedPassengersList = []

    @staticmethod
    def addPassengerIntoList(p):
        PassengerDL.passengersList.append(p)

    @staticmethod
    def sortPassengersByTotal():
        for p in PassengerDL.passengersList:
            p.calculateTotal()

        PassengerDL.sortedPassengersList = PassengerDL.passengersList.sort(
            key=lambda x: x.get('total'), reverse=True)

    @staticmethod
    def isValidPassenger(userX):
        for item in PassengerDL.passengersList:
            if userX.UserName == item.UserName and userX.UserPassword == item.UserPassword:
                return item
        return None

#     public static void storeIntoFile(string path, Passenger p)
#     {
#         StreamWriter f = new StreamWriter(path, true)
#         string flights = ""
#         for (int i=0
#              i < p.MyFlights.Count
#              i++)
#         {
#             if (i != p.MyFlights.Count - 1)
#             {
#                 flights += p.MyFlights[i].DepartCity + "^" + p.MyFlights[i].ArrCity + "^" +
#                 p.MyFlights[i].TripType + "^" + p.MyFlights[i].DepartDate +
#                 "^" + p.MyFlights[i].Price + ";"
#             }
#             else
#             {
#                 flights += p.MyFlights[i].DepartCity + "^" + p.MyFlights[i].ArrCity + "^" +
#                 p.MyFlights[i].TripType + "^" +
#                 p.MyFlights[i].DepartDate + "^" + p.MyFlights[i].Price
#             }
#         }

#         f.WriteLine(p.UserName + "," + p.UserPassword + "," + p.UserRole + ","
#                     + p.Name + "," + p.PassportNo + "," + p.Cnic + "," +
#                     p.EMail + "," + p.Gender + "," + p.ContactNum + "," +
#                     +p.Total + "," +
#                     flights)

#         f.Flush()
#         f.Close()
#     }
#     public static void storeAllIntoFile(string path)
#     {
#         StreamWriter f = new StreamWriter(path)

#         foreach(var p in PassengersList)
#         {
#             string flights = ""
#             for (int i=0
#                  i < p.MyFlights.Count
#                  i++)
#             {
#                 if (i != p.MyFlights.Count - 1)
#                 {
#                     flights += p.MyFlights[i].DepartCity + "^" + p.MyFlights[i].ArrCity + "^" +
#                     p.MyFlights[i].TripType + "^" + p.MyFlights[i].DepartDate +
#                     "^" + p.MyFlights[i].Price + ";"
#                 }
#                 else
#                 {
#                     flights += p.MyFlights[i].DepartCity + "^" + p.MyFlights[i].ArrCity + "^" +
#                     p.MyFlights[i].TripType + "^" +
#                     p.MyFlights[i].DepartDate + "^" + p.MyFlights[i].Price
#                 }
#             }

#             f.WriteLine(p.UserName + "," + p.UserPassword + "," + p.UserRole + ","
#                         + p.Name + "," + p.PassportNo + "," + p.Cnic + "," +
#                         p.EMail + "," + p.Gender + "," + p.ContactNum + "," +
#                         +p.Total + "," +
#                         flights)
#         }
#         f.Flush()
#         f.Close()
#     }
#     public static bool loadFromFile(string path)
#     {
#         StreamReader f = new StreamReader(path)
#         string record
#         if (File.Exists(path))
#         {
#             while ((record=f.ReadLine()) != null)
#             {
#                 string[] splittedRecord = record.Split(',')
#                 Passenger p = new Passenger()

#                 p.UserName = splittedRecord[0]
#                 p.UserPassword = (splittedRecord[1])
#                 p.UserRole = (splittedRecord[2])
#                 p.Name = (splittedRecord[3])
#                 p.PassportNo = (splittedRecord[4])
#                 p.Cnic = (splittedRecord[5])
#                 p.EMail = (splittedRecord[6])
#                 p.Gender = (splittedRecord[7])
#                 p.ContactNum = (splittedRecord[8])
#                 p.Total = double.Parse(splittedRecord[9])
#                 string[] splittedRecordFlight = splittedRecord[10].Split(';')
#                 if (splittedRecord[10] != "")
#                 {
#                     for (int i=0
#                          i < splittedRecordFlight.Length
#                          i++)
#                     {
#                         string[] splittedRecordx = splittedRecordFlight[i].Split('^')

#                         Flight newFlight = new Flight(splittedRecordx[0], splittedRecordx[1], splittedRecordx[2], DateTime.Parse(splittedRecordx[3]))
#                         Flight myFlight = FlightDL.checkFlight(newFlight)
#                         if (myFlight != null)
#                         {
#                             myFlight.Price = double.Parse(
#                                 splittedRecordx[4])
#                             p.bookFlight(myFlight)
#                         }

#                     }
#                 }
#                 else if (splittedRecord[10] == "")
#                 {
#                     continue
#                 }

#                 addPassengerIntoList(p)
#             }
#             f.Close()
#             return true
#         }
#         else
#         {
#             return false
#         }
#     }


# }
