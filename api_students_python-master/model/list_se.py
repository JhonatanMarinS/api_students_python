from .node import Node
from .student import Student

class ListSE:
    def __init__(self):
        self.head= None

    def add(self, data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            #posicionados en el ultimo
            temp.next = Node(data)

    def add_to_start(self,data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def invert(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp.next != None:
                list_cp.add_to_start(temp.data)
                temp = temp.next
            self.head = list_cp.head

    def count(self):
        count = 0
        if self.head != None:
            temp = self.head
            count=1
            while temp.next != self.head:
                temp = temp.next
                count += 1
        return count


    def validate_exist(self,id:str):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def add(self,data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception ("Ya existe un estudiante con la identificacion")
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next

                    # posicionados en el ultimo
                temp.next = Node(data)

    def exchange_extremes(self):
        if self.head != None:
            if self.head.next != None:
                list_cp = ListSE()
                temp = self.head.next
                while temp.next !=None:
                    list_cp.add_to_start(temp.data)
                    temp = temp.next
                list_cp.add_to_start(temp.data)
                list_cp.add(self.head.data)
                self.head = list_cp.head

    def add_to_position(self, position:int, data:Student):
        if position >0 and position <= (self.count+1):
            if position == 1:
                new_node = Node(Student)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp !=None:
                    if count == position -1:
                        new_node = Node(Student)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count =+1
                        break
                    temp = temp.next
                    count =+1
        else:
            raise Exception("La posici??n no es v??lida")

    def delete_to_position(self, position: int):
        if position > 0 and position <= (self.count):
            if position == 1 and self.count == 1:
                self.head = None
                self.count = -1
            if position == 1 and self.count >= 2:
                self.head = self.head.next
                self.count = -1
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        temp.next.next = temp.next
                        self.count = -1
                        break
                    temp = temp.next
                    count = +1
        else:
            raise Exception("La posici??n no es v??lida")

    def delete_to_data(self, data:Student, id: str):
        if self.validate_exist(data.identification) == False:
            count = 0
            temp = self.head
            while temp != None:
                if self.data.identication == id:
                    position = count
                    self.delete_to_position(position)
                temp = temp.next
                count = +1
        else:
            raise Exception ("La identifacion no se encuentra en la lista")

    def women_first(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp.next != None:
                if self.data.gender == 2:
                    list_cp.add_to_start(temp.data)
                    temp = temp.next
                else:
                    list_cp.add(temp.data)
                    temp = temp.next
            self.head = list_cp.head

    def interleaved_gender(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp.next != None:
                if self.data.gender != list_cp.data.gender:
                    list_cp.add_to_start(temp.data)
                    temp = temp.next
                list_cp.add(temp.data)
                temp = temp.next
            self.head = list_cp.head

























