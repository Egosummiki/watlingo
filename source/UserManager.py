# Main Package
# Login manager class

# Date: 18/11/2018
# Author: Mikołaj Bednarek

import os
import json
from pathlib import Path
from Manager import AbstractManager
from passlib.hash import pbkdf2_sha256

class UserManager(AbstractManager):

    def verifyPassword(self, userid, password):
        return pbkdf2_sha256.verify(password, self.users[userid]['hash'])

    def addUser(self, username, password):
        hashed = pbkdf2_sha256.hash(password)
        newUser = {'name': username, 'points': 0, 'hash': hashed}
        file = open("{}/users/{}.json".format(self.homeDir, username), "w") 
        file.write(json.JSONEncoder().encode(newUser))
        file.close()
        self.users.append(newUser)

    def removeUser(self, username):
        pass
    
    def __init__(self):
        self.homeDir = str(Path.home()) + "/.watlingo"
        self.users = []

        if os.path.isdir(self.homeDir):

            files = os.listdir(str(Path.home()) + "/.watlingo/users")

            for fileName in files:
                with open("{}/users/{}".format(self.homeDir, fileName), "r") as file:
                    self.users.append(json.loads(file.read()))
        else:
            os.mkdir(self.homeDir)
            os.mkdir(self.homeDir + "/users")

    def __iter__(self):
        return iter(self.users)

    def __next__(self):
        return next(self.users)
