#Завдання 4

class StudySubject:
    def init(self):
        self.name = input("Введите название предмета: ")
        self.hours = int(input("Введите количество часов: "))
        self.enable = input("Активен ли предмет? (да/нет): ").strip().lower() == "да"

    def info_study(self):
        print(f'Study: {self.name} | {self.hours} часов | Активен: {"Да" if self.enable else "Нет"}')


class Student:
    def init(self):
        self.name = input("Введите имя студента: ")
        self.surname = input("Введите фамилию студента: ")
        self.studies = []  # список для нескольких предметов
        num_subjects = int(input("Сколько предметов у студента? "))
        for _ in range(num_subjects):
            subject = StudySubject()
            self.studies.append(subject)

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        for subject in self.studies:
            subject.info_study()


class Group:
    def init(self):
        self.name = input("Введите название группы: ")
        self.age_category = input("Введите возрастную категорию группы: ")
        self.students = []
        num_students = int(input("Сколько студентов в группе? "))
        for _ in range(num_students):
            student = Student()
            self.students.append(student)

    def info_group(self):
        print(f'Group: {self.name}, Age Category: {self.age_category}, Students Count: {len(self.students)}')
        for student in self.students:
            student.info_all()


group = Group()
group.info_group()