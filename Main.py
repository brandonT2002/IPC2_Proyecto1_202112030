from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
from Matrix.InternalNode import InternalNode
m = SparseMatrix()
m.insert(7,6,2)
m.insert(8,7,2)
m.insert(9,8,1)

print('\nOriginal')
m.print()
a = Algorithm(m)

# print('\nClon')
# a.clon.print()

print('\nNuevo')
m.insert(6,5,1)
m.print()

node = m.searchNode(6,5)
#print('\n',node.toString(0))
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

# if m.searchNode(node.row,node.column) != None and m.searchNode(node.row - 1,node.column + 1) != None:
#     last_D = a.lastCell_UR(node.row - 1,node.column + 1,node.value)
#     if last_D:
#         row = last_D.row
#         column = last_D.column
# print('\nult pos')
# print(row,column)

# if m.searchNode(node.row,node.column) != None and m.searchNode(node.row - 1,node.column - 1) != None:
#     last_D = a.lastCell_UL(node.row - 1,node.column - 1,node.value)
#     if last_D:
#         row = last_D.row
#         column = last_D.column
# print('\nult pos')
# print(row,column)

if m.searchNode(node.row,node.column) != None and m.searchNode(node.row + 1,node.column + 1) != None:
    last_D = a.lastCell_DR(node.row + 1,node.column + 1,node.value)
    if last_D:
        row = last_D.row
        column = last_D.column
print('\nult pos')
print(row,column)