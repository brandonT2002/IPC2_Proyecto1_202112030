from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm

m = SparseMatrix()
#organismos 1 - verde
m.insert(1,4,1)
m.insert(2,2,1)
m.insert(6,2,1)
m.insert(9,3,1)

#organismos 2 - amarillo
m.insert(2,3,2)
m.insert(2,4,2)
m.insert(3,3,2)
m.insert(4,4,2)
m.insert(5,2,2)
m.insert(5,3,2)
m.insert(5,4,2)
m.insert(7,3,2)

#organismos 3 - azul
m.insert(3,2,3)
m.insert(3,2,3)
m.insert(4,2,3)
m.insert(4,3,3)
m.insert(6,3,3)
m.insert(8,2,3)
m.insert(8,3,3)
m.insert(8,4,3)
m.insert(8,5,3)

print('\nOriginal')
m.print()
a = Algorithm(m)

m.insert(2,5,2)
print('\nNuevo')
m.print()

node2 = m.searchNode(2,5)

print()
a.evaluateToEat(node2)
m.print()