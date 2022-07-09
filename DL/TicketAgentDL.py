from BL.MUser import MUser
from BL.TicketAgent import TicketAgent
from time import sleep


class TicketAgentDL:
    ticketAgentList = []

    @staticmethod
    def addTicketAgentIntoList(p):
        TicketAgentDL.ticketAgentList.append(p)

    @staticmethod
    def isValidTicketAgent(userX):
        for item in TicketAgentDL.ticketAgentList:
            if userX.UserName == item.UserName and userX.UserPassword == item.UserPassword:
                return item
        return None
