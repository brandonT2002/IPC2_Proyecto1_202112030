from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
from Matrix.InternalNode import InternalNode
m = SparseMatrix()
m.insert(3,4,2)
m.insert(4,4,2)
m.insert(5,4,3)
m.insert(6,4,1)

print('\nOriginal')
m.print()

a = Algorithm(m)
# print('\nClon')
# a.clon.print()

print('\nNuevo')
m.insert(2,4,1)
m.print()

node = m.searchNode(2,4)
#print('\n',node.toString(0))
#print(node.__dict__)
row = -1
column = -1
if node.down != None and node.row == node.down.row - 1:
    last_R = a.lastCell_D(node.down,node.value)
    if last_R:
        row = last_R.row
        column = last_R.column
print('\nderecha')
print(row,column)