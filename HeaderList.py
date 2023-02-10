from HeaderNode import HeaderNode

class HeaderList:
    def __init__(self):
        self.fist = None
        self.last = None

    def insertNode(self,index):
        if self.first:
            self.last.next = HeaderNode(index)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = HeaderNode(index)
        self.last = self.first