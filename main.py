class Human:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}

    def avg_grade(self):
        all_of_grades = []
        for value in self.grades.values():
            all_of_grades += value
        sum_of_grades = sum(all_of_grades)
        len_of_grades = len(all_of_grades)
        if sum_of_grades != 0:
            avg = sum_of_grades / len_of_grades
            return avg
        else:
            return 0

    def __lt__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() >= other.avg_grade()

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return self.avg_grade() != other.avg_grade()


class Student(Human):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached and course in self.courses_in_progress:
                lecturer.grades[course] = list(grade)
            else:
                print(f'Лектор {lecturer} должен вести курс {course}, а студент {self.name}, изучать его в'
                      f' настоящий момент!')
        else:
            print('Неверный тип объекта!')

    def __str__(self):
        avg_string = f'Средняя оценка за домашние задания: {self.avg_grade()}'
        courses_string = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}'
        finished = f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return f'{self.name} {self.surname}\n{avg_string}\n{courses_string}\n{finished}'


class Mentor(Human):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.courses_attached = []

    def __str__(self):
        response = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return response


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.courses_in_progress:
                student.grades[course] = list(grade)
            else:
                print(f'Cтудент {student.name} не изучает курс {course}!')
        else:
            print('Неверный тип объекта!')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_for_students(students, course):
    all_grades = []
    for student in students:
        if isinstance(student, Student):
            if course in student.courses_in_progress:
                all_grades += student.grades[course]
    return f'Средняя оценка на курсе "{course}" для студентов: ' + str(sum(all_grades) / len(all_grades))


def avg_for_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached:
                all_grades += lecturer.grades[course]
    return f'Средняя оценка на курсе "{course}" для лекторов: ' + str(sum(all_grades) / len(all_grades))


student_1 = Student('student_1', 'ssur1', 'male')
student_1.add_finished_courses('Введение в программирование')
student_1.courses_in_progress += ['Python', 'Git', 'JavaScript']

student_2 = Student('student_2', 'ssur2', 'male')
student_2.add_finished_courses('Python')
student_2.courses_in_progress += ['Java', 'JavaScript']

reviewer_1 = Reviewer('reviewer_1', 'rsur1', 'female')
reviewer_1.courses_attached.append('Введение в программирование')
reviewer_1.courses_attached.append('Python')

reviewer_2 = Reviewer('reviewer_2', 'rsur2', 'female')
reviewer_2.courses_attached.append('JavaScript')
reviewer_2.courses_attached.append('Java')

lecturer_1 = Lecturer('lecturer_1', 'lsur1', 'It')
lecturer_1.courses_attached += ['Введение в программирование', 'Python', 'Java']

lecturer_2 = Lecturer('lecturer_2', 'lsur2', 'It')
lecturer_2.courses_attached += ['Java', 'JavaScript', 'Git']

reviewer_1.rate_hw(student_1, 'Python', (10, 10, 10, 10, 10, 10, 10, 10, 10, 9))
reviewer_2.rate_hw(student_2, 'JavaScript', (5, 10, 10, 10, 10, 10, 10, 10, 10, 9))

student_1.rate_hw(lecturer_1, 'Python', (4, 5, 6))
student_2.rate_hw(lecturer_2, 'JavaScript', (10, 7, 9))

print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

print(avg_for_students((student_2, student_1),  'Python'))
print(avg_for_lecturers((lecturer_2, lecturer_1),  'JavaScript'))

print(lecturer_2 == lecturer_1)
print(student_2 < student_1)
print(student_1 > student_2)
print(lecturer_1 != lecturer_2)





