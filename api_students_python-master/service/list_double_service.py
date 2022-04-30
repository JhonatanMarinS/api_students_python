from model.student import Student
from model.list_double import ListSEDoble

class ListDoubleService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSEDoble()

    def get_all_students(self):
        return self.students.list()

    def add_student_to_start(self, data):
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

    def add_student_to_position(self, data, position):
        student = Student(data)
        if data["city"] in self.cities:
            self.student.add_to_position(student)
        else:
            raise Exception("La ciudad ingresada no es valida")

    def delete_to_position(self, position):
        if self.student.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.student.delete_to_position(int)
            return {"message": "Se ha eliminado"}

    def delete_to_data(self, id):
        if self.student.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.student.delete_to_data(str)
            return {"message": "Se ha eliminado"}

    def invert(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.invert()
            return {"message": "Se ha invertido la lista"}

    def exchange_extremes(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        if self.students.head.next == None:
            return {"message": "La lista solo tiene un dato"}
        else:
            self.students.exchange_extremes()
            return {"message": "Se han intercambiado los extremos"}

    def delete_to_age(self):
        if self.student.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.student.delete_to_age(str)
            return {"message": "Se han eliminado"}
