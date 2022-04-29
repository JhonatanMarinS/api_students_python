from model.student import Student
from model.list_se_doble import ListSEDoble
class ListSEDobleService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSEDoble()
        # carloaiza = Student("363763763", 1, 5000000,True, "Carlos Loaiza",self.cities[2])
        carloaiza = Student({"idenfication": "75147236", "name": "Carlos Loaiza",
                             "gender": 1, "salary": 2000000, "job": True, "city": self.cities[2]})
        self.students.add(carloaiza)
        self.students.add(Student({"idenfication": "1060456789",
                                   "name": "Valentina Hurtado",
                                   "gender": 2, "salary": 0, "job": False,
                                   "city": self.cities[0]}))

    def get_all_students(self):
        return self.students.head

    def add_student_to_start(self, data):
        student = Student(data)
        if data("city") in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad ingresada no es valida")

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