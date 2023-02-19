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
m = Matrix()
m.insert(3,3,2)
m.insert(2,2,1)
m.insert(1,2,3)
m.insert(2,5,3)
m.insert(5,3,4)
m.insert(4,7,2)
m.insert(6,5,2)
m.insert(7,7,8)
m.printMatrix()