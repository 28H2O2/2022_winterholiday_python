class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print(bart.age, bart.get_grade())