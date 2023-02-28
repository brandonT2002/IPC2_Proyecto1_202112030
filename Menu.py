import easygui as eg
from readFile import Read
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample
from Algorithm.Algorithm import Algorithm
from Matrix.Matrix import SparseMatrix

class Menu:
    def __init__(self):
        self.algorithm = Algorithm(SparseMatrix())
        self.read = Read(self.algorithm)
        self.llOrg = None
        self.llSamp = None

    def menu(self):
        file = False
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
                        self.llOrg : LinkedListOrganism = self.read.getOrganismList(LinkedListOrganism())
                        self.llSamp : LinkedListSample = self.read.getSamplesList(LinkedListSample(),self.llOrg)
                        print('Archivo cargado exitosamente')
                    except:
                        print('Ocurrió un error :(')
                elif option == '2':
                    print('opcion2')
                elif option == '3':
                    if file:
                        self.algorithm.matrix.print()
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
                while True:
                    x = input('PosX: ')
                    y = input('PosY: ')
                    if x.isdigit() and y.isdigit():
                        value = input('Tipo de Organismo: ')
                        print()
                        self.algorithm.matrix.insert(int(x),int(y),value)
                        self.algorithm.matrix.print()
                        self.algorithm.evaluateToEat(self.algorithm.matrix.searchNode(int(x),int(y)))
                        break
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