from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
from Matrix.InternalNode import InternalNode
m = SparseMatrix()
m.insert(3,8,1)
#m.insert(4,7,2)
m.insert(5,6,2)

print('\nOriginal')
m.print()
a = Algorithm(m)

# print('\nClon')
# a.clon.print()

print('\nNuevo')
m.insert(6,5,1)
m.print()

node = m.searchNode(6,5)
print('\n',node.toString(0))
#print(node.__dict__)
row = -1
column = -1
# if node.down != None and node.row == node.down.row - 1:
#     last_R = a.lastCell_D(node.down,node.value)
#     if last_R:
#         row = last_R.row
#         column = last_R.column
# print('\nderecha')
# print(row,column)

print(node.__dict__)
if m.searchNode(node.row,node.column) != None and m.searchNode(node.row - 1,node.column + 1) != None:
    print('entra')
    last_D = a.lastCell_UR(node.row - 1,node.column + 1,node.value)
    if last_D:
        row = last_D.row
        column = last_D.column
print(row,column)