from Matrix.InternalNode import InternalNode
class HeaderNode:
    def __init__(self,index):
        self.index = index
        self.previous : HeaderNode = None
        self.next : HeaderNode = None
        self.access : InternalNode = None
        self.last : InternalNode = None