import easygui as eg
from readFile import Read
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample

class Menu:
    def __init__(self):
        self.read = Read()

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
                        llOrg : LinkedListOrganism = self.read.getOrganismList(LinkedListOrganism())
                        llSamp : LinkedListSample = self.read.getSamplesList(LinkedListSample(),llOrg)
                        print('Archivo cargado exitosamente')
                    except:
                        print('Ocurrió un error :(')
                elif option == '2':
                    print('opcion2')
                elif option == '3':
                    if file:
                        self.read.m.print()
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
                x = int(input('PosX: '))
                y = int(input('PosY: '))
                value = int(input('Tipo de Organismo: '))
                print()
                self.read.m.insert(x,y,value)
                self.read.m.print()
                nodo = self.read.m.searchNode(x,y)
                self.read.algorithm.evaluateToEat(nodo)
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