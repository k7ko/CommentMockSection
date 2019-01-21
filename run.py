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
if __name__=="__main__":
    signup("Patrick","password123")