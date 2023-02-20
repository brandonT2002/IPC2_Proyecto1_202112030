from Matrix.Matrix import Matrix

class Algorithm:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clon = self.clone(self.matrix)

    def clone(self,matrix : Matrix) -> Matrix:
        return matrix.clone()