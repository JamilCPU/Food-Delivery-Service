class Driver:
    __driverID = 0
    __driverfName = ""
    __driverlName = ""
    __canTakeOrder = False
    __ordersInProgress = 0

    def getDriverID(self):
        return self.__driverID
    
    def getDriverfName(self):
        return self.__driverfName
    
    def getDriverlName(self):
        return self.__driverlName
    
    def getCanTakeOrder(self):
        return self.__canTakeorder
    
    def getOrdersInProgress(self):
        return self.ordersInProgress
    
    def setDriverName(self, fName, lName):
        self.__driverfName, __driverlName = fName, lName

    def beginTakingOrders(self):
        self.__canTakeOrder = True
    
    def dropOrder():
        print("implement drop order")

    