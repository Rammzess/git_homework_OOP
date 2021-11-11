class Student:
    stud_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.stud_list.append(self) #добавляем объекты класса в список

# Функция для оценки лекторов студентами
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
            and course in self.courses_in_progress or self.finished_courses:
            #  and course in lecturer.courses_in_progress
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функция для рассчета средней оценки студента за все его предметы       
    def _stud_mean_hw_grade(self, name, surname):
        if name == self.name and surname == self.surname:
            sum_grades = 0
            sum_elements = 0
            for gradelist in self.grades.values():  
                sum_grades += sum(gradelist)
                sum_elements +=len(gradelist)
        mean_grade = sum_grades / sum_elements
        return mean_grade
     
    #Перегрузка метода строки    
    def __str__(self):
        crs_in_pr = ",".join(self.courses_in_progress)
        crs_fin = ",".join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\
            \nСредняя оценка за домашние задания: {self._stud_mean_hw_grade(self.name, self.surname)}\
            \nКурсы в процессе изучения: {crs_in_pr}\nЗавершенные курсы: {crs_fin}\n'''
    
    
    #сравнение студентов по средней оценке 
    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            self.stud_one = self._stud_mean_hw_grade(self.name, self.surname)
            other_student = other_student._stud_mean_hw_grade(other_student.name, other_student.surname)
        return self.stud_one < other_student
    
    def __gt__(self, other_student):
        if isinstance(other_student, Student):
            self.stud_one = self._stud_mean_hw_grade(self.name, self.surname)
            other_student = other_student._stud_mean_hw_grade(other_student.name, other_student.surname)
        return self.stud_one > other_student
    
    def __eq__(self, other_student):
        if isinstance(other_student, Student):
            self.stud_one = self._stud_mean_hw_grade(self.name, self.surname)
            other_student = other_student._stud_mean_hw_grade(other_student.name, other_student.surname)
        return self.stud_one == other_student
    
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    #Оценка студентов    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    #Перегрузка метода строки     
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'  


class Lecturer(Mentor):
    lect_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lect_list.append(self) #добавляем объекты класса в список
 
    # Функция для рассчета средней оценки лектора за все его лекции       
    def _lect_mean_hw_grade(self, name, surname):
        if name == self.name and surname == self.surname:
            sum_grades = 0
            sum_elements = 0
            for gradelist in self.grades.values():  
                sum_grades += sum(gradelist)
                sum_elements +=len(gradelist)
        mean_grade = sum_grades / sum_elements
        return mean_grade
 
    #Перегрузка метода строки        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\
            \nСредняя оценка за лекции: {self._lect_mean_hw_grade(self.name, self.surname)}\n' 
    
    #Перегрузка метода стравнения
    def __lt__(self, other_lect):
        if isinstance(other_lect, Lecturer):
            self.lect_one = self._lect_mean_hw_grade(self.name, self.surname)
            other_lect = other_lect._lect_mean_hw_grade(other_lect.name, other_lect.surname)
        return self.lect_one < other_lect
    
    def __gt__(self, other_lect):
        if isinstance(other_lect, Lecturer):
            self.lect_one = self._lect_mean_hw_grade(self.name, self.surname)
            other_lect = other_lect._lect_mean_hw_grade(other_lect.name, other_lect.surname)
        return self.lect_one > other_lect
    
    def __eq__(self, other_lect):
        if isinstance(other_lect, Lecturer):
            self.lect_one = self._lect_mean_hw_grade(self.name, self.surname)
            other_lect = other_lect._lect_mean_hw_grade(other_lect.name, other_lect.surname)
        return self.lect_one == other_lect


# функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса


def _mean_stud_grades_all(stud_list, course):
    sum_gr = 0
    mean_gr = 0
    num_grades = 0
    for object in stud_list:
        if  object.grades.get(course) == None or object.grades.get(course) == 0:
            continue
        # print(object.grades)
        sum_gr += sum(object.grades.get(course))
        num_grades += len(object.grades.get(course)) # берем общее кол-во оценок всех студентов
        
    mean_gr = sum_gr / num_grades
    return mean_gr

#функция для подсчета средней оценки за лекции всех лекторов в рамках курса

def _mean_lect_grades_all(lect_list, course):
    sum_gr = 0
    mean_gr = 0
    num_grades = 0
    for object in lect_list:
        if  object.grades.get(course) == None or object.grades.get(course) == 0:
            continue
        sum_gr += sum(object.grades.get(course))
        num_grades += len(object.grades.get(course)) # берем общее кол-во оценок всех лекторов

    mean_gr = sum_gr / num_grades
    return mean_gr


# Создаем по 2 єкземпляра каждого класса
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']

happy_student = Student('Andrew', 'Reynolds', 'male')
happy_student.courses_in_progress += ['C#']
happy_student.finished_courses += ['Ruby']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached += ['Python']

strange_lecturer = Lecturer('Jane', 'Molly')
strange_lecturer.courses_attached += ['C#']

cool_reviewer = Reviewer('Lev', 'Tolstoy')
cool_reviewer.courses_attached += ['C#']

bad_reviewer = Reviewer('Josef', 'Biden')
bad_reviewer.courses_attached += ['PHP']

# Вызываем функции
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(happy_student, 'C#', 7)
cool_reviewer.rate_hw(happy_student, 'C#', 9)
cool_reviewer.rate_hw(happy_student, 'C#', 10)
 
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 8) 
best_student.rate_lect(cool_lecturer, 'Python', 8) 

happy_student.rate_lect(strange_lecturer, 'C#', 9)
happy_student.rate_lect(strange_lecturer, 'C#', 5)
happy_student.rate_lect(strange_lecturer, 'C#', 7)

# Проверяем перегрузку метода STR
print(best_student)
print(cool_lecturer)
print(cool_reviewer)
 
print(best_student.grades)
print(cool_lecturer.grades)
print(strange_lecturer.grades)

# Вызываем методы сравнения
print("Сравниваем оценки студентов:")
print(best_student.__lt__(happy_student))
print(best_student.__gt__(happy_student))
print(best_student.__eq__(happy_student))

print("Сравниваем оценки лекторов:")
print(cool_lecturer.__lt__(strange_lecturer))
print(cool_lecturer.__gt__(strange_lecturer))
print(cool_lecturer.__eq__(strange_lecturer))

print()

# Вызываем функции для рассчета средней оценки за курс
print('Функции для рассчета средней оценки среди всех Лекторов и студентов: ')
print(_mean_lect_grades_all(Lecturer.lect_list, 'Python'))
print(_mean_stud_grades_all(Student.stud_list, 'Python'))