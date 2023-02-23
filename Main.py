from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
m = SparseMatrix()
m.insert(4,4,1)

m.insert(4,5,2)
m.insert(5,4,2)
m.insert(5,5,2)
m.insert(6,3,2)
m.insert(6,4,2)
m.insert(6,5,2)

m.insert(7,9,3)
m.insert(8,8,3)
m.insert(9,9,3)

m.insert(7,8,4)
m.insert(8,9,4)
m.insert(9,10,4)

print('\nOriginal')
m.print()

a = Algorithm(m)
print('\nClon')
a.clon.print()

print('\nNuevo')
m.insert(4,6,1)
m.print()