from Colors.NodeColor import NodeColor

class LinkedListColors:
    def __init__(self):
        self.first : NodeColor = None
        self.last : NodeColor = None

    def insert(self,color):
        if self.first:
            self.last.next = NodeColor(color)
            self.last = self.last.next
            return
        self.first = NodeColor(color)
        self.last = self.first

    def recorrer(self):
        current = self.first
        while current:
            print(current.color)
            current = current.next

    def pop(self):
        if self.first:
            temp = self.first.color
            self.first = self.first.next
            return temp
        return None