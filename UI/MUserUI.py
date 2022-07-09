from BL.MUser import MUser


class MUserUI:
    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignUp")
        print("3. Exit")
        print("3. Enter Your Option")
        option = int(input())
        return option

    @staticmethod
    def printList(userList):
        for user in userList:
            print(user.userName, user.userPassword, user.userRole)

    @staticmethod
    def TakeInputFromConsole():
        userName = input("Enter Your Name:")
        userPassword = input("Enter Your Password:")
        userRole = input("Enter Your Role:")
        user = MUser(userName, userPassword, userRole)
        return user

    @staticmethod
    def TakeInputWithOutRole():
        userName = input("Enter Your Name:")
        userPassword = input("Enter Your Password:")
        user = MUser(userName, userPassword)
        return user
