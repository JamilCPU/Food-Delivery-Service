import User

class Authentication:
    
    __accessToken = ""
    __authLevel = 0

    def setUserID(self, userID):
        self.__userID = userID

    def setUserIP(self, userIP):
        self.__userIP = userIP

    def setUserMacAddr(self, macAddr):
        self.__userMacAddr = macAddr

   

    def checkCredentials(userCredentials, userCredList):
        if(userCredentials[0]==userCredList[userCredentials[0]]):
            return True
        else:
            return False
    
    def userForgotPswrd():
        print("implement user forgot password")

    def rejectUser(User):
        print("implement reject user")
    
    def generateAccessToken(User):
        print("implement generate access token")
        print("set auth level")

    def authenticateUser(self, User, userCredList):

        userCredentials = {User.getUsername(User), User.getPassword(User)}
        credentialsValid = self.checkCredentials(userCredentials, userCredList)
        ##compare database info with username + password
        if(credentialsValid==True):
            self.generateAccessToken(User)
        else:
            self.rejectUser(User)
        