import xml.etree.ElementTree as ET
from Nodes.Organism import Cell,Sample,Organism
from Algorithm.Algorithm import Algorithm
from Color import Color
import random

class Read:
    def __init__(self,algorithm):
        self.color = Color()
        self.algorithm : Algorithm = algorithm

    def readFile(self,routeFile):
        self.tree = ET.parse(routeFile)
        self.root = self.tree.getroot()

    def getOrganismList(self,llOrg):
        for organisms in self.root[0]:
            if not llOrg.existOrganism(organisms[0].text):
                llOrg.insertOrganism(Organism(organisms[0].text,organisms[1].text,self.color.colors.pop()))
        return llOrg
    
    def getSamplesList(self,llSamp,llOrg):
        for samples in self.root[1]:
            llSamp.insertSample(Sample(samples[0].text,samples[1].text,samples[2].text,samples[3].text))
            cell = samples[4]
            for livingCell in cell:
                llSamp.last.sample.liveCells.insertCell(Cell(livingCell[0].text,livingCell[1].text,llOrg.validateStatement(livingCell[2].text)))
                self.algorithm.matrix.overWrite(int(livingCell[0].text),int(livingCell[1].text),llOrg.validateStatement(livingCell[2].text))
        return llSamp
    
    def generateColor(self):
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        color = str(color)
        color = color.replace('[\'','')
        color = color.replace('\']','')
        return color