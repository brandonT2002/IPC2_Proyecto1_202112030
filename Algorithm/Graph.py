from Matrix.Matrix import SparseMatrix
from Matrix.HeaderNode import HeaderNode
from Matrix.InternalNode import InternalNode
from Nodes.LinkedListOrganism import LinkedListOrganism
import os
import webbrowser

class Graph:
    def setOrganism(self,organisms):
        self.organisms = organisms

    def getMatrixI(self,matrixI,row = -1,col = -1):
        self.rowI = row
        self.colI = col
        dot = 'matrizInicial [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">\n'
        dot += self.sparseMatrix(self.organisms,matrixI)
        dot += '</TABLE>>];'
        return dot

    def getMatrixF(self,matrixF,row = -1,col = -1):
        self.rowI = row
        self.colI = col
        dot = 'matrizFinal [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">\n'
        dot += self.sparseMatrix(self.organisms,matrixF)
        dot += '</TABLE>>];'
        return dot

    def getDot(self,name,dotI,dotF = None):
        dot = 'digraph html {\n'

        dot += dotI

        if dotF:
            dot += dotF

        dot += '\norganismos [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="5" CELLPADDING="20">'
        current = self.organisms.first
        while current:
            dot += f'\n<tr>\n<td BGCOLOR="{current.organism.color}" width="60" height="60">{current.organism.name} - {current.organism.code}</td>\n</tr>'
            current = current.next
        dot += '\n</TABLE>>];'
        dot += '\n}'

        with open(f'Dot/{name}.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system(f'dot -Tpdf Dot/{name}.txt -o Dot/{name}.pdf')
        webbrowser.open(f'Dot\{name}.pdf')

    def sparseMatrix(self,organisms,matrix : SparseMatrix):
        temp = SparseMatrix()
        node : InternalNode
        for i in range(1,matrix.accessR.last.index + 1):
            for j in range(1,matrix.accessC.last.index + 1):
                node = matrix.searchNode(i,j)
                if node:
                    temp.insert(i,j,node.value)
                else:
                    temp.insert(i,j,0)
        return self.sparseMatrix_1(organisms,temp)

    def sparseMatrix_1(self,organisms : LinkedListOrganism, matrix : SparseMatrix):
        dot = ''
        currentR : HeaderNode = matrix.accessR.first
        enumerateC = '<td BGCOLOR="white" width="60" height="60" border="0">0</td>'
        while currentR:
            currentC = currentR.access
            dot += f'<tr><td BGCOLOR="white" width="60" height="60" border="0">{currentR.index}</td>'
            while currentC:
                border = '1'
                if currentR.index == self.rowI and currentC.column == self.colI:
                    border = '5'
                dot += f'<td BGCOLOR="{self.getOrganismColor(currentC.value,organisms.first)}" width="60" height="60" border="{border}"></td>\n'
                currentC = currentC.right
            currentR = currentR.next
            dot += '</tr>'
        currentC = HeaderNode = matrix.accessC.first
        while currentC:
            enumerateC += f'<td BGCOLOR="white" width="60" height="60" border="0">{currentC.index}</td>'
            currentC = currentC.next
        return f'<tr>{enumerateC}</tr> {dot}'
    
    def getOrganismColor(self,value,currentO):
        while currentO:
            if value == currentO.organism.code:
                return currentO.organism.color
            elif value == 0:
                return "white"
            currentO = currentO.next