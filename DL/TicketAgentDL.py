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
            if userX.userName == item.id.userName and userX.userPassword == item.id.userPassword:
                return item
        return None
