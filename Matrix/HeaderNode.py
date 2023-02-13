class HeaderNode:
    def __init__(self,index):
        self.index = index
        self.next = None
        self.prev = None
        self.access = None
        self.last = None