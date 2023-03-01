from Nodes.LinkedListCell import LinkedListCell
class Organism:
    def __init__(self,code,name,color):
        self.code = code
        self.name = name
        self.color = color

class Sample:
    def __init__(self,code,description,row,column):
        self.code = code
        self.description = description
        self.row = row
        self.column = column
        self.liveCells : LinkedListCell = LinkedListCell()

class Cell:
    def __init__(self,row,column,organism):
        self.row = row
        self.column = column
        self.organism : Organism = organism