
class unitData():

    def __init__(self, itemType, unitPrice, unitCost, unitsSold):
        self.itemType = itemType
        self.unitPrice = unitPrice
        self.unitCost = unitCost
        self.unitsSold = unitsSold

class financialTotal():

    def __init__(self, totalRevenue, totalCost, totalProfit):
        self.totalRevenue = totalRevenue
        self.totalCost = totalCost
        self.totalProfit = totalProfit

class dataLocation():

    def __init__ (self, region, country):
        self.region = region
        self.country = country

class DataRow():
    def __init__(self, salesChannel, orderPriority, orderDate, orderID, shipDate, location, unit, financial):
        self.salesChannel = salesChannel
        self.orderPriority = orderPriority
        self.orderDate = orderDate
        self.orderID = int(orderID)
        self.shipDate = shipDate
        self.location = location
        self.unit = unit
        self.financial = financial

    def toString(self):
        return f'{self.orderID}\t{self.orderDate}'

    def __repr__(self):
        return f'{self.orderID} {self.unit}'

    def __str__(self):
        return f'{self.orderID}\t{self.orderDate}'
    
    #def toJson(self):
    #    return json.dumps(self,default=lambda o: o.__dict__)

from json import JSONEncoder

class DataEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__