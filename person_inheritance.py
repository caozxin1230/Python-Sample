class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


student_1 = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX045")
student_1.enrol('a_postgrad_course')

staff_1 = Lecturer(StaffMember.PERMANENT, "Bob", "Jones", "123456789")
staff_1.assign_teaching('an_undergrad_course')

print(student_1.name, student_1.surname, student_1.classes)
print(staff_1.name, staff_1.surname, staff_1.courses_taught)
