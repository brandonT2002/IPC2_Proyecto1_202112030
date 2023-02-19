class HeaderNode:
    def __init__(self,index):
        self.index : int = index
        self.next : HeaderNode = None
        self.prev : HeaderNode = None
        self.access : HeaderNode = None
        self.last : HeaderNode = None