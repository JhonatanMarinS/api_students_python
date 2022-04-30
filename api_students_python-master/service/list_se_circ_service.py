from model.student import Student
from model.list_se_circ import ListSECirc

class ListSECircService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSECirc()

    def get_all_students(self):
        return self.students.head

    def add_student_to_start(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad ingresada no es valida")

    def add(self, data):
        student = Student(data)
        if data["city"] in self.cities:
            self.student.add(student)
        else:
            raise Exception("La ciudad ingresada no es valida")

