from Matrix.HeaderList import HeaderList
from Matrix.InternalNode import NodeI
from Matrix.HeaderNode import NodeH

class SparseMatrix:
    def __init__(self):
        self.accessR = HeaderList()
        self.accessC = HeaderList()

    def insert(self,row,column,number):
        if not self.accessR.isHearIndex(row):
            self.accessR.add(row)
        if not self.accessC.isHearIndex(column):
            self.accessC.add(column)
        node = NodeI(row,column,number)
        self.addRow(row,node)
        self.addColumn(column,node)

    def addRow(self,row,node : NodeI):
        currentR = self.accessR.first
        while currentR:
            if currentR.index == row:
                if currentR.access:
                    if node.column < currentR.access.column:
                        currentR.access.left = node
                        currentR.access.left.right = currentR.access
                        currentR.access = currentR.access.left
                    elif node.column > currentR.last.column:
                        currentR.last.right = node
                        currentR.last.right.left = currentR.last
                        currentR.last = currentR.last.right
                    else:
                        currentC = currentR.access
                        while currentC.right:
                            if node.column > currentC.column and node.column < currentC.right.column:
                                node.left = currentC
                                node.right = currentC.right

                                currentC.right.left = node
                                currentC.right = node
                                return
                            currentC = currentC.right
                    return
                currentR.access = node
                currentR.last = currentR.access
                return
            currentR = currentR.next

    def addColumn(self,column,node : NodeI):
        currentC = self.accessC.first
        while currentC:
            if currentC.index == column:
                if currentC.access:
                    if node.row < currentC.access.row:
                        currentC.access.up = node
                        currentC.access.up.down = currentC.access
                        currentC.access = currentC.access.up
                    elif node.row > currentC.last.row:
                        currentC.last.down = node
                        currentC.last.down.up = currentC.last
                        currentC.last = currentC.last.down
                    else:
                        currentR = currentC.access
                        while currentR.down:
                            if node.row > currentR.row and node.row < currentR.down.row:
                                node.up = currentR
                                node.down = currentR.down

                                currentR.down.up = node
                                currentR.down = node
                                return
                            currentR = currentR.down
                    return
                currentC.access = node
                currentC.last = currentC.access
                return
            currentC = currentC.next

    def print(self) :
        currentR = self.accessR.first
        while currentR:
            currentC = currentR.access
            w = ''
            while currentC:
                w += f'{currentC.number} '
                currentC = currentC.right
            print(w)
            currentR = currentR.next

    def cloneMatrix(self):
        m = SparseMatrix()
        currentR : NodeH = self.accessR.first
        currentC : NodeI
        while currentR:
            currentC = currentR.access
            while currentC:
                m.insert(currentC.row,currentC.column,currentC.number)
                currentC = currentC.right
            currentR = currentR.next
        return m
