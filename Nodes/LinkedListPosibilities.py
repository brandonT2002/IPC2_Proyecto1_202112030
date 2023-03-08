class LinkedListPosibilities:
    def __init__(self):
        self.first = None
        self.last = None

    def insertCoord(self,row,column):
        if self.first:
            self.last.next = NodeCoord(row,column)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = NodeCoord(row,column)
        self.last = self.first

    def iterateList(self):
        self.current = self.first
        while self.current:
            print(self.current.row,self.current.column)
            self.current = self.current.next

class NodeCoord:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.next = None
        self.prev = None