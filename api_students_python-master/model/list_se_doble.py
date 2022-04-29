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
                temp.next.previus = temp
                temp = temp.next

            #posicionados en el ultimo
            temp.next = NodeDoble(data)
            temp.next.previus = temp

    def add_to_start(self, data: Student):
        if self.head == None:
            self.head = NodeDoble(data)
        else:
            temp = NodeDoble(data)
            temp.next = self.head
            temp.next.previus = temp
            self.head = temp

    def invert(self):
        if self.head != None:
            list_cp = ListSEDoble()
            temp = self.head
            while temp.next != None:
                list_cp.add_to_start(temp.data)
                temp.next.previus = temp
                temp = temp.next
            self.head = list_cp.head

    def exchange_extremes(self):
        if self.head != None:
            if self.head.next != None:
                list_cp = ListSEDoble()
                temp = self.head.next
                while temp.next !=None:
                    list_cp.add_to_start(temp.data)
                    temp.next.previus = temp
                    temp = temp.next
                list_cp.add_to_start(temp.data)
                list_cp.add(self.head.data)
                self.head = list_cp.head