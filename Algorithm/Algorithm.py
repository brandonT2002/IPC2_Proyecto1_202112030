from Matrix.Matrix import Matrix
from Matrix.InternalNode import InternalNode

class Algorithm:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : Matrix) -> Matrix:
        return matrix.clone()
    
    def lastCell_R(self,node : InternalNode, idOrganism):
        if node != None and node.value != 0 and node.value != idOrganism:
            if node.right != None and node.right.value != idOrganism:
                return self.lastCell_R(node.right,idOrganism)
            else:
                return InternalNode(node.row, node.column)
        return None