# Main Package
# Login manager class

# Date: 18/11/2018
# Author: Mikołaj Bednarek

import os
import json
from pathlib import Path

class LoginManager:

    users = []
    homeDir = "~"

    def addUser(self, username):
        newUser = {'name': username, 'points': 0}
        file = open("{}/users/{}.json".format(LoginManager.homeDir, username), "w") 
        file.write(json.JSONEncoder().encode(newUser))
        file.close()
        LoginManager.users.append(newUser)


    def removeUser(self, username):
        pass

    
    def __init__(self):
        LoginManager.homeDir = str(Path.home()) + "/.watlingo"

        if os.path.isdir(self.homeDir):

            files = os.listdir(str(Path.home()) + "/.watlingo/users")
            LoginManager.users = []

            for fileName in files:
                file = open("{}/users/{}".format(LoginManager.homeDir, fileName), "r")
                LoginManager.users.append(json.loads(file.read()))
        else:
            os.mkdir(self.homeDir)
            os.mkdir(self.homeDir + "/users")
            LoginManager.users = []

global loginManager
loginManager = LoginManager()
