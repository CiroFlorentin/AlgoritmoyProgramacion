import csv


class Menu:
    """Gestiona la presentación y selección de opciones de un menú bancario."""

    # ['1- Gestion de Sucursales','2- Gestion de Articulos','3- Carga de Stock','4- Venta de Articulos','5- Existencia de Mercaderias','6- Salir']
    def __init__(self, nombre: str, opciones: list[str]):
        if not isinstance(opciones, list):
            raise ValueError("El parametro opciones debe ser una lista de opciones")
        self.opciones_menu = opciones
        self.nombre = nombre

    def mostrar_menu(self) -> None:
        """Muestra las opciones del menú en la consola."""
        print(f"\n--- {self.nombre} ---")
        for opcion in self.opciones_menu:
            print(opcion)
        print("---------------------")

    def pedir_opcion_de_menu_valida(self) -> int:
        """Solicita al usuario una opción del menú y la valida."""
        opcion_seleccionada = ''
        num_opciones = len(self.opciones_menu)
        while not opcion_seleccionada.isdigit() or \
                int(opcion_seleccionada) not in range(1, num_opciones + 1):
            opcion_seleccionada = input(f'Seleccione una opción (1-{num_opciones}): ')
            if not opcion_seleccionada.isdigit() or \
                    int(opcion_seleccionada) not in range(1, num_opciones + 1):
                print(f'Opción no válida. Debe ser un número entre 1 y {num_opciones}.')
        return int(opcion_seleccionada)


class Alumno:
    def __init__(self, legajo, nombre, apellido, notas=None):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.nota = notas if notas else []

    def promedio(self):
        if self.nota:
            return sum(self.nota) / len(self.nota)
        else:
            return 0

    def mostrar_notas(self):
        for i, nota in enumerate(self.nota, 1):
            print(f'{i} - {nota}')

    def __str__(self):
        return f'[{self.legajo}] - {self.nombre} {self.apellido} - Promedio: {self.promedio():.2f} '


class GestorAlumno:
    def __init__(self, archivo="alumnos.csv"):
        self.archivo = archivo
        self.lista_alumnos = self.cargar_alumno_desde_csv()

    def cargar_alumno_desde_csv(self):
        alumnos = []
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo_csv:
                reader = csv.DictReader(archivo_csv)
                for fila in reader:
                    legajo = int(fila['legajo'])
                    nombre = fila['nombre']
                    apellido = fila['apellido']
                    notas = [float(n) for n in fila['Notas'].split(';') if n]
                    nuevo_alumno = Alumno(legajo, nombre, apellido, notas)
                    alumnos.append(nuevo_alumno)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo al guardar.")
        return alumnos

    def guardar_alumno_en_csv(self):
        with open(self.archivo, 'w', newline="", encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['legajo', 'nombre', 'apellido', 'Notas', 'Promedio'])
            for alumno in self.lista_alumnos:
                notas_str = ';'.join(str(n) for n in alumno.nota)
                writer.writerow([alumno.legajo, alumno.nombre, alumno.apellido, notas_str, round(alumno.promedio(), 2)])

    def _verificar_legajo(self, legajo):
        for i in self.lista_alumnos:
            if i.legajo == legajo:
                return busqueda_binaria(self.lista_alumnos, legajo)
        return False

    def _promedio_general(self):

        if not self.lista_alumnos:
            return 0
        return round(sum(a.promedio() for a in self.lista_alumnos) / len(self.lista_alumnos), 2)

    def agregar_alumno(self):
        legajo_a_verificar = int(input('Ingresa un numero de legajo: '))
        legajo = self._verificar_legajo(legajo_a_verificar)
        if not legajo:
            nombre = input('Ingrese un nombre: ')
            apellido = input('Ingrese el apellido: ')
            nuevo_alumno = Alumno(legajo_a_verificar, nombre, apellido)
            self.lista_alumnos.append(nuevo_alumno)
            self.guardar_alumno_en_csv()
        else:
            print('El legajo ya existe')

    def agregar_notas(self, legajo_a_verificar):
        if not self.lista_alumnos:
            print('No hay alumnos creados')
            return
        alumno = self._verificar_legajo(legajo_a_verificar)
        if not alumno:
            print('El legajo no existe')
            return
        if len(alumno.nota) < 5:
            for i in range(5):
                while True:
                    nota = input(f'Ingrese la nota {i + 1}: ').replace(',', '.')
                    try:
                        nota = float(nota)
                        if 0 <= nota <= 10:
                            alumno.nota.append(nota)
                            break
                        else:
                            print('Nota no valida (debe ser entre 0 y 10')
                    except ValueError:
                        print('Entrada no válida. Debe ingresar un número.')
            self.guardar_alumno_en_csv()
        elif alumno:
            print('El alumno ya tiene 5 notas')
        else:
            print('El legajo no existe')

    def mostrar_alumnos(self):
        if self.lista_alumnos:
            for i in self.lista_alumnos:
                print(i)
        else:
            print('No hay Alumnos creados')

    def modificar_alumno(self):
        if not self.lista_alumnos:
            print('No hay alumnos creados')
            return
        with open('alumnos.csv', newline='') as archivo_csv:
            lector = csv.reader(archivo_csv)
            datos = list(lector)

        legajo_a_modificar = int(input('Ingrese el legajo del alumno a modificar: '))
        alumno = self._verificar_legajo(legajo_a_modificar)
        if not alumno:
            print('El alumno no existe')
            return
        print('Ingrese los nuevos datos del alumno:')
        nuevo_nombre = input('Nuevo nombre: ')
        nuevo_apellido = input('Nuevo apellido: ')
        opcion = input('Desea modificar las notas? (s/n): ')
        if opcion.lower() == 's':
            nueva_nota = []
            for i in range(5):
                while True:
                    nota = input(f'Ingrese la nueva nota {i + 1}: ').replace(',', '.')
                    try:
                        nota = float(nota)
                        if 0 <= nota <= 10:
                            nueva_nota.append(nota)
                            break
                        else:
                            print('Nota no valida (debe ser entre 0 y 10')
                    except ValueError:
                        print('Entrada no válida. Debe ingresar un número.')
            alumno.nota = nueva_nota

        alumno.nombre = nuevo_nombre if nuevo_nombre else alumno.nombre
        alumno.apellido = nuevo_apellido if nuevo_apellido else alumno.apellido
        self.guardar_alumno_en_csv()

    def mostrar_notas_de_alumno(self):
        if self.lista_alumnos:
            legajo_a_verificar = int(input('Ingresa un numero de legajo: '))
            alumno = self._verificar_legajo(legajo_a_verificar)
            if alumno:
                print(f'Notas de {alumno.nombre} {alumno.apellido}:')
                alumno.mostrar_notas()
            else:
                print('El legajo no existe')
        else:
            print('No hay Alumnos creados')

    def promedio_mayor_descendente(self):
        if self.lista_alumnos:
            promedio_total = self._promedio_general()
            print(f'El promedio total de la clase es: {promedio_total}')
            lista_mayor = []
            for i in self.lista_alumnos:
                if i.promedio() > promedio_total:
                    lista_mayor.append(i)
            main(lista_mayor, 1)

    def promedio_mayor_ascendente(self):
        if self.lista_alumnos:
            promedio_total = self._promedio_general()
            print(f'El promedio total de la clase es: {promedio_total}')
            lista_mayor = []
            for i in self.lista_alumnos:
                if i.promedio() > promedio_total:
                    lista_mayor.append(i)
            main(lista_mayor, 2)


