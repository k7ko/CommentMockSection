
class User():

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.lastLoggedInAt = None
        self.isLoggedIn = False

    def isLoggedin(self):
        return self.isLoggedIn

    

class Moderator(User):
    def __init__(self,username,password):
        super().__init__(username,password)

class Admin(Moderator):
    def __init__(self,username,password):
        super().__init__(username,password)
        
