from classes.staff import Staff
from classes.student import Student


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        for student in self.students:
            print(student.name, student.school_id)

    def find_student_by_id(self, id):
        for student in self.students:
            if id == student.school_id:
                return student
