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
    def __init__(self, legajo, nombre, apellido):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.nota = []

    def promedio(self):
        if self.nota:
            suma = 0
            for i in self.nota:
                suma += i
            return suma / len(self.nota)
        else:
            return 0

    def mostrar_notas(self):
        for i in self.nota:
            print(i)

    def __str__(self):
        return f'[{self.legajo}] - {self.nombre} {self.apellido}- Promedio: {self.promedio()} '


class GestorAlumno:
    def __init__(self):
        self.lista_alumnos: list[Alumno] = []

    def _verificar_legajo(self, legajo):
        for i in self.lista_alumnos:
            if i.legajo == legajo:
                return busqueda_binaria(self.lista_alumnos, legajo)
        return False

    def _promedio_general(self):
        notas_suma_total = 0
        if self.lista_alumnos:
            for alumno in self.lista_alumnos:
                notas_suma_total += alumno.promedio()
            promedio_total = notas_suma_total / len(self.lista_alumnos)
            promedio_total = round(promedio_total, 2)
            return promedio_total
        return 0

    def agregar_alumno(self):
        legajo_a_verificar = int(input('Ingresa un numero de legajo: '))
        legajo = self._verificar_legajo(legajo_a_verificar)
        if not legajo:
            nombre = input('Ingrese un nombre: ')
            apellido = input('Ingrese el apellido: ')
            nuevo_alumno = Alumno(legajo_a_verificar, nombre, apellido)
            self.lista_alumnos.append(nuevo_alumno)
        else:
            print('El legajo ya existe')

    def agregar_notas(self):
        if self.lista_alumnos:
            legajo_a_verificar = int(input('Ingresa un numero de legajo: '))
            alumno = self._verificar_legajo(legajo_a_verificar)
            if alumno:
                i = 0
                while True:
                    nota = input(f'Ingrese la nota {i + 1}: ').replace(',', '.')
                    nota = float(nota)
                    if i < 4:
                        if 0 <= nota <= 10:
                            alumno.nota.append(nota)
                            i += 1
                        else:
                            print('Nota no valida')
                    else:
                        break
            else:
                print('El legajo no existe')
        else:
            print('No hay alumnos creados')

    def mostrar_alumnos(self):
        if self.lista_alumnos:
            for i in self.lista_alumnos:
                print(i)
        else:
            print('No hay Alumnos creados')

    def promedio_mayor_descendente(self):
        if self.lista_alumnos:
            promedio_total = self._promedio_general()
            print(f'El promedio total de la clase es: {promedio_total}')
            lista_mayor = []
            if self.lista_alumnos:
                for i in self.lista_alumnos:
                    if i.promedio() > promedio_total:
                        lista_mayor.append(i)
            main(lista_mayor, 1)

    def promedio_mayor_ascendente(self):
        if self.lista_alumnos:
            promedio_total = self._promedio_general()
            print(f'El promedio total de la clase es: {promedio_total}')
            lista_mayor = []
            if self.lista_alumnos:
                for i in self.lista_alumnos:
                    if i.promedio() > promedio_total:
                        lista_mayor.append(i)
            main(self.lista_alumnos, 2)


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
    else:
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
        self.menu_principal = Menu("Menu Principal", ['1 -Crear alumno ', '2- Agregar notas a alumno', '3- Ver alumnos',
                                                      '4- Mostrar alumnos que superan promedio general ordenados de forma descendente',
                                                      '5- Mostrar alumnos que superan promedio general ordenados de forma ascendente', '6- Salir'])
        self.gestor_alumno = GestorAlumno()

    def ejecutar(self):
        while True:
            self.menu_principal.mostrar_menu()
            opcion = self.menu_principal.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_alumno.agregar_alumno()
                case 2:
                    self.gestor_alumno.agregar_notas()
                case 3:
                    self.gestor_alumno.mostrar_alumnos()
                case 4:
                    self.gestor_alumno.promedio_mayor_descendente()
                case 5:
                    self.gestor_alumno.promedio_mayor_ascendente()
                case 6:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no válida. Debe ser un número entre 1 y 6.")


Aplicacion = Aplicacion()
Aplicacion.ejecutar()
