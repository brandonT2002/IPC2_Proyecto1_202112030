from Matrix.Matrix import Matrix
from Matrix.InternalNode import InternalNode

class Algorithm:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : Matrix) -> Matrix:
        return matrix.clone()
    
    def lastCell_R(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.right != None and node.right.value != idOrganism:
                return self.lastCell_R(node.right,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None
    
    def lastCell_L(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.left != None and node.left.value != idOrganism:
                return self.lastCell_L(node.left,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None
    
    def lastCell_U(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.up != None and node.up.value != idOrganism:
                return self.lastCell_U(node.up,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None
    
    def lastCell_D(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.down != None and node.down.value != idOrganism:
                return self.lastCell_D(node.down,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None
    
    def lastCell_UR(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.up.right != None and node.up.right.value != idOrganism:
                return self.lastCell_UR(node.up.right,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None
    
    def lastCell_UL(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0:
            if node.up.left != None and node.up.left.value != idOrganism:
                return self.lastCell_UL(node.up.left,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None