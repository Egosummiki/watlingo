import json

class LessonManager:

    def __init__(self, courseData):
    
        self.name = courseData['name']
        self.plain = courseData['plain']
        self.lessonsFiles = courseData['lessons']
        self.lessons = []

        for f in self.lessonsFiles:
            with open("courses/{}/lessons/{}".format(self.plain, f)) as file:
                self.lessons.append(json.loads(file.read()))

    def __iter__(self):
        return iter(self.lessons)

    def __next__(self):
        return next(self.lessons)

    def __getitem__(self, pos):
        return self.lessons[pos]
