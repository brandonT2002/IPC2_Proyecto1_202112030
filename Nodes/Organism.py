class Sample:
    def __init__(self,code,description,row,column,liveCells):
        self.code = code
        self.description = description
        self.row = row
        self.column = column
        self.liveCells = liveCells

class Organism:
    def __init__(self,code,name):
        self.code = code
        self.name = name

class Cell:
    def __init__(self,row,column,type):
        self.row = row
        self.column = column
        self.type = type