
import re

class Input:
    def __init__(self, ticketFields, yourTicket, allTickets):
        self.ticketFields = ticketFields
        self.yourTicket = yourTicket
        self.allTickets = allTickets

class TicketField:
    def __init__(self, name, range1, range2):
        self.name = name
        self.range1 = range1
        self.range2 = range2
        self.used = 0

class Ticket:
    def __init__(self, fieldValues):
        self.fieldValues = fieldValues

def GetInput(strFile):
    ticketFields = []
    yourTicket = []
    allTickets = []
    readingFields = True
    with open(strFile) as f:
        for line in f:
            if line == '\n':
                readingFields = False
            elif readingFields:
                lineParsed = re.match("(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
                ticketFields.append(TicketField(lineParsed[1], (int(lineParsed[2]), int(lineParsed[3])), (int(lineParsed[4]), int(lineParsed[5]))))
            else:
                allTickets.append([int(n) for n in line.split(',')])
                if (len(allTickets) == 1):
                    yourTicket = allTickets[0]
    return Input(ticketFields, yourTicket, allTickets)

def IsValidValueForTicketField(val, ticketField):
    return (val >= ticketField.range1[0] and val <= ticketField.range1[1]) or (val >= ticketField.range2[0] and val <= ticketField.range2[1])

def GetInvalidValues(input):
    invalidValues = []
    for ticket in input.allTickets:
        for val in ticket:
            foundValidRange = False
            for ticketField in input.ticketFields:
                if IsValidValueForTicketField(val, ticketField):
                    foundValidRange = True
                    break
            if not foundValidRange:
                invalidValues.append(val)
    return invalidValues

def RemoveInvalidTickets(input):
    allTicketsValid = []
    for ticket in input.allTickets:
        isValidTicket = True
        for val in ticket:
            foundValidRange = False
            for ticketField in input.ticketFields:
                if IsValidValueForTicketField(val, ticketField):
                    foundValidRange = True
                    break
            if not foundValidRange:
                isValidTicket = False
                break
        if isValidTicket:
            allTicketsValid.append(ticket)         
    input.allTickets = allTicketsValid

def GetValidTicketFieldOrder(validTicketFieldsPerIndex):
    validTicketFieldOrder = []
    for validTicketFields in validTicketFieldsPerIndex:
        if (len(validTicketFields) != 1):
            return None
        else:
            validTicketFieldOrder.append(validTicketFields[0])
    return validTicketFieldOrder

def GetCorrectTicketFieldOrder(input):
    validTicketFieldsPerIndex = []
    for fieldIndex in range(len(input.yourTicket)):
        validTicketFieldsPerIndex.append([])
        for ticketField in input.ticketFields:
            isValidForAllTickets = True
            for ticket in input.allTickets:
                if not IsValidValueForTicketField(ticket[fieldIndex], ticketField):
                    isValidForAllTickets = False
                    break
            if isValidForAllTickets:
                validTicketFieldsPerIndex[fieldIndex].append(ticketField)
                ticketField.used += 1
    validTicketFieldOrder = None
    while validTicketFieldOrder == None:
        for validTicketFields in validTicketFieldsPerIndex:
            if len(validTicketFields) == 1 and validTicketFields[0].used > 1:
                validTicketField = validTicketFields[0]
                for validTicketFieldsOther in validTicketFieldsPerIndex: 
                    if validTicketFields != validTicketFieldsOther:
                        try:
                            validTicketFieldsOther.remove(validTicketField)
                            validTicketField.used -= 1
                        except ValueError:
                            pass
        validTicketFieldOrder = GetValidTicketFieldOrder(validTicketFieldsPerIndex)
    return validTicketFieldOrder

def SumFromList(list):
    sum = 0
    for e in list:
        sum += e
    return sum

def ProductFromList(list):
    product = 1
    for e in list:
        product *= e
    return product

def GetDepartureValues(ticketFieldsOrdered, ticket):
    departureValues = []
    for fieldIndex in range(len(ticketFieldsOrdered)):
        ticketField = ticketFieldsOrdered[fieldIndex]
        if 'departure' in ticketField.name:
            departureValues.append(ticket[fieldIndex])
    return departureValues

def Main(strFile):
    input = GetInput(strFile)
    print(SumFromList(GetInvalidValues(input)))
    RemoveInvalidTickets(input)
    ticketFieldsOrdered = GetCorrectTicketFieldOrder(input)
    print(ProductFromList(GetDepartureValues(ticketFieldsOrdered, input.yourTicket)))

Main('2020/input/day_16.txt')