import functools

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def set_average_grade(self):
        avg = functools.reduce(sum, self.scores)    


