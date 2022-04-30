from .node_doble import NodeDoble
from .student import Student

class ListSEDoble:
    def __init__(self):
        self.head = None

    def add(self, data:Student):
        if self.head == None:
            self.head = NodeDoble(data)
        else:
            temp = self.head
            while temp.next != None:
                temp.next.previous = temp
                temp = temp.next
            temp.next = NodeDoble(data)
            temp.next.previous = temp

    def add_to_start(self, data: Student):
        if self.head == None:
            self.head = NodeDoble(data)
        else:
            temp = NodeDoble(data)
            temp.next = self.head
            temp.next.previous = temp
            self.head = temp

    def invert(self):
        if self.head != None:
            list_cp = ListSEDoble()
            temp = self.head
            while temp.next != None:
                list_cp.add_to_start(temp.data)
                temp.next.previous = temp
                temp = temp.next
            self.head = list_cp.head

    def count(self):
        count = 0
        if self.head != None:
            temp = self.head
            count=1
            while temp.next != self.head:
                temp.next.previous = temp
                temp = temp.next
                count += 1
        return count

    def exchange_extremes(self):
        if self.head != None:
            if self.head.next != None:
                list_cp = ListSEDoble()
                temp = self.head.next
                while temp.next !=None:
                    list_cp.add_to_start(temp.data)
                    temp.next.previous = temp
                    temp = temp.next
                list_cp.add_to_start(temp.data)
                list_cp.add(self.head.data)
                self.head = list_cp.head

    def add_to_position(self,position:int, data:Student):
        if position >0 and position <= (self.count+1):
            if position == 1:
                new_node = NodeDoble(Student)
                new_node.next = self.head
                new_node.next.previous = new_node
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp !=None:
                    if count == position -1:
                        new_node = NodeDoble(Student)
                        new_node.next = temp.next
                        new_node.next.previous = new_node
                        temp.next = new_node
                        temp.next.previous = temp
                        self.count =+1
                        break
                    temp.next.previous = temp
                    temp = temp.next
                    count =+1
        else:
            raise Exception("La posición no es válida")

    def delete_to_position(self, position: int):
        if position > 0 and position <= (self.count):
            if position == 1 and self.count == 1:
                self.head = None
                self.count = -1
            if position == 1 and self.count >= 2:
                self.head = self.head.next
                self.head.previus = None
                self.count = -1
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        temp.next.next = temp.next
                        temp.next.previous = temp
                        self.count = -1
                        break
                    temp.next.previous = temp
                    temp = temp.next
                    count = +1
        else:
            raise Exception("La posición no es válida")

    def delete_to_data(self, data:Student):
        if self.validate_exist(data.identification) == False:
            count = 0
            temp = self.head
            while temp != None:
                if self.data.identication == id:
                    position = count
                    self.delete_to_position(position)
                temp.next.previous = temp
                temp = temp.next
                count = +1
        else:
            raise Exception ("La identifacion no se encuentra en la lista")

    def women_first(self):
        if self.head != None:
            list_cp = ListSEDoble()
            temp = self.head
            while temp.next != None:
                if self.data.gender == 2:
                    list_cp.add_to_start(temp.data)
                    temp.next.previous = temp
                    temp = temp.next
                else:
                    list_cp.add(temp.data)
                    temp.next.previous = temp
                    temp = temp.next
            self.head = list_cp.head

    def interleaved_gender(self):
        if self.head != None:
            list_cp = ListSEDoble()
            temp = self.head
            while temp.next != None:
                if self.data.gender != list_cp.data.gender:
                    list_cp.add_to_start(temp.data)
                    temp.next.previous = temp
                    temp = temp.next
                list_cp.add(temp.data)
                temp.next.previous = temp
                temp = temp.next
            self.head = list_cp.head

    def delete_to_age(self, num:int):
        if self.head != None:
            list_cp = ListSEDoble()
            temp = self.head
            age = self.data.age
            while temp.next != None:
                if age != None:
                    if (self.data.age % 10) == num:
                        temp = temp.next
                    else:
                        list_cp.add(temp.data)
                    temp = temp.next
                else:
                    raise Exception("El estudiante{} No tiene una edad ingresada".format(self.data.name))
            self.head = list_cp.head
        else:
            raise Exception("La lista se encuentra vacia")