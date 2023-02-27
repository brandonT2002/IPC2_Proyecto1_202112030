class Menu:
    def __init__(self):
        #self.read = Read()
        pass

    def menu(self):
        while True:
            print()
            self.options()
            option = input('Opción: ')
            print()
            if option.isdigit():
                if option == '1':
                    try:
                        print('opcion1')
                    except:
                        print('Ocurrió un error :(')
                elif option == '2':
                    print('opcion2')
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