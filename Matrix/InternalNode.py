class InternalNode:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.value = 0
        self.up : InternalNode = None
        self.down : InternalNode = None
        self.left : InternalNode = None
        self.right: InternalNode = None