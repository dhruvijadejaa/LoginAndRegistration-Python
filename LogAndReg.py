####################################
#  Python Login Validation System  #
#        By coolhobo77             #
####################################

# This module aims to provide a clear layout for a login system based in Python
# This module is not over-complicated and very straightforward to use!
# This is a way for beginners to look into modules and see how they work

# Defines an Array that Contains Every Instantiated User Class added
# LogAndReg.py

totalUsers = []

class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        totalUsers.append(self)

def createUser(name, surname, email, password):
    return User(name, surname, email, password)

def userExists(email, password):
    for user in totalUsers:
        if user.email == email and user.password == password:
            return True
    return False

def emailAlreadyExists(email):
    for user in totalUsers:
        if user.email == email:
            return True
    return False

def listUsers():
    return [
        {
            "name": user.name,
            "surname": user.surname,
            "email": user.email
        }
        for user in totalUsers
    ]

def removeUser(email):
    global totalUsers
    totalUsers = [user for user in totalUsers if user.email != email]
    return True
