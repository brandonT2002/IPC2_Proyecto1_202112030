from Matrix.Matrix import SparseMatrix
matrix = SparseMatrix()
matrix.insert(2,3,5)
matrix.insert(0,1,5)
matrix.insert(1,2,5)
matrix.insert(1,1,5)

matrix.insert(0,0,1)
matrix.insert(0,2,1)
matrix.insert(0,3,1)

matrix.insert(1,0,1)
matrix.insert(1,3,1)

matrix.insert(2,0,1)
matrix.insert(2,1,1)
matrix.insert(2,2,1)

matrix.print()