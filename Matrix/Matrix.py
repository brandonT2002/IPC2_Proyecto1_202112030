from Matrix.HeaderList import HeaderList
from Matrix.InternalNode import InternalNode
from Matrix.HeaderNode import HeaderNode
class Matrix:
    def __init__(self):
        self.row = HeaderList()
        self.column = HeaderList()
        self.lastR = 0
        self.lastC = 0

    def insert(self,row : int,column : int,value : int):
        if row > self.lastR:
            for i in range(self.lastR,row):
                self.row.insertNode(i)
        if column > self.lastC:
            for i in range(self.lastC,column):
                self.column.insertNode(i)
        if row <= self.lastR and column <= self.lastC:
            self.__addNodeE(row,column,value)
        elif row >= self.lastR and column < self.lastC:
            self.__addNode(self.lastR,row,0,self.lastC,row,column,value)
        elif self.lastR * self.lastC == 0:
            self.__addNode(0,row,0,column,row,column,value)
        else:
            self.__addNode(0,self.lastR,self.lastC,column,row,column,value)
            self.__addNode(self.lastR,row,0,column,row,column,value)

        if row > self.lastR:
            self.lastR = row
        if column > self.lastC:
            self.lastC = column


    def __addNode(self,r0,r1,c0,c1,row,column,value):
        node = None
        for i in range(r0,r1):
            for j in range(c0,c1):
                node = InternalNode(i,j)
                if i == row -1 and j == column -1:
                    node.value = value
                self.__addR(i,node)
                self.__addC(j,node)

    def __addNodeE(self,row,column,value):
        currentR : HeaderNode = self.row.first
        currentC : InternalNode
        while currentR:
            if currentR.index == row - 1:
                currentC = currentR.access
                while currentC:
                    if currentC.column == column - 1:
                        currentC.value = value
                        return
                    currentC = currentC.right
            currentR = currentR.next

    def __addR(self,row,node : InternalNode):
        currentR : HeaderNode = self.row.first
        while currentR:
            if currentR.index == row:
                if currentR.access:
                    currentR.last.right = node
                    currentR.last.right.left = currentR.last
                    currentR.last = currentR.last.right
                    return
                currentR.access = node
                currentR.last = node
            currentR = currentR.next

    def __addC(self,column,node : InternalNode):
        currentC : HeaderNode = self.column.first
        while currentC:
            if currentC.index == column:
                if currentC.access:
                    currentC.last.down = node
                    currentC.last.down.up = currentC.last
                    currentC.last = currentC.last.down
                    return
                currentC.access = node
                currentC.last = node
            currentC = currentC.next

    def printMatrix(self):
        currentR : HeaderNode = self.row.first
        currentC : InternalNode
        matrix = ''
        while currentR:
            currentC = currentR.access
            while currentC:
                matrix += str(currentC.value)
                currentC = currentC.right
            matrix += '\n'
            currentR = currentR.next

        print(matrix)