from Nodes.NodeOrganism import NodeOrganism

class LinkedListOrganism:
    def __init__(self):
        self.first = None
        self.last = None

    def insertOrganism(self,organism):
        if self.first:
            self.last.next = NodeOrganism(organism)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = NodeOrganism(organism)
        self.last = self.first

    def iterateList(self):
        self.current = self.first
        while self.current:
            print(self.current.organism.code,self.current.organism.name)