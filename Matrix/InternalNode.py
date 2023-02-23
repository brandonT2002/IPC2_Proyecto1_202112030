class InternalNode:
    def __init__(self,row,column,value : int):
        self.value = value
        self.row = row
        self.column = column
        self.right : InternalNode = None
        self.left : InternalNode = None
        self.up : InternalNode = None
        self.down : InternalNode = None