# Main Package
# Login manager class

# Date: 18/11/2018
# Author: Mikołaj Bednarek

import os
from pathlib import Path

class LoginManager:
    
    def __init__(self):
        
        print("Creating login manager")

        self.homeDir = str(Path.home()) + "/.watlingo"

        if os.path.isdir(self.homeDir):

            dirs = os.listdir(str(Path.home()) + "/.watlingo/users")
            self.users = []

            for dirName in dirs:
                self.users.append(dirName[:dirName.index(".")])
        else:
            os.mkdir(self.homeDir)
            os.mkdir(self.homeDir + "/users")
            self.users = []

global loginManager
loginManager = LoginManager()
