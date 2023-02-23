from Matrix.InternalNode import NodeI
class NodeH:
    def __init__(self,index):
        self.index = index
        self.previous : NodeH = None
        self.next : NodeH = None
        self.access : NodeI = None
        self.last : NodeI = None