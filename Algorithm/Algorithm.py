from Matrix.Matrix import SparseMatrix
from Matrix.InternalNode import NodeI

class Algorithm:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : SparseMatrix) -> SparseMatrix:
        return matrix.cloneMatrix()
    
    def lastCell_R(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.right != None and node.right.value != idOrganism:
                return self.lastCell_R(node.right,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_L(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.left != None and node.left.value != idOrganism:
                return self.lastCell_L(node.left,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_U(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.up != None and node.up.value != idOrganism:
                return self.lastCell_U(node.up,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_D(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.down != None and node.down.value != idOrganism:
                return self.lastCell_D(node.down,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_UR(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.up != None and node.up.right != None and node.up.right.value != idOrganism:
                return self.lastCell_UR(node.up.right,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_UL(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.up != None and node.up.left != None and node.up.left.value != idOrganism:
                return self.lastCell_UL(node.up.left,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_DR(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.down != None and node.down.right != None and node.down.right.value != idOrganism:
                return self.lastCell_DR(node.down.right,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None
    
    def lastCell_DL(self,node : NodeI, idOrganism):
        if node != None and node.value != 0:
            if node.down != None and node.down.left != None and node.down.left.value != idOrganism:
                return self.lastCell_DL(node.down.left,idOrganism)
            else:
                return NodeI(node.row, node.column)
        return None