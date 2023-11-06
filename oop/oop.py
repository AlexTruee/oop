class Student:
    def __init__(self, name, surname, gender):
        self.average = None
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

    def calc_average(self):
        sum_ = 0
        len_ = 0
        for key, value in self.grades.items():
            sum_ += sum(value)
            len_ += len(value)
        average = sum_ / len_
        return average

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.calc_average()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __gt__(self, other):
        return self.calc_average() > other.calc_average()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average(self):
        sum_ = 0
        len_ = 0
        for key, value in self.grades.items():
            sum_ += sum(value)
            len_ += len(value)
        average = sum_ / len_
        return average

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}' \
               f'\nСредняя оценка за лекции: {self.calc_average()}'

    def __gt__(self, other):
        return self.calc_average() > other.calc_average()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка! Проверьте введённые данные'

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}'


def student_rate(students, course_name):
    sum_rate = 0
    count_rate = 0
    for student in students:
        if course_name in student.courses_in_progress:
            sum_rate += sum(student.grades[course_name])
            count_rate += len(student.grades[course_name])
    average = sum_rate / count_rate
    return average


def lecturer_rate(lecturers, course_name):
    sum_rate = 0
    count_rate = 0
    for lecturer in lecturers:
        if course_name in lecturer.courses_attached:
            sum_rate += sum(lecturer.grades[course_name])
            count_rate += len(lecturer.grades[course_name])
    average = sum_rate / count_rate
    return average


some_student = Student('Мария', 'Алексеева ', 'женщина')
second_student = Student('Павел', 'Баранов', 'мужчина')

some_lecturer = Lecturer('Доктор', 'Лектор')
second_lecturer = Lecturer('Энтони', 'Хопкинс')

reviewer = Reviewer('Лада', 'Дэнс')
second_reviewer = Reviewer('Сильвестр', 'Сталонне')

some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']

reviewer.rate_hw(some_student, 'Python', 10)
reviewer.rate_hw(some_student, 'Python', 10)
reviewer.rate_hw(some_student, 'Git', 8)
reviewer.rate_hw(some_student, 'Git', 10)

reviewer.rate_hw(second_student, 'Python', 10)
reviewer.rate_hw(second_student, 'Python', 8)
reviewer.rate_hw(second_student, 'Git', 10)
reviewer.rate_hw(second_student, 'Git', 10)

some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Git', 3)
some_student.rate_lecture(some_lecturer, 'Git', 6)

some_student.rate_lecture(second_lecturer, 'Python', 10)
some_student.rate_lecture(second_lecturer, 'Python', 9)
some_student.rate_lecture(second_lecturer, 'Git', 10)
some_student.rate_lecture(second_lecturer, 'Git', 10)

# Создаем списки для расчета средней оценки студентов и лекторов
student_list = [some_student, second_student]
lecturer_list = [some_lecturer, second_lecturer]


print(some_student)
print(second_student)
print(some_lecturer)
print(second_lecturer)
print(some_lecturer > second_lecturer)
print(f"Средняя оценка для всех студентов: {student_rate(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов: {lecturer_rate(lecturer_list, 'Python')}")
