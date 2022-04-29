from .node import Node
from .student import Student

class ListSECirc:
    def __init__(self):
        self.head = None

    def add(self, data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            #posicionados en el ultimo
            temp.next = Node(data)
            temp.next.next = self.head

    def add_to_start(self, data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node = Node(data)
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def list(self):
        list = []
        if self.head != None:
            temp = self.head
            while temp.next != self.head:
                list.append(temp.data)
                temp = temp.next
            list.append(temp.data)
        return list

    def count(self):
        count = 0
        if self.head != None:
            temp = self.head
            count=1
            while temp.next != self.head:
                temp = temp.next
                count += 1
        return count
