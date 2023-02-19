import xml.etree.ElementTree as ET
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample
from Nodes.Organism import Cell,Sample,Organism
from Matrix.Matrix import Matrix

class Read:
    def __init__(self) -> None:
        self.m = Matrix()

    def readFile(self,routeFile):
        self.tree = ET.parse(routeFile)
        self.root = self.tree.getroot()

    def getOrganismList(self,llOrg):
        for organisms in self.root[0]:
            llOrg.insertOrganism(Organism(organisms[0].text,organisms[1].text))
        return llOrg
    
    def getSamplesList(self,llSamp,llOrg):
        print()
        for samples in self.root[1]:
            llSamp.insertSample(Sample(samples[0].text,samples[1].text,samples[2].text,samples[3].text))
            cell = samples[4]
            for livingCell in cell:
                llSamp.last.sample.liveCells.insertCell(Cell(livingCell[0].text,livingCell[1].text,llOrg.validateStatement(livingCell[2].text)))
                self.m.insert(int(livingCell[0].text),int(livingCell[1].text),int(llOrg.validateStatement(livingCell[2].text)))
        return llSamp

read = Read()
read.readFile('Entrada.xml')

llOrg : LinkedListOrganism = read.getOrganismList(LinkedListOrganism())
llOrg.iterateList()
llSamp : LinkedListSample = read.getSamplesList(LinkedListSample(),llOrg)
llSamp.iterateList()

read.m.printMatrix()