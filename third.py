"""Задание № 3. Полиморфизм и магические методы"""


def validate_grade(grade):
    """
    функция для проверки корректности введенной оценки (вынесена для избегания дублирования кода)
    """
    return 1 <= grade <= 10


def calculate_average_grade(grades):
    """
    функцию для расчета средней оценки (вынесена для избегания дублирования кода)
    """
    total_grades = []
    for grade_list in grades.values():
        total_grades.extend(grade_list)
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0


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

    def __str__(self):
        average_grade = calculate_average_grade(self.grades)
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) < calculate_average_grade(other.grades)
        return NotImplemented  # для обработки случаев, когда сравниваются объекты разных типов

    def __eq__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) == calculate_average_grade(other.grades)
        return NotImplemented

   # # взаимоисключающие методы закомментированы
   # def __le__(self, other):
    #     if isinstance(other, Student):
    #         return calculate_average_grade(self.grades) <= calculate_average_grade(other.grades)
    #     return NotImplemented
    #
    # def __gt__(self, other):
    #     if isinstance(other, Student):
    #         return calculate_average_grade(self.grades) > calculate_average_grade(other.grades)
    #     return NotImplemented
    #
    # def __ge__(self, other):
    #     if isinstance(other, Student):
    #         return calculate_average_grade(self.grades) >= calculate_average_grade(other.grades)
    #     return NotImplemented

    # def __ne__(self, other):
    #     if isinstance(other, Student):
    #         return calculate_average_grade(self.grades) != calculate_average_grade(other.grades)
    #     return NotImplemented

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

    def __str__(self):
        average_grade = calculate_average_grade(self.grades)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) < calculate_average_grade(other.grades)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) == calculate_average_grade(other.grades)
        return NotImplemented

    ## взаимоисключающие методы закомментированы
    # def __le__(self, other):
    #     if isinstance(other, Lecturer):
    #         return calculate_average_grade(self.grades) <= calculate_average_grade(other.grades)
    #     return NotImplemented
    #
    # def __gt__(self, other):
    #     if isinstance(other, Lecturer):
    #         return calculate_average_grade(self.grades) > calculate_average_grade(other.grades)
    #     return NotImplemented
    #
    # def __ge__(self, other):
    #     if isinstance(other, Lecturer):
    #         return calculate_average_grade(self.grades) >= calculate_average_grade(other.grades)
    #     return NotImplemented

    # def __ne__(self, other):
    #     if isinstance(other, Lecturer):
    #         return calculate_average_grade(self.grades) != calculate_average_grade(other.grades)
    #     return NotImplemented

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

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Создание студента, лектора и эксперта
student1 = Student('Джордж', 'Мартин')
student1.courses_in_progress += ['Python', 'Java', 'Django']
student1.finished_courses += ['TCP/IP — Сетевое администрирование', 'Python для Excel']

student2 = Student('Анна', 'Чапмэн')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Оптимизация запросов в PostgreSQL']

lecturer1 = Lecturer('Петра', 'Газеткова', 'просто красотка')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Инна', 'Друзь', 'умная женщина')
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Егор', 'Просвирин')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']
reviewer1.courses_attached += ['Django']
reviewer1.rate_hw(student1, 'Java', 8)
reviewer1.rate_hw(student1, 'Python', 10)


# Оценка лекторов студентами
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Git', 7)

# Оценка студентов экспертом
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Git', 7)
reviewer1.rate_hw(student2, 'Python', 6)

# Сравнение студентов и лекторов
print(student1 > student2)  # True, если средняя оценка student1 больше, чем у student2
print(lecturer1 < lecturer2)  # True, если средняя оценка lecturer1 меньше, чем у lecturer2

# Вывод информации о студентах и лекторах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

