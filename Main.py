from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm

a = Algorithm(SparseMatrix())

a.matrix.insert(10,10,1)
a.matrix.insert(10,11,1)
a.matrix.insert(10,12,1)
a.matrix.insert(10,13,1)
a.matrix.insert(11,10,1)
a.matrix.insert(11,11,1)
a.matrix.insert(11,12,1)

a.matrix.insert(9,11,3)
a.matrix.insert(9,12,3)

a.matrix.insert(12,11,2)
a.matrix.insert(12,12,2)

#a.matrix.insert(3,1,2)

print('\nOriginal')
a.matrix.print()


#a.matrix.insert(9,10,3)
a.matrix.insert(3,3,1)
print('\nNuevo')
a.matrix.print()

print()
a.evaluateToEat(a.matrix.searchNode(3,3))