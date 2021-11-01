from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def is_finished(self, course):
        for course_st in self.courses_in_progress:
            if course in self.grades.keys():
                self.finished_courses.append(course)



    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in Lecturer.courses_attached:
            if course in lecturer.stud_grades.keys():
                lecturer.stud_grades[course] += [grade]
            else:
                lecturer.stud_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mean_grades_st(self):
        sum = 0
        for grade in self.grades.values():
            sum += grade
        mean_gr = sum/len(self.grades.values())
        return mean_gr



    def __Str__(self, some_student):
        inpr_crs=",".join(Student.courses_in_progress)
        fin_crs=",".join(Student.finished_courses)
        if isinstance(some_student, Student):    
                return f'Имя: {self.name} \nФамилия: {self.surname} \n \
                Средняя оценка за домашние задания: {print(Student._mean_grades_st())} \n \
                Курсы в процессе: {inpr_crs}\n \
                Завершенные курсы: {fin_crs} '

    def __lt__(self, other_student): 
	# сравнение студентов по средней оценке между собой self < other
        if not isinstance(other_student, Student):
            print('Not a Student!')
        else:
            mean_other = mean(int(other_student.grades.values()) for course in other_student.grades.keys())
            self_mean = mean(int(Student.grades.values()) for course in Student.grades.keys())    
        return self_mean < mean_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):   
    stud_grades = {}
    courses_attached = []

    
    def _mean_grades_lect(self):
        sum = 0    
        for grade in self.stud_grades.values():
            sum += grade
        mean_gr = sum/len(self.stud_grades.values())
        return mean_gr

    def __Str__(self, some_lecturer):
        return f"Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка: {self._mean_grades_lect(some_lecturer)}"
    
    
    def __lt__(self, other_lecturer): 
	# сравнение лекторов по средней оценке между собой self < other
        if not isinstance(other_lecturer, Lecturer):
            print('Not a Lecturer!')
        else:
            mean_other = mean(int(other_lecturer.stud_grades[course]) for course in other_lecturer.stud_grades.keys())
            self_mean = mean(int(Lecturer.stud_grades[course]) for course in Lecturer.stud_grades.keys())    
        return self_mean < mean_other
       

class Reviewer(Mentor):
    courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    
    def __Str__(self, reviewer):
        if isinstance(reviewer, Reviewer):
            return f'Имя: {reviewer.name} \n Фамилия: {reviewer.surname}'
    

 

# создаем объекты классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

new_student_1 = Student("Axel", "Rose", "Man")
new_student_1.courses_in_progress += ['Ruby']

new_student_2 = Student("Blackie", "Lawless", "Man")
new_student_2.courses_in_progress += ['C#']

new_student_3 = Student("Blackie", "Lawless", "Man")
new_student_3.courses_in_progress += ['Java']


cool_reviewer = Reviewer('Craig', 'Richie')
cool_reviewer.courses_attached += ['Python']

another_reviewer = Reviewer('Tim', "Rush")
another_reviewer.courses_attached += ['Java']

another_reviewer_2 = Reviewer('Frank', "Zappa")
another_reviewer_2.courses_attached += ['C#']



cool_lecturer = Lecturer('George', 'Best')
cool_lecturer.courses_attached += ['Python']

new_lecturer = Lecturer('Andy', "Johnson")
new_lecturer.courses_attached += ['Ruby']

new_lecturer_2 = Lecturer('Bruce', "Stevenson")
new_lecturer_2.courses_attached += ['C#']


# создаем списки и зобъектов классов
students_list = [best_student, new_student_1, new_student_2, new_student_3]
lecturers_list = [cool_lecturer, new_lecturer, new_lecturer_2]


#  СОздаем функции для рассчета средних оценок 
def mean_grade_lect(lect_list, course_name):
    sum_grades = 0
    for lect in lect_list:
        if course_name in Lecturer.stud_grades.keys():
            sum_grades += int(Lecturer.stud_grades[course_name])
    return mean(sum_grades)


def mean_grade_stud(stud_list, course_name):
    sum_grades_st = 0
    for stud in stud_list:
        if course_name in Student.grades.keys():
            sum_grades_st += int(Student.grades[course_name])
    return mean(sum_grades_st)

#Вызываем все методы
cool_reviewer.rate_hw(best_student, 'Python', 8)
another_reviewer.rate_hw(new_student_3, 'Python', 7)
another_reviewer_2.rate_hw(new_student_2, 'C#', 10)


best_student.rate_lect(cool_lecturer, 'Python', 9)
new_student_1.rate_lect(new_lecturer, 'Ruby', 7)
new_student_2.rate_lect(new_lecturer_2, 'C#', 6)
 

# Сравнение между собой
print(best_student.__lt__(new_student_1))
print(cool_lecturer.__lt__(new_lecturer))


# Перегрузка метода STR
print(cool_reviewer)
print(cool_lecturer)
print(best_student)


# запуск функций рассчета средних
print(mean_grade_stud(students_list, "Python"))
print(mean_grade_lect(lecturers_list, "Ruby"))
