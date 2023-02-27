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
                    if currentC.column >= nodeI.column and currentC.column <= nodeF.column:
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
                    if currentC.column <= nodeI.column:
                        currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_U(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index >= nodeF.row and currentR.index <= nodeI.row:
                currentC = currentR.access
                while currentC:
                    if currentC.column == nodeI.column:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_D(self,nodeI : InternalNode, nodeF : InternalNode, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index >= nodeI.row and currentR.index <= nodeF.row:
                currentC = currentR.access
                while currentC:
                    if currentC.column == nodeI.column:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_UR(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index <= rowI and currentR.index >= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column >= columnI and currentC.column <= columnF:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_UL(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index <= rowI and currentR.index >= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column <= columnI and currentC.column >= columnF:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_DR(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index >= rowI and currentR.index <= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column >= columnI and currentC.column <= columnF:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
                    currentC = currentC.right
            currentR = currentR.next

    def eatOrganisms_DL(self, rowI, columnI, rowF, columnF, idOrganism):
        currentR : HeaderNode = self.matrix.accessR.first
        currentC : InternalNode
        while currentR:
            if currentR.index >= rowI and currentR.index <= rowF:
                currentC = currentR.access
                while currentC:
                    if currentC.column <= columnI and currentC.column >= columnF:
                        if currentC.value != idOrganism:
                            currentC.value = idOrganism
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