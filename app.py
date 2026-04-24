class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print(f"{self.name} -> O‘rtacha: {self.average():.2f}")


# Test
s = Student("Ali")
s.add_grade(5)
s.add_grade(4)
s.add_grade(3)

s.show_info()
