import easygui as eg
from readFile import Read
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample
from Algorithm.Algorithm import Algorithm
from Algorithm.Graph import Graph
from Algorithm.Output import Output
from Matrix.Matrix import SparseMatrix

class Menu:
    def __init__(self):
        self.initObjects()

    def initObjects(self):
        self.algorithm = Algorithm(SparseMatrix())
        self.read = Read(self.algorithm)
        self.llOrg = LinkedListOrganism()
        self.llSamp = LinkedListSample()
        self.graph = Graph()
        self.resetScripts()

    def menu(self):
        while True:
            print()
            self.options()
            option = input('Opción: ')
            print()
            if option.isdigit():
                if option == '1':
                    try:
                        file = eg.fileopenbox()
                        self.read.readFile(file)
                        self.llOrg : LinkedListOrganism = self.read.getOrganismList(self.llOrg)
                        self.llSamp : LinkedListSample = self.read.getSamplesList(self.llSamp,self.llOrg)

                        self.graph.setOrganism(self.llOrg)
                        self.graph.getDot('Muestra',self.graph.getMatrixI(self.algorithm.matrix))
                        print('Archivo cargado exitosamente')
                    except:
                        print('Ocurrió un error :(')
                elif option == '2':
                    print('opcion2')
                elif option == '3':
                    if self.llOrg.first and self.llSamp.first:
                        self.addOrganism()
                    else:
                        print('No se ha cargado ningún archivo')
                elif option == '4':
                    if self.llOrg.first and self.llSamp.first:
                        organism = input('Ingrese el código de Organismo: ')
                        if self.algorithm.searchLive(organism):
                            print('Todavía puede prosperar')
                        else:
                            print('Ya no puede prosperar')
                    else:
                        print('No se ha cargado ningún archivo')
                elif option == '5':
                    self.initObjects()
                    self.resetScripts()
                    print('El sistema ha sido restaurado')
                elif option == '6':
                    self.resetScripts()
                    print('¡Hasta pronto!')
                    break
                else:
                    print('Opción fuera de rango')
            else:
                print('Ingrese solo números')

    def addOrganism(self):
        while True:
            option = input('\n¿Desea ingresar un orgamismo? (s/n): ')
            if option == 's':
                self.insertOrgasim()
            elif option == 'n':
                option = input('\n¿Generar archivo XML? (s/n): ')
                if option == 's':
                    description = input('Descripción de la muestra: ')
                    Output().getXML(self.llOrg,description,self.algorithm.matrix)
                    break
                elif option == 'n':
                    break
                else:
                    print('Opción invalida')
            else:
                print('Opción invalida')

    def insertOrgasim(self):
        while True:
            row = input('Fila: ')
            column = input('Columna: ')
            if row.isdigit() and column.isdigit() and (int(row) > 0 or int(column) > 0):
                value = input('Tipo de Organismo: ')
                if self.algorithm.exist(value,self.llOrg):
                    if self.algorithm.matrix.insertNew(int(row),int(column),value):
                        print()
                        self.graph.setOrganism(self.llOrg)
                        graph1 = self.graph.getMatrixI(self.algorithm.matrix,int(row),int(column))
                        self.algorithm.evaluateToEat(self.algorithm.matrix.searchNode(int(row),int(column)))
                        graph2 = self.graph.getMatrixF(self.algorithm.matrix)
                        self.graph.getDot('Resultado',graph1,graph2)

                        self.graph.setOrganism(self.llOrg)
                        self.graph.getDot('Muestra',self.graph.getMatrixI(self.algorithm.matrix))
                        break
                    else:
                        print('No se pueden agregar organismos en celdas vivas')
                else:
                    print('El tipo de organismo no existe')
            else:
                print('Valores incorrectos')

    def resetScripts(self):
        file = open('Reports/js/scriptOrigin.js','wt')
        text = f'd3.select(\'#original\').graphviz().scale(.6).height(document.getElementById(\'original\').innerHTML = "<table><tr><th> No hay muestras cargadas </th></tr></table>")'
        file.write(text)
        file.close()

        file = open('Reports/js/scriptResult.js','wt')
        text = f'd3.select(\'#resultado\').graphviz().scale(.45).height(document.getElementById(\'resultado\').innerHTML = "<table><tr><th> No se han agregado organismos </th></tr></table>")'
        file.write(text)
        file.close()

    def options(self):
        print('╔════════════════════════════════════════════════════════════╗')
        print('║                                                            ║')
        print('║                       MENÚ PRINCIPAL                       ║')
        print('║                  1. Cargar Archivo                         ║')
        print('║                  2. ¿Dónde Puede Prosperar?                ║')
        print('║                  3. Colocar Organismos                     ║')
        print('║                  4. ¿Puéde Prosperar?                      ║')
        print('║                  5. Limpiar Sistema                        ║')
        print('║                  6. Salir                                  ║')
        print('║                                                            ║')
        print('╚════════════════════════════════════════════════════════════╝')