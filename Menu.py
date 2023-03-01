import easygui as eg
from readFile import Read
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample
from Algorithm.Algorithm import Algorithm
from Algorithm.Graph import Graph
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
                    print('opcion4')
                elif option == '5':
                    print('¡Hasta pronto!')
                    break
                else:
                    print('Opción fuera de rango')
            else:
                print('Ingrese solo números')

    def addOrganism(self):
        while True:
            option = input('\nDesea ingresar un orgamismo (s/n)? ')
            if option == 's':
                self.graph.setOrganism(self.llOrg)
                self.graph.getDot('Muestra',self.graph.getMatrixI(self.algorithm.matrix))
                while True:
                    row = input('Fila: ')
                    column = input('Columna: ')
                    if row.isdigit() and column.isdigit():
                        value = input('Tipo de Organismo: ')
                        if self.algorithm.matrix.insertNew(int(row),int(column),value):
                            print()
                            self.algorithm.matrix.insert(int(row),int(column),value)
                            self.graph.setOrganism(self.llOrg)
                            graph1 = self.graph.getMatrixI(self.algorithm.matrix,int(row),int(column))
                            self.algorithm.evaluateToEat(self.algorithm.matrix.searchNode(int(row),int(column)))
                            graph2 = self.graph.getMatrixF(self.algorithm.matrix)
                            self.graph.getDot('Resultado',graph1,graph2)
                            break
                        else:
                            print('No se pueden agregar organismos en celdas vivas')
                    else:
                        print('Valores incorrectos')
            elif option == 'n':
                break
            else:
                print('Opción invalida')

    def options(self):
        print('╔════════════════════════════════════════════════════════════╗')
        print('║                                                            ║')
        print('║                       MENÚ PRINCIPAL                       ║')
        print('║                  1. Cargar Archivo                         ║')
        print('║                  2. ¿Dónde Puede Prosperar?                ║')
        print('║                  3. Colocar Organismos                     ║')
        print('║                  4. ¿Puéde Prosperar?                      ║')
        print('║                  5. Salir                                  ║')
        print('║                                                            ║')
        print('╚════════════════════════════════════════════════════════════╝')

menu = Menu()
menu.menu()