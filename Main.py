from Nodes.LinkedListSample import LinkedListSample
from Nodes.LinkedListCell import LinkedListCell
from Nodes.Organism import Cell,Sample

celda0 = Cell(4,4,1)
celda1 = Cell(4,5,2)
celda2 = Cell(5,4,2)

ls1 = LinkedListCell()
ls1.insertCell(celda0)

ls2 = LinkedListCell()
ls2.insertCell(celda1)
ls2.insertCell(celda2)

muestra1 = Sample(1,'Epidemia mst1',1,1,ls1)
muestra2 = Sample(2,'Epidemia mst2',2,2,ls2)

spl1 = LinkedListSample()
spl1.insertSample(muestra1)
spl1.insertSample(muestra2)
spl1.iterateList()