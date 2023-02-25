from Matrix.Matrix import SparseMatrix
from Matrix.InternalNode import InternalNode

class Algorithm:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : SparseMatrix) -> SparseMatrix:
        return matrix.cloneMatrix()
    
    def lastCell_R(self,node : InternalNode, idOrganism):
        if node != None and node.value != idOrganism:
            if node.right != None and node.column == node.right.column - 1:
                if node.right.value != idOrganism:
                    return self.lastCell_R(node.right,idOrganism)
                if node.right.value == idOrganism:
                    temporal = self.lastCell_R(node.right,idOrganism)
                    if temporal == None:
                        return InternalNode(node.row,node.column,node.value)
                    return temporal
        if node != None and node.value == idOrganism:
            if node.right != None and node.column == node.right.column - 1:
                return self.lastCell_R(node.right,idOrganism)
        return None
    
    def lastCell_L(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_U(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_D(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_UR(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_UL(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_DR(self,node : InternalNode, idOrganism):
        
        return None
    
    def lastCell_DL(self,node : InternalNode, idOrganism):
        
        return None