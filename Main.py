from Matrix.Matrix import SparseMatrix
from Algorithm.Algorithm import Algorithm
from Algorithm.Graph import Graph
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.Organism import Organism
from Algorithm.Output import Output

a = Algorithm(SparseMatrix())
organisms = LinkedListOrganism()
organisms.insertOrganism(Organism(1,'Organismo A','#E6B8AF'))
organisms.insertOrganism(Organism(2,'Organismo B','#F4CCCC'))
organisms.insertOrganism(Organism(3,'Organismo C','#FCE5CD'))

a.matrix.insert(10,10,1)
a.matrix.insert(10,11,1)
a.matrix.insert(10,12,1)
a.matrix.insert(10,13,1)
a.matrix.insert(11,10,1)
a.matrix.insert(11,11,1)
a.matrix.insert(11,12,1)

a.matrix.insert(9,11,3)
a.matrix.insert(9,12,3)

# a.matrix.insert(12,11,2)
# a.matrix.insert(12,12,2)

#a.matrix.insert(3,1,2)

a.matrix.insert(2,2,2)
a.matrix.insert(2,3,2)
a.matrix.insert(2,4,2)
a.matrix.insert(2,5,2)
a.matrix.insert(2,6,2)
a.matrix.insert(2,7,2)
a.matrix.insert(2,8,2)

a.matrix.insert(3,8,2)
a.matrix.insert(4,8,2)
a.matrix.insert(5,8,2)
a.matrix.insert(6,8,2)
a.matrix.insert(7,8,2)
a.matrix.insert(8,8,2)

a.matrix.insert(8,7,2)
a.matrix.insert(8,6,2)
a.matrix.insert(8,5,2)
a.matrix.insert(8,4,2)
a.matrix.insert(8,3,2)

a.matrix.insert(8,2,2)
a.matrix.insert(7,2,2)
a.matrix.insert(6,2,2)
a.matrix.insert(5,2,2)
a.matrix.insert(4,2,2)
a.matrix.insert(3,2,2)

# #
a.matrix.insert(3,3,1)
a.matrix.insert(3,4,1)
a.matrix.insert(3,5,1)
a.matrix.insert(3,6,1)
a.matrix.insert(3,7,1)
a.matrix.insert(4,3,1)
a.matrix.insert(4,4,1)
a.matrix.insert(4,5,1)
a.matrix.insert(4,6,3)
a.matrix.insert(4,7,1)

a.matrix.insert(5,3,1)
a.matrix.insert(5,4,1)
a.matrix.insert(5,6,1)
a.matrix.insert(5,7,1)

a.matrix.insert(6,3,1)
a.matrix.insert(6,4,1)
a.matrix.insert(6,5,1)
a.matrix.insert(6,6,1)
a.matrix.insert(6,7,1)
a.matrix.insert(7,3,1)
a.matrix.insert(7,4,1)
a.matrix.insert(7,5,1)
a.matrix.insert(7,6,1)
a.matrix.insert(7,7,1)

#a.matrix.insert(9,10,3)
# a.matrix.print()
# if a.searchLive(2):
#     print('prospera')
# else:
#     print('no prospera')

# posibilities = a.getPosibilities(2)
# print('2 prospera en las coordenadas:')
#posibilities.iterateList()

# g = Graph()
# AQUÍ COMIENZA EL CÓDIGO
# a.matrix.insert(7,9,2) #INSERCIÓN
# g.setOrganism(organisms)
# graph1 = g.getMatrixI(a.matrix,7,9)
# a.evaluateToEat(a.matrix.searchNode(7,9))
# graph2 = g.getMatrixF(a.matrix)
# g.getDot('file',graph1,graph2)
#a.matrix.insert(12,9,3) #INSERCIÓN
#g.setOrganism(organisms)
#graph1 = g.getMatrixI(a.matrix,12,9)
#a.evaluateToEat(a.matrix.searchNode(12,9))
#graph2 = g.getMatrixF(a.matrix)
#g.getDot('file1',graph1,graph2)
#Output().getXML(organisms)

print(Output().getXML(organisms,'nueva muestra',a.matrix))