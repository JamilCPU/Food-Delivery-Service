import User

class Account:
    
    __accID=0
    __cardNum = 000000000
    __address = ""
    __birthDate = ""

    def __init__(self, user):
        self.user = User(user)



    def setCardNum(self, cardNum):
        self.__cardNum = cardNum

    def setName(self, name):
        self.__name = name

    def setPhoneNumber(self, phoneNum):
        self.__phoneNum = phoneNum

    def setAddress(self, address):
        self.__address = address

    def getAccID(self):
        return self.__accID

    def getCardNum(self):
        return self.__cardNum
    
    def getNameself(self):
        return self.__fName
    
    def getAddress(self):
        return self.__address
    
    def getBirthDate(self):
        return self.__birthDate
    
    def addTip():
        print("implement add tip")

    def cancelDelivery():
        print("implement cancel delivery")
    
    def changeDefaultStore():
        print("change default store")
    
    def showOrderHistory():
        print("implement show order history")
    
    def placeOrder():
        print("implement place order")

    def selectStore():
        print("implement select store")

    