class Store:
    __storeID = 0
    __storeLocation = ""
    __storeName = ""
    __categories = [""]

    def getStoreID(self):
        return self.__storeID
    
    def getStoreLocation(self):
        return self.__storeLocation
    
    def getStoreName(self):
        return self.__storeName
    
    def getCategories(self):
        return self.__categories
    
    def setOrderAvailabilityStatus(self, x):
        print("implement set order availability status")

    def changeOrderStatus():
        print("implement change order status")

    def suspendDeliveryDriver():
        print("implement suspend delivery driver")

    def cancelOrder():
        print("implement cancel order")

    def findDriver():
        print("implement find driver")

    