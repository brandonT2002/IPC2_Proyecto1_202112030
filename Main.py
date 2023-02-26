from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm

m = SparseMatrix()
m.insert(2,3,1)
m.insert(3,3,2)
m.insert(4,3,2)

m.insert(6,3,2)
m.insert(7,3,2)
m.insert(8,3,1)

print('\nOriginal')
m.print()
a = Algorithm(m)

print('\nNuevo')
m.insert(5,3,1)
a.matrix.print()

node = m.searchNode(5,3)
#print('\n',node.toString(0))
#print(node.__dict__)
row = -1
column = -1
# if node.right != None and node.column == node.right.column - 1:
#     last_R = a.lastCell_R(node.right,node.value)
#     if last_R:
#         print('\nComer Org Der')
#         a.eatOrganisms_R(node.right,last_R,node.value)
#         row = last_R.row
#         column = last_R.column
#         m.print()
#     else:
#         print('\nEl organismo no prospera Der')
#         m.print()

# row = -1
# column = -1
# if node.left != None and node.column == node.left.column + 1:
#     last_L = a.lastCell_L(node.left,node.value)
#     if last_L:
#         print('\nComer Org Izq')
#         a.eatOrganisms_L(node.left,last_L,node.value)
#         row = last_L.row
#         column = last_L.column
#         m.print()
#     else:
#         print('\nEl organismo no prospera Izq')
#         m.print()

if node.up != None and node.row == node.up.row + 1:
    last_U = a.lastCell_U(node.up,node.value)
    if last_U:
        print('\nComer Org Arr')
        a.eatOrganisms_U(node.up,last_U,node.value)
        row = last_U.row
        column = last_U.column
        m.print()
    else:
        print('\nEl organismo no prospera Arr')

if node.down != None and node.row == node.down.row - 1:
    last_D = a.lastCell_D(node.down,node.value)
    if last_D:
        print('\nComer Org Abj')
        a.eatOrganisms_D(node.down,last_D,node.value)
        row = last_D.row
        column = last_D.column
        m.print()
    else:
        print('\nEl organismo no prospera Abj')

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

# if m.searchNode(node.row,node.column) != None and m.searchNode(node.row + 1,node.column + 1) != None:
#     last_D = a.lastCell_DR(node.row + 1,node.column + 1,node.value)
#     if last_D:
#         row = last_D.row
#         column = last_D.column
# print('\nult pos')
# print(row,column)

# if m.searchNode(node.row,node.column) != None and m.searchNode(node.row + 1,node.column - 1) != None:
#     last_D = a.lastCell_DL(node.row + 1,node.column - 1,node.value)
#     if last_D:
#         row = last_D.row
#         column = last_D.column
# print('\nult pos')
# print(row,column)