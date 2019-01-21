from user import User
users = []

from datetime import datetime


def signup(username,password):
    
    if not username or not password:
        print("provide Both username and password")
    
    for user in users:
        if user.username == username:
            print("user already exists")
            break
    new_user_obj = User(username=username, password=password)
    users.append(new_user_obj)
    print("Successfully signed up account")

def login(username,password):
    """Logs in user"""
    is_valid_user = None
    for user in users:

        if user.username == username and user.password == password:
            user.isLoggedIn = True
            user.lastLoggedInAt = datetime.now()
            is_valid_user = user.username
            break
    if is_valid_user:
        print(f"Welcome {user.username}")
    else:
        print("Invalid credentials")

    
    
if __name__=="__main__":
    signup("Patrick","password123")
    login("Patrick","password123")
