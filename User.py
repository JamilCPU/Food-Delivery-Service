class User:##inner class of Account
    __username=""
    __password=""
    __fName=""
    __lName=""
    __phoneNum=0000000
    __email = ""
    __userID = 000000000000000
    __userIP = ""
    __userMacAddr = ""

    def setUsername(self, user):
        self.__username = user
        
    def setPassword(self, password):
        self.__password = password

    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    
    def setEmail(self, email):
        self.__email = email

    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    def getfName(self):
        return self.__fName
    
    def getlName(self):
        return self.__lName
    
    def getphoneNum(self):
        return self.__phoneNum
    
    def getEmail(self):
        return self.__email
    

    

    

    def forgotPassword():
        print("implement forgot password")

    def createAccount():
        print("implement create account")
    
    def changeCountry():
        print("implement change country")

    def __init__(self, username, password, fName, lName, phoneNum, email):
        self.__username = username
        self.__password = password
        self.__fName = fName
        self.__lName = lName
        self.__phoneNum = phoneNum
        self.__email =  email
      
