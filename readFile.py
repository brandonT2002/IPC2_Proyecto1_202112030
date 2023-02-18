import xml.etree.ElementTree as ET
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample
from Nodes.Organism import Cell,Sample,Organism

class Read:
    def readFile(self,routeFile):
        self.tree = ET.parse(routeFile)
        self.root = self.tree.getroot()

    def getOrganismList(self,llOrg):
        for organisms in self.root[0]:
            llOrg.insertOrganism(Organism(organisms[0].text,organisms[1].text))
            #print(f'Código Org: {organisms[0].text} Nombre Org: {organisms[1].text}')
        return llOrg
    
    def getSamplesList(self,llSamp,llOrg):
        print()
        for samples in self.root[1]:
            #print(f'Código Org: {samples[0].text}')
            #print(f'Descripción: {samples[1].text}')
            #print(f'Dimensión Muestra: {samples[2].text}x{samples[3].text}')
            llSamp.insertSample(Sample(samples[0].text,samples[1].text,samples[2].text,samples[3].text))
            cell = samples[4]
            for livingCell in cell:
                llSamp.last.sample.liveCells.insertCell(Cell(livingCell[0].text,livingCell[1].text,llOrg.validateStatement(livingCell[2].text)))
                #print(f'F: {livingCell[0].text} C: {livingCell[1].text}')
                #print(f'Código Org: {livingCell[2].text}')
            #print()
        return llSamp

read = Read()
read.readFile('Entrada.xml')

llOrg : LinkedListOrganism = read.getOrganismList(LinkedListOrganism())
llOrg.iterateList()
llSamp : LinkedListSample = read.getSamplesList(LinkedListSample(),llOrg)
llSamp.iterateList()