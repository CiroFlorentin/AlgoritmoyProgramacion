from datetime import datetime

class Menu:
    def __init__(self, opciones: list[str], nombre: str ):
        if not isinstance(opciones, list):
            raise ValueError("El parametro opciones debe ser una lista de opciones")
        self.opciones_menu = opciones
        self.nombre = nombre

    def mostrar_menu(self) -> None:
        """Muestra las opciones del menú en la consola."""
        print(f"\n----{self.nombre}----")
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

class Fecha:
    def __init__(self, fecha_str: str, horario_str: str = None):
        self.dt_objeto = None
        formato_fecha = "%d/%m/%Y"
        formato_fecha_hora = "%d/%m/%Y %H:%M"
        if horario_str:
            fecha_hora = f"{fecha_str} {horario_str}"
            try:
                fecha_dt = datetime.strptime(fecha_hora, formato_fecha_hora)
            except ValueError:
                raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")

            if fecha_dt < datetime.now():
                raise ValueError("La fecha no puede ser anterior a la fecha actual.")
        else:
            try:
                fecha_dt = datetime.strptime(fecha_str, formato_fecha)
            except ValueError:
                raise ValueError("Formato de fecha no válido. Debe ser dd/mm/aaaa")

        self.dt_objeto = fecha_dt
        self.dia = self.dt_objeto.day
        self.mes = self.dt_objeto.month
        self.anio = self.dt_objeto.year
        self.hora = self.dt_objeto.hour if horario_str else None
        self.minuto = self.dt_objeto.minute if horario_str else None

    def __str__(self):
        if self.hora is not None and self.minuto is not None:
            return self.dt_objeto.strftime("%d/%m/%Y %H:%M")
        else:
            return self.dt_objeto.strftime("%d/%m/%Y")

class merge_sort:
    """Clase para ordenar una lista de Turnos por fecha y hora usando el algoritmo Merge Sort."""

    def merge(self, lista: list, list_temp, inicio, medio, fin):
        fin_primera_parte = medio - 1
        indice_temp = inicio
        tamano_lista = fin - inicio + 1

        while inicio <= fin_primera_parte and medio <= fin:
            if lista[inicio].fecha.dt_objeto <= lista[medio].fecha.dt_objeto:
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

    def merge_sort(self,lista, list_temp, inicio, fin):
        if inicio < fin:
            medio = (inicio + fin) // 2
            self.merge_sort(lista, list_temp, inicio, medio)
            self.merge_sort(lista, list_temp, medio + 1, fin)
            self.merge(lista, list_temp, inicio, medio + 1, fin)

    def main(self,lista):
        tamano_lista = len(lista)
        lista_temp = [0] * tamano_lista
        self.merge_sort(lista, lista_temp, 0, tamano_lista - 1)
        return lista
