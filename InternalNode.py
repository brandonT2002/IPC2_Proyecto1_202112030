class InternalNode:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.value = 0
        self.up = None
        self.down = None
        self.left = None
        self.right = None