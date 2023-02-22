# from Nodes.LinkedListSample import LinkedListSample
# from Nodes.Organism import Cell,Sample,Organism

# organismo1 = Organism(1,'OrganismoA',)

# spl1 = LinkedListSample()

# spl1.insertSample(Sample(1,'Epidemia mst1',1,1))
# spl1.last.liveCells.insertCell(Cell(4,4,organismo1))

# spl1.insertSample(Sample(2,'Epidemia mst2',2,2))
# spl1.last.liveCells.insertCell(Cell(4,5,organismo1))
# spl1.last.liveCells.insertCell(Cell(5,4,organismo1))

# spl1.iterateList()

from Matrix.Matrix import Matrix
from Algorithm.Algorithm import Algorithm
m = Matrix()
m.insert(5,6,1)
m.insert(5,7,1)
m.insert(5,8,1)
m.insert(5,9,1)
m.insert(5,10,1)

m.insert(6,6,1)
m.insert(7,6,1)
m.insert(8,6,1)

m.insert(9,6,1)
m.insert(9,7,1)
m.insert(9,8,1)
m.insert(9,9,1)
m.insert(9,10,1)

m.insert(6,10,1)
m.insert(7,10,1)
m.insert(8,10,1)

m.insert(6,7,2)
m.insert(6,8,2)
m.insert(6,9,2)

m.insert(8,7,2)
m.insert(8,8,2)
m.insert(8,9,2)

m.printMatrix()

a = Algorithm(m)
node = m.searchNode(6,7)
node.value = 2
m.printMatrix()

print(node.row,node.column,node.value)
# analizar a la derecha
last_R = a.lastCell_R(node.right,node.value)
row = -1
column = -1
if last_R:
    row = last_R.row
    column = last_R.column
print('derecha')
print(row,column)

# analizar a la izquierda
last_L = a.lastCell_L(node.left,node.value)
row = -1
column = -1
if last_L:
    row = last_L.row
    column = last_L.column
print('izquierda')
print(row,column)

# analizar hacia arriba
last_u = a.lastCell_U(node.up,node.value)
row = -1
column = -1
if last_u:
    row = last_u.row
    column = last_u.column
print('arriba')
print(row,column)

# analizar hacia abajo
last_d = a.lastCell_D(node.down,node.value)
row = -1
column = -1
if last_d:
    row = last_d.row
    column = last_d.column
print('abajo')
print(row,column)

# analizar arriba a la derecha
if node.up:
    last_ur = a.lastCell_UR(node.up.right,node.value)
    row = -1
    column = -1
    if last_ur:
        row = last_ur.row
        column = last_ur.column
    print('arriba-derecha')
    print(row,column)

# analizar arriba a la izquierda
if node.up:
    last_ul = a.lastCell_UL(node.up.left,node.value)
    row = -1
    column = -1
    if last_ul:
        row = last_ul.row
        column = last_ul.column
    print('arriba-izquierda')
    print(row,column)

# analizar abajo a la derecha
if node.down:
    last_dr = a.lastCell_DR(node.down.right,node.value)
    row = -1
    column = -1
    if last_dr:
        row = last_dr.row
        column = last_dr.column
    print('abajo-derecha')
    print(row,column)

# analizar abajo a la izquierda
if node.down:
    last_dl = a.lastCell_DL(node.down.left,node.value)
    row = -1
    column = -1
    if last_dl:
        row = last_dl.row
        column = last_dl.column
    print('abajo-izquierda')
    print(row,column)