class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.lecturer_grades:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.aver_stud()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def aver_stud(self):
        count = 0
        countlen = 0
        for value in student.grades.values():
            countlen += len(value)
            for item in value:
                count += item
        return round(count/countlen, 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.lecturer_grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'средняя оценка за лекции: {self.average_rate()}\n')
        return res

    def average_rate(self):
        count = 0
        countlen = 0
        for value in lecturer.grades.values():
            countlen += len(value)
            for item in value:
                count += item
        return round(count / countlen, 2)

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, name, surname):
        self.name = name
        self.surname = surname
        some_reviewer = (f'Имя: {self.name}\n '
                         f'Фамилия: {self.surname}\n')
        return(some_reviewer)

def __eq__(self, other):
    return self.average_rate == other.aver_stud

def __ne__(self, other):
    return self.average_rate != other.aver_stud

# функция подсчета средней оценки за дом/задание по студентам
def grade_homework_students(students, course):
    total_grades = 0
    num_students = 0
    for i in students:
        if student.course == course:
            total_grades += students.grade_homework_students()
            num_students += 1
    return total_grades / num_students

# функция для подсчета средней оценки за лекции у лекторов
def grade_lecturers(lecturers, course):
    total_grades = 0
    num_lecturers = 0
    for i in students:
        if student.course == course:
            total_grades += num_lecturers.grade_lecturers()
            num_lecturers += 1
    return total_grades / num_lecturers





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# берем хороший ревьюр из класса
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# хороший ревьюр выставляет оценки хорошим студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# берем хороший лекчер из класса
best_lecturer = Lecturer('Jeik', 'Tomson')
# хорошие студенты выставляют оценки хорошим лекторам
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)

print(best_student.grades)
print(best_lecturer.grades)
