import xml.etree.ElementTree as ET

class Read:
    def getContent(self,routeFile):
        tree = ET.parse(routeFile)
        root = tree.getroot()

        for organisms in root[0]:
            print(f'Código Org: {organisms[0].text} Tipo Org: {organisms[1].text}')

        print()
        for samples in root[1]:
            print(f'Código Org: {samples[0].text}')
            print(f'Descripción: {samples[1].text}')
            print(f'Dimensión Muestra: {samples[2].text}x{samples[3].text}')
            cell = samples[4]
            for livingCell in cell:
                print(f'F: {livingCell[0].text} C: {livingCell[1].text}')
            print()

read = Read()
read.getContent('Entrada.xml')