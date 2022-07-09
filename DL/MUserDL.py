from collections import UserList
import os.path
from BL.MUser import MUser
from time import sleep


class MUserDL:
    userList = []

    @staticmethod
    def addUserInList(user):
        MUserDL.userList.append(user)

    @staticmethod
    def signIn(user):
        for storedUser in MUserDL.userList:

           # print(user.userName)
           # print(storedUser.userName)
           # sleep(10)
            if(storedUser.userName == user.userName and storedUser.userPassword == user.userPassword):
                return storedUser
            else:
                return None

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readDataFromFile(path):
        if(os.path.exists(path)):
            f = open(path, 'r')
            records = f.read().split("\n")
            f.close()
            for line in records:
                userName, userPassword, userRole = MUserDL.parseData(line)
                user = MUser(userName, userPassword, userRole)
                print(user.userName, userPassword)
                sleep(10)
                MUserDL.addUserInList(user)

            return True
        else:
            return False

    @staticmethod
    def storeDataInFile(user, path):
        file = open(path, "a")
        file.write("\n"+user.userName+","+user.userPassword+","+user.userRole)
        file.close()
