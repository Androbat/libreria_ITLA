class Catalogo:

    def __init__(self):

        self.libros = {"dan brown":["Digital Fortress"]}
    
        self.audio_libros = [
            {'Nombre:': ['El Cambio'], 'Autor:':['Wayne Dyer']}
        ]


    def menu_catalogo(self):
        print("""

            Bienvenido a la libreria ITLA

            1-Mostrar Libros

            2-Mostrar Audiolibros

            3-Mostrar catalogo completo

            4-Agregar Libro

            5-Agregar Audiolibro

            6-Volver al menu principal

            7-Salir
                """)

        opcion = input("Elija una opcion: ")
        if opcion == '1':
            self.mostrar_libros()
        elif opcion == '2':
            self.mostrar_audio_libros()
        elif opcion == '3':
            self.mostrar_catalogo()
        elif opcion == '4':
            self.agregar_libro()
        elif opcion == '5':
            self.agregar_audio_libro()
        elif opcion == '6':
            self.ir_al_menu_principal()
        elif opcion == '7':
            exit()


    def agregar_libro(self):
        # Encuentra una forma de agregar una nueva key, value al dict.
        agregar_autor = input("agregue autor: ")
        agregar_nombre = input('Agregue un nombre: ')
        

        if agregar_autor in self.libros:
            self.libros[agregar_autor].append(agregar_nombre)
        else:
            self.libros[agregar_autor] = []
            self.libros[agregar_autor].append(agregar_nombre)

        print(self.libros)
    def mostrar_libros(self):
        # Mostrar libro
        for key, value in self.libros[0].items():
            print(key, value)


    def mostrar_audio_libros(self):

        for key, value in self.audio_libros[0].items():
            print(key, value)

    def agregar_audio_libro(self):
        agrega_nombre = input('Agrega un audio libro: ')
        agrega_autor = input('Agrega el autor del libro agregado: ')
        self.audio_libros[0].append(agrega_nombre)
        self.audio_libros[1].append(agrega_autor)


    def mostrar_catalogo(self):
        print()


        #print('Audio libros: {}'.format(self.audio_libros))
    def prestar_libros(self):
        pass

    def ir_al_menu_principal(self):
        pass


cliente = Catalogo()
cliente.menu_catalogo()
