class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка! Проверьте введенные данные'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка! Проверьте введенные данные'


best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_lector = Lecturer('Cool', 'Lector')
best_student.courses_in_progress += ['Python']
cool_lector.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecture(cool_lector, 'Python', 10)
best_student.rate_lecture(cool_lector, 'Python', 10)
print(best_student.grades)
print(cool_lector.grades)