class Student:
    students_dict = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_hw = {}
               

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades_lecture:
                lecturer.grades_lecture[course] += [grade]
            else:
                lecturer.grades_lecture[course] = [grade]
        else:
            return 'Ошибка'

    def calculate(self):
        sum_grades_hw = 0
        for dict_grades_hw in self.grades_hw.values():
            for grade in dict_grades_hw:
                sum_grades_hw += grade
                average_rating_st = round(sum_grades_hw / len(dict_grades_hw), 2)
            return average_rating_st  

    def __str__(self):
            some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
            return some_student
          
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        elif self.calculate() > other.calculate():
            a = f'{self.name} {self.surname} лучше {other.name} {other.surname}'
            return a
        elif self.calculate() == other.calculate():
            x = f'{self.name} {self.surname} имеет такой же балл {other.name} {other.surname}'
            return x
        else:
            b = f'{self.name} {self.surname} хуже {other.name} {other.surname}'
            return b                            
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
          
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecture = {}


    def calculate_lec(self):
        sum_grades_lecture = 0
        for dict_grades_lecture in self.grades_lecture.values():
            for grade in dict_grades_lecture:
                sum_grades_lecture += grade
                average_rating_lecturer = round(sum_grades_lecture / len(dict_grades_lecture), 2)
            return average_rating_lecturer 
          
    def __str__(self):
            some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_lec()}'
            return some_lecturer

    def __lt__(self, other):
            if not isinstance(other, Lecturer):
                print('Ошибка')
                return
            elif self.calculate_lec() > other.calculate_lec():
                a = f'{self.name} {self.surname} лучше {other.name} {other.surname}'
                return a
            elif self.calculate_lec() == other.calculate_lec():
                b = f'{self.name} {self.surname} имеет такой же балл {other.name} {other.surname}'
                return b
            else:
                c = f'{self.name} {self.surname} хуже {other.name} {other.surname}'
                return c
      
class Reviewer(Mentor):      
  
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_hw:
                student.grades_hw[course] += [grade]
            else:
                student.grades_hw[course] = [grade]
        else:
            return 'Ошибка'
          
    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer
        
 
student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python']
 
reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
 
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
 
print(reviewer)
print()


lecturer = Lecturer('Vasya', 'Pupkin')
lecturer.courses_attached += ['Python']

student.rate_lecture(lecturer, 'Python', 8)
student.rate_lecture(lecturer, 'Python', 6)
student.rate_lecture(lecturer, 'Python', 10)

print(lecturer)
print()


Ivan = Student('Ivan', 'Drago', 'm') 
Ivan.courses_in_progress += ['Python']
Ivan.courses_in_progress += ['Git']
Ivan.finished_courses += ['Введение в программирование'] 
reviewer.rate_hw(Ivan, 'Python', 5)
reviewer.rate_hw(Ivan, 'Python', 10)
reviewer.rate_hw(Ivan, 'Python', 7)

Ослик = Student('Ослик', 'Огородников', 'm')
Ослик.courses_in_progress += ['Python']
Ослик.courses_in_progress += ['Git']
Ослик.finished_courses += ['Введение в программирование']
reviewer.rate_hw(Ослик, 'Python', 8)
reviewer.rate_hw(Ослик, 'Python', 9)
reviewer.rate_hw(Ослик, 'Python', 9)


print(Ivan)
print()
print(Ослик)
print(Ivan.calculate())
print(Ослик.calculate())
print(Ivan.__lt__(Ослик))
print()


Ахалай = Lecturer('Ахалай', 'Махалай')
Ахалай.courses_attached += ['Python']
student.rate_lecture(Ахалай, 'Python', 8)
student.rate_lecture(Ахалай, 'Python', 6)
student.rate_lecture(Ахалай, 'Python', 10)

Рахат = Lecturer('Рахат', 'Лукум')
Рахат.courses_attached += ['Python']
student.rate_lecture(Рахат, 'Python', 7)
student.rate_lecture(Рахат, 'Python', 6)
student.rate_lecture(Рахат, 'Python', 9)

print(Рахат)
print(Ахалай)
print(Ахалай.__lt__(Рахат))
print(Рахат.__lt__(Ахалай))
print(Рахат.calculate_lec())

print()


lecture_dict = [
   {'name':'Ахалай', 'surname':'Махалай', 'grades':[8,6,10], 'courses':['Python']},
   {'name':'Захат', 'surname':'Лукум', 'grades':[9,9,7], 'courses':['Python']}]


def calculate_average_lec(dict, course_name):
        grades = []
        lecture_course = 0
        for lecture in dict:
                    if course_name in lecture['courses']:
                        lecture_course += 1
                        grades += lecture['grades']
                        sum_grades = sum(grades)
        average = (sum_grades / len(lecture['grades'])) / lecture_course
        print(round(average, 2))   
                                         
calculate_average_lec(lecture_dict, 'Python')
print()


students_dict = [
   {'name':'Ivan', 'surname':'Drago', 'gender':'m', 'grades':[7,9,5], 'courses':['Python']},
   {'name':'Ослик', 'surname':'Огородников', 'gender':'m', 'grades':[6,10,10],  'courses':['Python']},           
   {'name':'Чудо', 'surname':'Дивное', 'gender':'m', 'grades':[9,9,7], 'courses':['Git']}]


def calculate_average_st(dict, course_name):
        grades = []
        student_course = 0
        for student in dict:
                if course_name in student['courses']:
                        student_course += 1
                        grades.extend(student['grades'])
                        sum_grades = sum(grades)
        average = round(((sum_grades / len(student['grades'])) / student_course), 2)
        print(average)
                
                                           
calculate_average_st(students_dict,'Python')