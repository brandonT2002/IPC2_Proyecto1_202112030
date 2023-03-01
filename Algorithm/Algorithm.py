from Matrix.Matrix import SparseMatrix
from Matrix.InternalNode import InternalNode
from Matrix.HeaderNode import HeaderNode

class Algorithm:
    def __init__(self,matrix):
        self.matrix : SparseMatrix = matrix

    # métodos para comer organismos
    def eatOrganisms_R(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index == nodeI.row:
                currentC = currentR.access
                while currentC:
                    if currentC.column == nodeF.column:
                        currentC.value = idOrganism
                        return
                    if currentC.column > nodeI.column:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_L(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index == nodeF.row:
                currentC = currentR.access
                while currentC:
                    if currentC.column == nodeI.column:
                        return
                    if currentC.column >= nodeF.column:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_U(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentC : HeaderNode = self.matrix.accessC.first
        currentR : InternalNode
        while currentC:
            if currentC.index == nodeF.column:
                currentR = currentC.access
                while currentR:
                    if currentR.row == nodeI.row:
                        return
                    if currentR.row >= nodeF.row:
                        if currentR.value != idOrganism:
                            currentR.value = idOrganism
                    currentR = currentR.down
            currentC = currentC.next

    def eatOrganisms_D(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentC : HeaderNode = self.matrix.accessC.first
        currentR : InternalNode
        while currentC:
            if currentC.index == nodeI.column:
                currentR = currentC.access
                while currentR:
                    if currentR.row == nodeF.row:
                        currentR.value = idOrganism
                        return
                    if currentR.row > nodeI.row:
                        if currentR.value != idOrganism:
                            currentR.value = idOrganism
                    currentR = currentR.down
            currentC = currentC.next

    def eatOrganisms_UR(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        col = columnF
        while currentR:
            if currentR.index >= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column == col:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                            col -= 1
                        break
                    currentC = currentC.right
            currentR = currentR.next
            if currentR.index == rowI:
                return

    def eatOrganisms_UL(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        col = columnF
        while currentR:
            if currentR.index >= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column == col:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                            col += 1
                        break
                    currentC = currentC.right
            currentR = currentR.next
            if currentR.index == rowI:
                return

    def eatOrganisms_DR(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        col = columnI + 1
        while currentR:
            if currentR.index > rowI and currentR.index <= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column == col:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                            col += 1
                        break
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_DL(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        col = columnI - 1
        while currentR:
            if currentR.index > rowI and currentR.index <= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column == col:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                            col -= 1
                        break
                    currentC = currentC.right
            currentR = currentR.next

    # detección de otros organismos en todas las direcciones
    def lastCell_R(self,node : InternalNode, idOrganism):
        if node != None and node.value != idOrganism:
            if node.right != None and node.column == node.right.column - 1:
                if node.right.value != idOrganism:
                    return self.lastCell_R(node.right,idOrganism)
                if node.right.value == idOrganism:
                    temp = self.lastCell_R(node.right,idOrganism)
                    if temp == None:
                        return InternalNode(node.row,node.column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            if node.right != None and node.column == node.right.column - 1:
                return self.lastCell_R(node.right,idOrganism)
        return None
    
    def lastCell_L(self,node : InternalNode, idOrganism):
        if node != None and node.value != idOrganism:
            if node.left != None and node.column == node.left.column + 1:
                if node.left.value != idOrganism:
                    return self.lastCell_L(node.left,idOrganism)
                if node.left.value == idOrganism:
                    temp = self.lastCell_L(node.left,idOrganism)
                    if temp == None:
                        return InternalNode(node.row,node.column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            if node.left != None and node.column == node.left.column + 1:
                return self.lastCell_L(node.left,idOrganism)
        return None
    
    def lastCell_U(self,node : InternalNode, idOrganism):
        if node != None and node.value != idOrganism:
            if node.up != None and node.row == node.up.row + 1:
                if node.up.value != idOrganism:
                    return self.lastCell_U(node.up,idOrganism)
                if node.up.value == idOrganism:
                    temp = self.lastCell_U(node.up,idOrganism)
                    if temp == None:
                        return InternalNode(node.row,node.column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            if node.up != None and node.row == node.up.row + 1:
                return self.lastCell_U(node.up,idOrganism)
        return None
    
    def lastCell_D(self,node : InternalNode, idOrganism):
        if node != None and node.value != idOrganism:
            if node.down != None and node.row == node.down.row - 1:
                if node.down.value != idOrganism:
                    return self.lastCell_D(node.down,idOrganism)
                if node.down.value == idOrganism:
                    temp = self.lastCell_D(node.down,idOrganism)
                    if temp == None:
                        return InternalNode(node.row,node.column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            if node.down != None and node.row == node.down.row - 1:
                return self.lastCell_D(node.down,idOrganism)
        return None
    
    def lastCell_UR(self, row, column, idOrganism):
        node = self.matrix.searchNode(row,column)
        if node != None and node.value != idOrganism:
            node = self.matrix.searchNode(row - 1,column + 1)
            if node != None:
                if node.value != idOrganism:
                    return self.lastCell_UR(row - 1, column + 1, idOrganism)
                if node.value == idOrganism:
                    temp = self.lastCell_UR(row - 1, column + 1, idOrganism)
                    if temp == None:
                        return InternalNode(row,column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            node = self.matrix.searchNode(row - 1,column + 1)
            if node != None:
                return self.lastCell_UR(row - 1, column + 1, idOrganism)
        return None
    
    def lastCell_UL(self, row, column, idOrganism):
        node = self.matrix.searchNode(row,column)
        if node != None and node.value != idOrganism:
            node = self.matrix.searchNode(row - 1, column - 1)
            if node != None:
                if node.value != idOrganism:
                    return self.lastCell_UL(row - 1, column - 1, idOrganism)
                if node.value == idOrganism:
                    temp = self.lastCell_UL(row - 1, column - 1, idOrganism)
                    if temp == None:
                        return InternalNode(row,column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            node = self.matrix.searchNode(row - 1, column - 1)
            if node != None:
                return self.lastCell_UL(row - 1, column - 1, idOrganism)
        return None
    
    def lastCell_DR(self, row, column, idOrganism):
        node = self.matrix.searchNode(row,column)
        if node != None and node.value != idOrganism:
            node = self.matrix.searchNode(row + 1, column + 1)
            if node != None:
                if node.value != idOrganism:
                    return self.lastCell_DR(row + 1, column + 1, idOrganism)
                if node.value == idOrganism:
                    temp = self.lastCell_DR(row + 1, column + 1, idOrganism)
                    if temp == None:
                        return InternalNode(row,column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            node = self.matrix.searchNode(row + 1, column + 1)
            if node != None:
                return self.lastCell_DR(row + 1, column + 1, idOrganism)
        return None
    
    def lastCell_DL(self, row, column, idOrganism):
        node = self.matrix.searchNode(row,column)
        if node != None and node.value != idOrganism:
            node = self.matrix.searchNode(row + 1, column - 1)
            if node != None:
                if node.value != idOrganism:
                    return self.lastCell_DL(row + 1, column - 1, idOrganism)
                if node.value == idOrganism:
                    temp = self.lastCell_DL(row + 1, column - 1, idOrganism)
                    if temp == None:
                        return InternalNode(row,column,node.value)
                    return temp
        if node != None and node.value == idOrganism:
            node = self.matrix.searchNode(row + 1, column - 1)
            if node != None:
                return self.lastCell_DL(row + 1, column - 1, idOrganism)
        return None
    
    def evaluateToEat(self,node):
        self.last_R = None
        self.last_L = None
        self.last_U = None
        self.last_D = None
        self.last_UR = None
        self.last_UL = None
        self.last_DR = None
        self.last_DL = None
        if node.right != None and node.column == node.right.column - 1:
            self.last_R = self.lastCell_R(node.right,node.value)

        if node.left != None and node.column == node.left.column + 1:
            self.last_L = self.lastCell_L(node.left,node.value)

        if node.up != None and node.row == node.up.row + 1:
            self.last_U = self.lastCell_U(node.up,node.value)

        if node.down != None and node.row == node.down.row - 1:
            self.last_D = self.lastCell_D(node.down,node.value)

        if self.matrix.searchNode(node.row,node.column) != None and self.matrix.searchNode(node.row - 1,node.column + 1) != None:
            self.last_UR = self.lastCell_UR(node.row - 1,node.column + 1,node.value)

        if self.matrix.searchNode(node.row,node.column) != None and self.matrix.searchNode(node.row - 1,node.column - 1) != None:
            self.last_UL = self.lastCell_UL(node.row - 1,node.column - 1,node.value)

        if self.matrix.searchNode(node.row,node.column) != None and self.matrix.searchNode(node.row + 1,node.column + 1) != None:
            self.last_DR = self.lastCell_DR(node.row + 1,node.column + 1,node.value)

        if self.matrix.searchNode(node.row,node.column) != None and self.matrix.searchNode(node.row + 1,node.column - 1) != None:
            self.last_DL = self.lastCell_DL(node.row + 1,node.column - 1,node.value)

        if not self.last_R and not self.last_L and not self.last_U and not self.last_D and not self.last_UR and not self.last_UL and not self.last_DR and not self.last_DL:
            print('\nNo Prospera\n')
            self.matrix.unbindNode(node)
            return

        if self.last_R:
            self.eatOrganisms_R(node,self.last_R,node.value)

        if self.last_L:
            self.eatOrganisms_L(node,self.last_L,node.value)

        if self.last_U:
            self.eatOrganisms_U(node,self.last_U,node.value)

        if self.last_D:
            self.eatOrganisms_D(node,self.last_D,node.value)

        if self.last_UR:
            self.eatOrganisms_UR(node.row,node.column,self.last_UR.row,self.last_UR.column,node.value)

        if self.last_UL:
            self.eatOrganisms_UL(node.row,node.column,self.last_UL.row,self.last_UL.column,node.value)

        if self.last_DR:
            self.eatOrganisms_DR(node.row,node.column,self.last_DR.row,self.last_DR.column,node.value)

        if self.last_DL:
            self.eatOrganisms_DL(node.row,node.column,self.last_DL.row,self.last_DL.column,node.value)
