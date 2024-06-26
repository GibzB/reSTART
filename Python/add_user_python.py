import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        
        confirm = username.upper()
        
    os.system("sudo adduser " + username)
