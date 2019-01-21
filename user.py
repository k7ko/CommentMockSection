
class User():

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.lastLoggedInAt = None
        self.isLoggedIn = False

    def isLoggedin(self):
        return self.isLoggedIn

    

class Moderator(User):

   pass

class Admin(Moderator):
    pass
        
