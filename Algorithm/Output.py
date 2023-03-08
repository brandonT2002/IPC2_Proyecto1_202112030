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
        row = ET.SubElement(Samp,'filas')
        column = ET.SubElement(Samp,'columnas')
        listLiveCell = ET.SubElement(Samp,'listadoCeldasVivas')

        currentR : HeaderNode = matrix.accessR.first
        maxColumn : HeaderNode = matrix.accessC.last
        currentC : InternalNode
        row.text = str(matrix.accessR.last.index)
        column.text = str(matrix.accessC.last.index)
        while currentR:
            currentC = currentR.access
            while currentC:
                cell =ET.SubElement(listLiveCell,'celdaViva')
                ET.SubElement(cell,'fila').text=f'{currentC.row}'
                ET.SubElement(cell,'columna').text=f'{currentC.column}'
                ET.SubElement(cell,'codigoOrganismo').text=f'{currentC.value}'
                currentC = currentC.right
            currentR = currentR.next
        
        # file = ET.ElementTree(root)

        file = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
        return open('Output/Salida.xml','w').write(file)