def merge(lista, list_temp, inicio, medio, fin):
    fin_primera_parte = medio - 1
    indice_temp = inicio
    tamano_lista = fin - inicio + 1

    while inicio <= fin_primera_parte and medio <= fin:
        if lista[inicio].promedio() <= lista[medio].promedio():
            list_temp[indice_temp] = lista[inicio]
            inicio += 1
        else:
            list_temp[indice_temp] = lista[medio]
            medio += 1
        indice_temp += 1
    while inicio <= fin_primera_parte:
        list_temp[indice_temp] = lista[inicio]
        inicio += 1
        indice_temp += 1
    while medio <= fin:
        list_temp[indice_temp] = lista[medio]
        medio += 1
        indice_temp += 1
    for i in range(0, tamano_lista):
        lista[fin] = list_temp[fin]
        fin -= 1


def merge_sort(lista, list_temp, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort(lista, list_temp, inicio, medio)
        merge_sort(lista, list_temp, medio + 1, fin)
        merge(lista, list_temp, inicio, medio + 1, fin)


def main(lista, x):
    tamano_lista = len(lista)
    lista_temp = [0] * tamano_lista
    merge_sort(lista, lista_temp, 0, tamano_lista - 1)
    if x == 1:
        print('Lista ordenada de forma descendente: ')
        for nombre in lista:
            print(nombre)
    elif x == 2:
        print('Lista ordenada de forma ascendente: ')
        for nombre in lista[::-1]:
            print(nombre)


def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio].legajo == x:
            return lista[medio]
        elif lista[medio].legajo > x:
            der = medio - 1
        else:
            izq = medio + 1
    return False


class Aplicacion:
    def __init__(self):
        self.menu_principal = Menu("Menu Principal", ['1 -Crear alumno ', '2- Agregar notas a alumno', '3- Modificar Alumno', '4- Ver alumnos',
                                                      '5- Mostrar Notas de alumno',
                                                      '6- Mostrar alumnos que superan promedio general ordenados de forma descendente',
                                                      '7- Mostrar alumnos que superan promedio general ordenados de forma ascendente', '8- Salir'])
        self.gestor_alumno = GestorAlumno()

    def ejecutar(self):
        while True:
            self.menu_principal.mostrar_menu()
            opcion = self.menu_principal.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_alumno.agregar_alumno()
                case 2:
                    legajo = int(input('Ingresa un numero de legajo: '))
                    self.gestor_alumno.agregar_notas(legajo)
                case 3:
                    self.gestor_alumno.modificar_alumno()

                case 4:
                    self.gestor_alumno.mostrar_alumnos()
                case 5:
                    self.gestor_alumno.mostrar_notas_de_alumno()
                case 6:
                    self.gestor_alumno.promedio_mayor_descendente()
                case 7:
                    self.gestor_alumno.promedio_mayor_ascendente()
                case 8:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no válida. Debe ser un número entre 1 y 6.")


Aplicacion = Aplicacion()
Aplicacion.ejecutar()
