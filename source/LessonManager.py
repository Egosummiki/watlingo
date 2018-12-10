
class LessonManager:

    def __init__(self, course):
        self.course = course

    def __iter__(self):
        return iter(self.course['lessons'])

    def __next__(self):
        return next(self.course['lessons'])
