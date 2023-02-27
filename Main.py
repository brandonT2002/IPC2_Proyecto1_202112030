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

print('\nNuevo')
m.insert(1,3,1)
a.matrix.print()

node1 = m.searchNode(1,3)

#print('\n',node.toString(0))
#print(node.__dict__)

def evaluar(node):
    if node.right != None and node.column == node.right.column - 1:
        last_R = a.lastCell_R(node.right,node.value)
        if last_R:
            print('\nComer Org Der')
            a.eatOrganisms_R(node,last_R,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera Der')
            m.print()

    if node.left != None and node.column == node.left.column + 1:
        last_L = a.lastCell_L(node.left,node.value)
        if last_L:
            print('\nComer Org Izq')
            a.eatOrganisms_L(node,last_L,node.value)
            print(last_L.row,last_L.column)
            m.print()
        else:
            print('\nEl organismo no prospera Izq')
            m.print()

    if node.up != None and node.row == node.up.row + 1:
        last_U = a.lastCell_U(node.up,node.value)
        if last_U:
            print('\nComer Org Arr')
            a.eatOrganisms_U(node,last_U,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera Arr')

    if node.down != None and node.row == node.down.row - 1:
        last_D = a.lastCell_D(node.down,node.value)
        if last_D:
            print('\nComer Org Abj')
            a.eatOrganisms_D(node,last_D,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera Abj')


    if m.searchNode(node.row,node.column) != None and m.searchNode(node.row - 1,node.column + 1) != None:
        last_UR = a.lastCell_UR(node.row - 1,node.column + 1,node.value)
        if last_UR:
            print('\nComer Org ArDer')
            a.eatOrganisms_UR(node.row,node.column,last_UR.row,last_UR.column,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera ADer')
    else:
        print('\nEl organismo no prospera ADer')

    if m.searchNode(node.row,node.column) != None and m.searchNode(node.row - 1,node.column - 1) != None:
        last_UL = a.lastCell_UL(node.row - 1,node.column - 1,node.value)
        if last_UL:
            print('\nComer Org ArIzq')
            a.eatOrganisms_UL(node.row,node.column,last_UL.row,last_UL.column,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera AIzq')
    else:
        print('\nEl organismo no prospera AIzq')

    if m.searchNode(node.row,node.column) != None and m.searchNode(node.row + 1,node.column + 1) != None:
        last_DR = a.lastCell_DR(node.row + 1,node.column + 1,node.value)
        if last_DR:
            print('\nComer Org AbDer')
            a.eatOrganisms_DR(node.row,node.column,last_DR.row,last_DR.column,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera AbDer')
    else:
        print('\nEl organismo no prospera AbDer')

    if m.searchNode(node.row,node.column) != None and m.searchNode(node.row + 1,node.column - 1) != None:
        last_DL = a.lastCell_DL(node.row + 1,node.column - 1,node.value)
        if last_DL:
            print('\nComer Org AbIzq')
            a.eatOrganisms_DL(node.row,node.column,last_DL.row,last_DL.column,node.value)
            m.print()
        else:
            print('\nEl organismo no prospera AbIzq')
    else:
        print('\nEl organismo no prospera AbIzq')

evaluar(node1)

m.insert(5,5,1)
node2 = m.searchNode(5,5)
evaluar(node2)