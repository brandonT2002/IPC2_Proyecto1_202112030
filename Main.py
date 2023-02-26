from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
from Matrix.InternalNode import InternalNode
m = SparseMatrix()
m.insert(2,4,1)
m.insert(3,4,2)
m.insert(4,4,2)
m.insert(5,4,3)

print('\nOriginal')
m.print()

a = Algorithm(m)
# print('\nClon')
# a.clon.print()

print('\nNuevo')
m.insert(6,4,1)
m.print()

node = m.searchNode(6,4)
#print('\n',node.toString(0))
print(node.__dict__)
row = -1
column = -1
if node.up != None and node.row == node.up.row + 1:
    last_R = a.lastCell_U(node.up,node.value)
    if last_R:
        row = last_R.row
        column = last_R.column
print('\nderecha')
print(row,column)