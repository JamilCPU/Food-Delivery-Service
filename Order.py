import Store

class Order:
    __orderID = 0
    __orderStore = Store
    __orderItems = [""]
    __orderPrice = 0.00

    def getOrderItemsself(self):
        return self.__orderItems
    
    def getOrderPrice(self):
        return self.__orderPrice
    
    def setOrderItems(self, orderItems):
        self.__orderItems = orderItems
    
    def setOrderPrice(self, orderPrice):
        self.__orderPrice=orderPrice #re-evaluate

        def __init__(self):
            self.__orderID = 1
            self.__orderStore = Store