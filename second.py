"""Задание № 2. Атрибуты и взаимодействие классов. В квизе к предыдущей лекции мы реализовали возможность выставлять
студентам оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут
делать лекторы? Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса
Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов,
а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент."""


def validate_grade(grade):
    """
    чтобы избежать дублирования кода вынесу в отдельную функцию проверку того,
    что оценка будет находится в диапазоне от 1 до 10.
    """
    return 1 <= grade <= 10


class Student:
    def __init__(self, name, surname, status='Щенок'):
        self.name = name
        self.surname = surname
        self.status = status
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if validate_grade(grade):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
                return f'Вы оценили лекцию на курсе {course} на {grade} из 10 баллов'
            else:
                return "Оцените лекцию от 1 до 10 баллов"
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname, status='HIGHER MIND'):
        self.name = name
        self.surname = surname
        self.status = status
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, status='Инопланетный Гость'):
        super().__init__(name, surname, status)
        self.grades = {}  # словарик для оценок лекторов


class Reviewer(Mentor):
    def __init__(self, name, surname, status='БОГ'):
        super().__init__(name, surname, status)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if validate_grade(grade):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
                return f'Вы ценили работу студента на {grade} из 10 на курсе {course}'
            else:
                return 'Оцените работу студента в диапазоне от 1 до 10'
        else:
            return 'Ошибка'


# Создание студента, лектора и эксперта
student1 = Student('Иван', 'Иванов')
student1.courses_in_progress += ['Python']

lecturer1 = Lecturer('Петра', 'Газеткова', 'просто красотка')
lecturer1.courses_attached += ['Python']

reviewer1 = Reviewer('Сидор', 'Сидоров')
reviewer1.courses_attached += ['Python']

# Эксперт выставляет оценку студенту на курсе
print(reviewer1.rate_hw(student1, 'Python', 8))
print(reviewer1.rate_hw(student1, 'Python', 57))  # Некорректно оценим

# Студент выставляет оценку лектору за лекции
print(student1.rate_lecturer(lecturer1, 'Python', 9))
print(student1.rate_lecturer(lecturer1, 'Python', 28))  # Некорректно оценим

# Проверим результаты
print(f'Оценки студенту: {student1.grades}')
print(f'Оценки лектору: {lecturer1.grades}')

# print(lecturer1.status)
# print(student1.status)
# print(reviewer1.status)
