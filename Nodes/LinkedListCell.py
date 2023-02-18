from Nodes.NodeCell import NodeCell
class LinkedListCell:
    def __init__(self):
        self.first = None
        self.last = None

    def insertCell(self,cell):
        if self.first:
            self.last.next = NodeCell(cell)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = NodeCell(cell)
        self.last = self.first

    def iterateList(self):
        self.current = self.first
        while self.current:
            print(self.current.cell.row,self.current.cell.column,self.current.cell.organism)
            self.current = self.current.next