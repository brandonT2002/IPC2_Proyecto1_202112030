import easygui as eg
from readFile import Read
from Nodes.LinkedListOrganism import LinkedListOrganism
from Nodes.LinkedListSample import LinkedListSample

class Menu:
    def __init__(self):
        self.read = Read()

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
                        llOrg : LinkedListOrganism = self.read.getOrganismList(LinkedListOrganism())
                        llSamp : LinkedListSample = self.read.getSamplesList(LinkedListSample(),llOrg)
                        print('Archivo cargado exitosamente')
                    except:
                        print('Ocurrió un error :(')
                elif option == '2':
                    self.read.m.print()
                elif option == '3':
                    print('¡Hasta pronto!')
                    break
                else:
                    print('Opción fuera de rango')
            else:
                print('Ingrese solo números')

    def options(self):
        print('╔════════════════════════════════════════════════════════════╗')
        print('║                                                            ║')
        print('║                       MENÚ PRINCIPAL                       ║')
        print('║                    1. Cargar Archivo                       ║')
        print('║                    2. Ver Muestras                         ║')
        print('║                    3. Salir                                ║')
        print('║                                                            ║')
        print('╚════════════════════════════════════════════════════════════╝')

menu = Menu()
menu.menu()