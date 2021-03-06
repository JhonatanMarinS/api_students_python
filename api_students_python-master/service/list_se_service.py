from model.student import Student
from model.list_se import ListSE

class ListSEService:
    cities = ['Manizales', 'Pereira', 'ChinchinĂ¡', 'Armenia']

    def __init__(self):
        self.students = ListSE()

    def get_all_students(self):
        return self.student.head

    def add_student_to_start(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.student.add_to_start(student)
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
            return {"message":"La lista esta vacia"}
        else:
            self.student.delete_to_position(int)
            return {"message":"Se ha eliminado"}

    def delete_to_position(self, id):
        if self.student.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.student.delete_to_data(str)
            return {"message":"Se ha eliminado"}

    def invert(self):
        if self.student.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.student.invert()
            return {"message":"Se ha invertido la lista"}

    def exchange_extremes(self):
        if self.student.head == None:
            return {"message":"La lista esta vacia"}
        if self.student.head.next == None:
            return {"message":"La lista solo tiene un dato"}
        else:
            self.student.exchange_extremes()
            return {"message": "Se han intercambiado los extremos"}


