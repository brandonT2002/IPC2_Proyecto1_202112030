from Nodes.NodeSample import NodeSample

class LinkedListSample:
    def __init__(self):
        self.first = None
        self.last = None

    def insertSample(self,sample):
        if self.first:
            self.last.next = NodeSample(sample)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = NodeSample(sample)
        self.last = self.first

    def iterateList(self):
        self.current = self.first
        while self.current:
            print(self.current.sample.code,self.current.sample.description,self.current.sample.row,'x',self.current.sample.column)
            self.current.sample.liveCells.iterateList()
            self.current = self.current.next