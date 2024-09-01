"""Задание № 4. Полевые испытания"""



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
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) <= calculate_average_grade(other.grades)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) > calculate_average_grade(other.grades)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) >= calculate_average_grade(other.grades)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) == calculate_average_grade(other.grades)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return calculate_average_grade(self.grades) != calculate_average_grade(other.grades)
        return NotImplemented


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
        return NotImplemented  # для обработки случаев, когда сравниваются объекты разных типов

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) <= calculate_average_grade(other.grades)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) > calculate_average_grade(other.grades)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) >= calculate_average_grade(other.grades)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) == calculate_average_grade(other.grades)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return calculate_average_grade(self.grades) != calculate_average_grade(other.grades)
        return NotImplemented


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


# Создание экземпляров классов
student1 = Student('Пол', 'Уокер')
student2 = Student('Быстрый', 'Гонзалес')
lecturer1 = Lecturer('Ольга', 'Лукашенко')
lecturer2 = Lecturer('Владимир', 'Маяковский')

reviewer1 = Reviewer('Николай', 'Баскофф')
reviewer2 = Reviewer('Барак', 'Обама')

# Привязка курсов к студентам и лекторам
student1.courses_in_progress.append('Python')
student2.courses_in_progress.append('Python')
student1.courses_in_progress.append('Git')
student2.courses_in_progress.append('Git')
student1.finished_courses.append('Введение в SQL')
student2.finished_courses.append('Java - основной курс')

lecturer1.courses_attached.append('Python')
lecturer2.courses_attached.append('Git')

reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Git')

# Оценки студентов и лекторов
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student2, 'Git', 8)

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Git', 8)
student2.rate_lecturer(lecturer2, 'Git', 9)

# Вывод информации о студентах, лекторах и ревьюерах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_grade_for_course(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grade_for_course(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0


# Пример использования функций
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_grade_for_course(students, 'Python'):.1f}")
print(f"Средняя оценка за домашние задания по курсу 'Git': {average_grade_for_course(students, 'Git'):.1f}")

print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade_for_course(lecturers, 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу 'Git': {average_lecturer_grade_for_course(lecturers, 'Git'):.1f}")
