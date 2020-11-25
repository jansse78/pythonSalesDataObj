class DataContainer():

    def __init__(self):
        self.container = []
        self.placeHolder = 0

    def containerSize(self):
        return len(self.container)

    def addToContainer(self, dataRow):
        self.container.append(dataRow)

    def returnContainerValue(self,i):
        return self.container[i]

    def returnContainer(self):
        return self.container

    def sort_container(self):
        self.container.sort(key=lambda x:x.orderID)

    def findDataRows(self, arrValuesToFind):
        returningArray = []
        notFound = 0
        found = 0

        for i in range(len(arrValuesToFind)):
            valPosition = self.findValue(arrValuesToFind[i])
            if (valPosition != -1):
                returningArray.append(self.container[valPosition])
                found += 1
            else:
                returningArray.append(f'orderID:{valPosition} ei löydy')
                notFound += 1

        return returningArray

    def findValue(self, val):
        middle = -1
        begin = 0
        end = self.containerSize() - 1

        while begin <= end:
            middle = (begin + end) // 2

            if (val < self.container[middle].orderID):
                end = middle - 1
            elif (val > self.container[middle].orderID):
                begin = middle + 1
            else:
                return middle

        return -1

    def gatherRandom(self, amount):
        import random as rand

        returningArray = []
        upperLimit = self.containerSize() - 1

        for i in range(amount):
            fetchValue = rand.randint(0, upperLimit)
            returningArray.append(self.container[fetchValue].orderID)

        return returningArray

