class NodeI:
    def __init__(self,row,column,number : int):
        self.number = number
        self.row = row
        self.column = column
        self.right : NodeI = None
        self.left : NodeI = None
        self.up : NodeI = None
        self.down : NodeI = None