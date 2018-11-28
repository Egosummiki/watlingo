from Manager import AbstractManager 
import os
import json

class CourseManager(AbstractManager):

    def __init__(self):
        self.courses = []
        files = os.listdir("./courses")
        for filename in files:
            file = open("./courses/{}/manifest.json".format(filename), "r")
            self.courses.append(json.loads(file.read()))
        print("Hello!")

