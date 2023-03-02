import xml.etree.ElementTree as ET
import xml.dom.minidom
from Nodes.LinkedListOrganism import LinkedListOrganism
from Matrix.Matrix import SparseMatrix
from Matrix.HeaderNode import HeaderNode
from Matrix.InternalNode import InternalNode
import uuid

class Output:
    def getXML(self,organisms : LinkedListOrganism,description,matrix : SparseMatrix):

        root = ET.Element('datosMarte')
        listOrg = ET.SubElement(root,'listaOrganismos')

        currentO = organisms.first
        while currentO:
            organism = ET.SubElement(listOrg,'organismo')
            ET.SubElement(organism,'codigo').text=f'{currentO.organism.code}'
            ET.SubElement(organism,'nombre').text=f'{currentO.organism.name}'
            currentO = currentO.next

        listSamp = ET.SubElement(root,'listadoMuestras')
        Samp = ET.SubElement(listSamp,'muestra')
        ET.SubElement(Samp,'codigo').text=f'{uuid.uuid4()}'
        ET.SubElement(Samp,'descripcion').text=f'{description}'
        row = ET.SubElement(Samp,'Filas')
        column = ET.SubElement(Samp,'columnas')
        listLiveCell = ET.SubElement(Samp,'listadoCeldasVivas')

        currentR : HeaderNode = matrix.accessR.first
        maxColumn : HeaderNode = matrix.accessC.last
        currentC : InternalNode
        while currentR:
            currentC = currentR.access
            while currentC:
                cell =ET.SubElement(listLiveCell,'celdaViva')
                ET.SubElement(cell,'fila').text=f'{currentC.row}'
                ET.SubElement(cell,'columna').text=f'{currentC.column}'
                ET.SubElement(cell,'codigoOrganismo').text=f'{currentC.value}'
                if currentC.row == currentR.last.row and currentC.column == maxColumn.last.column:
                    row.text=f'{currentC.row}'
                    column.text=f'{currentC.column}'
                currentC = currentC.right
            currentR = currentR.next
        
        # file = ET.ElementTree(root)

        file = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
        return open('Resource/Salida.xml','w').write(file)