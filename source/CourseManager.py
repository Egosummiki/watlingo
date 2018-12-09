from Manager import AbstractManager 
from LessonManager import LessonManager
import os
import json

class CourseManager(AbstractManager):

    def getLessonManager(self, id):
        return LessonManager(self.courses[id])

    def __init__(self):
        self.courses = []
        files = os.listdir("./courses")
        for filename in files:
            with open("./courses/{}/manifest.json".format(filename), "r") as file:
                self.courses.append(json.loads(file.read()))
        print("Hello!")

