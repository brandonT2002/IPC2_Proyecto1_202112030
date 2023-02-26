from Matrix.Matrix import SparseMatrix
from Matrix.InternalNode import InternalNode

class Algorithm:
    def __init__(self,matrix):
        self.matrix : SparseMatrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : SparseMatrix) -> SparseMatrix:
        return matrix.cloneMatrix()
    
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