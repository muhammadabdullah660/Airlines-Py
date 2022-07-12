class MUser:
    userName = ""
    userPassword = ""
    userRole = ""

    def __init__(self, *args):
        if len(args) == 3:
            self.userName = args[0]
            self.userPassword = args[1]
            self.userRole = args[2]
        elif len(args) == 2:
            self.userName = args[0]
            self.userPassword = args[1]

    def isAdmin(self):
        if(self.userRole == "Admin" or self.userRole == "admin"):
            return True
        else:
            return False
