""" Un banco tiene 50 cuentas. Se pide hacer un programa que realice las siguientes opciones:

ALTA: Permitir ingresa los siguientes datos de cada cuenta (Numero de cuenta--- entero. Tipo de cuenta --- carácter (C: cuenta corriente, A: caja de ahorro). Saldo de la cuenta --- flotante.
MODICACION: Permite cambiar el saldo de una cuenta (se busca por número de cuenta).
CONSULTA muestra los datos de todas las cuentas.
CONSULTA POR NUMERO DE CUENTA muestra los datos de una cuenta cualquiera (se busca por número de cuenta).
SALIR DEL PROGRAMA"""

"""CC-1 Se pide modificar el software  CRUD de cuentas bancarias para que permita la gestión de Clientes con los siguientes datos (CUIL, nombre, apellido, fecha de nacimiento, cuentas bancarias). Cada cliente del banco puede tener múltiples cuentas.

CC-2 Se pide agregar el tipo de cuenta "cuenta sueldo"

CC-3 Se pide que cada cuenta sea en una moneda específica dentro de las cuales pueden estar: ARS (pesos argentinos), USD (dólares americanos), BRL(real brasileño)
"""
import re
from datetime import datetime


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    'Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


class MenuPrincipal:
    def __init__(self):
        self.menu_principal = ['1- Entrar al sistema de clientes', '2- Entrar al sistemas de cuentas bancarias', '3- Salir']

    def mostrar_menu(self) -> None:
        for opcion in self.menu_principal:
            print(opcion)

    def pedir_opcion_de_menu_valida(self) -> int:
        opcion_seleccionada = ''
        while not opcion_seleccionada.isnumeric() or \
                int(opcion_seleccionada) not in range(1, len(self.menu_principal) + 1):
            opcion_seleccionada = input('Seleccione una opción del menú: ')
            if not opcion_seleccionada.isnumeric() or \
                    int(opcion_seleccionada) not in range(1, len(self.menu_principal) + 1):
                print(
                    f'Opción no válida. Debe ser un número entre 1 y {len(self.menu_principal)}')
        return int(opcion_seleccionada)


class MenuClientes:
    def __init__(self):
        self.menu_clientes = ['1- Crear Cliente ', '2- Modificacion de cliente ', '3- Mostrar clientes ', '4- Ir para atras']

    def mostrar_menu_clientes(self) -> None:
        for opcion in self.menu_clientes:
            print(opcion)

    def pedir_opcion_de_menu_valida(self) -> int:
        opcion_seleccionada = ''
        while not opcion_seleccionada.isnumeric() or \
                int(opcion_seleccionada) not in range(1, len(self.menu_clientes) + 1):
            opcion_seleccionada = input('Seleccione una opción del menú: ')
            if not opcion_seleccionada.isnumeric() or \
                    int(opcion_seleccionada) not in range(1, len(self.menu_clientes) + 1):
                print(
                    f'Opción no válida. Debe ser un número entre 1 y {len(self.menu_clientes)}')
        return int(opcion_seleccionada)


class MenuCuentaBancaria:
    def __init__(self):
        self.opciones_menu_cuenta_bancaria = ['1- Alta de la cuenta ', '2- Modificacion de la cuenta ', '3- Mostrar cuentas ', '4- Ir para atras']

    def mostrar_menu_cuentas(self) -> None:
        for opcion in self.opciones_menu_cuenta_bancaria:
            print(opcion)

    def pedir_opcion_de_menu_valida(self) -> int:
        opcion_seleccionada = ''
        while not opcion_seleccionada.isnumeric() or \
                int(opcion_seleccionada) not in range(1, len(self.opciones_menu_cuenta_bancaria) + 1):
            opcion_seleccionada = input('Seleccione una opción del menú: ')
            if not opcion_seleccionada.isnumeric() or \
                    int(opcion_seleccionada) not in range(1, len(self.opciones_menu_cuenta_bancaria) + 1):
                print(
                    f'Opción no válida. Debe ser un número entre 1 y {len(self.opciones_menu_cuenta_bancaria)}')
        return int(opcion_seleccionada)


class CuentaBancaria:
    def __init__(self, numero_cuenta: int, tipo_cuenta: str, saldo: float, moneda: str):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.moneda = moneda.upper()
        self.tipo_cuenta = tipo_cuenta.upper()  # C

    def __str__(self):
        tipos = {
            'C': 'Cuenta Corriente',
            'A': 'Caja de Ahorro',
            'S': 'Cuenta Sueldo'
        }
        return f'Numero de cuenta: {self.numero_cuenta}, Tipo de cuenta: {tipos[self.tipo_cuenta]}, Saldo: {self.saldo}, Moneda: {self.moneda}'


class ClienteBanco:
    def __init__(self, cuil: int, nombre: str, apellido: str, fecha_nacimiento: str):
        self.cuil = cuil
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = Fecha(fecha_nacimiento)
        self.cuentas_bancarias = []

    def formate_cuil(self):
        cuil_str = str(self.cuil).zfill(11)  # asegura que tenga 11 dígitos
        return f"{cuil_str[:2]}-{cuil_str[2:10]}-{cuil_str[10]}"

    def agregar_cuenta_bancaria(self, cuenta):  # [numero_cuenta,tipo_De_cuenta,Saldo,moneda]
        for c in self.cuentas_bancarias:
            if c.moneda == cuenta.moneda:
                print(f"Ya existe una cuenta en {cuenta.moneda}.")
                return
        self.cuentas_bancarias.append(cuenta)
        print(f"Cuenta en {cuenta.moneda} agregada correctamente.")

    def __str__(self):
        cuentas_bancarias_info = '\n'.join(str(cuenta) for cuenta in self.cuentas_bancarias)
        return f'CUIL: {self.formate_cuil()}, Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de Nacimiento: {self.fecha_nacimiento}\nCuentas Bancarias:\n{cuentas_bancarias_info if cuentas_bancarias_info else "No hay cuentas bancarias registradas."}'


class GestorClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        if cliente.cuil in self.clientes:
            print('El cliente ya existe.')
        else:
            self.clientes[cliente.cuil] = cliente
            print('Cliente agregado con éxito.')

    def ver_clientes(self):
        for cliente in self.clientes.values():
            print(cliente)

    def modificar_cliente(self, cuil, nombre=None, apellido=None, fecha_nacimiento=None):
        try:
            cliente = self.clientes[cuil]
            if nombre: cliente.nombre = nombre
            if apellido: cliente.apellido = apellido
            if fecha_nacimiento: cliente.fecha_nacimiento = Fecha(fecha_nacimiento)
            print('Cliente modificado con éxito.')
        except KeyError:
            print('Cliente no encontrado.')

    def obtener_cliente(self, cuil):
        if cuil in self.clientes:
            return self.clientes[cuil]
        else:
            print('Cliente no encontrado.')
            return None

    def eliminar_cliente(self, cuil):
        if cuil in self.clientes:
            del self.clientes[cuil]
            print('Cliente eliminado con éxito.')
        else:
            print('Cliente no encontrado.')


class GestionCuentasBancarias:
    def __init__(self, cliente):
        self.cliente = cliente

    def crear_cuenta(self, numero_cuenta: int, tipo_cuenta: str, saldo: float, moneda: str):
        for c in self.cliente.cuentas_bancarias:
            if c.numero_cuenta == numero_cuenta:
                print('El número de cuenta ya existe.')
                return
        cuenta = CuentaBancaria(numero_cuenta, tipo_cuenta, saldo, moneda)
        self.cliente.agregar_cuenta_bancaria(cuenta)

    def ver_cuentas(self):
        if not self.cliente.cuentas_bancarias:
            print('No hay cuentas bancarias registradas.')
            return
        for cuenta in self.cliente.cuentas_bancarias:
            print(f" {cuenta}")

    def modificar_cuenta_bancaria(self, numero_cuenta, saldo=None, tipo_cuenta=None):
        for cuenta in self.cliente.cuentas_bancarias:
            if cuenta.numero_cuenta == numero_cuenta:
                if saldo is not None:
                    cuenta.saldo = saldo
                if tipo_cuenta is not None:
                    cuenta.tipo_cuenta = tipo_cuenta
                print('Saldo modificado con éxito.')
                return
        print('Número de cuenta no encontrado.')

    def eliminar_cuenta(self, numero_cuenta):
        for cuenta in self.cliente.cuentas_bancarias:
            if cuenta.numero_cuenta == numero_cuenta:
                self.cliente.cuentas_bancarias.remove(cuenta)
                print('Cuenta eliminada con éxito.')
                return
        print('Número de cuenta no encontrado.')


def main():
    menu_principal = MenuPrincipal()
    menu_clientes = MenuClientes()
    menu_cuenta_bancaria = MenuCuentaBancaria()
    gestor = GestorClientes()

    while True:
        menu_principal.mostrar_menu()
        opcion_seleccionada = menu_principal.pedir_opcion_de_menu_valida()
        bandera = True
        match opcion_seleccionada:
            # menu CLIENTES
            case 1:
                while bandera:
                    print('Entrando al sistema de Clientes')
                    menu_clientes.mostrar_menu_clientes()
                    opcion_seleccionada_clientes = menu_clientes.pedir_opcion_de_menu_valida()
                    match opcion_seleccionada_clientes:
                        case 1:
                            print('Creando cliente')
                            cuil = int(input('Ingrese el CUIL del cliente: '))
                            nombre = input('Ingrese el nombre del cliente: ')
                            apellido = input('Ingrese el apellido del cliente: ')
                            fecha_nacimiento = input('Ingrese la fecha de nacimiento del cliente (dd/mm/aaaa): ')
                            cliente = ClienteBanco(cuil, nombre, apellido, fecha_nacimiento)
                            gestor.agregar_cliente(cliente)
                        case 2:
                            print('Modificando cliente')
                            cuil = int(input('Ingrese el CUIL del cliente a modificar: '))
                            if cuil not in gestor.clientes:
                                print('El cliente no existe.')
                                continue
                            nombre = input('Ingrese el nuevo nombre del cliente: ')
                            apellido = input('Ingrese el nuevo apellido del cliente: ')
                            fecha_nacimiento = input('Ingrese la nueva fecha de nacimiento del cliente (dd/mm/aaaa): ')
                            gestor.modificar_cliente(cuil, nombre, apellido, fecha_nacimiento)
                        case 3:
                            print('Mostrando clientes')
                            gestor.ver_clientes()
                        case 4:
                            print('Ir para atras')
                            bandera = False
                        case _:
                            print('Opción no válida. Por favor, seleccione una opción válida.')
            # Menu BANCARIO
            case 2:
                while bandera:
                    print('Entrando al sistema de Cuentas Bancarias')
                    menu_cuenta_bancaria.mostrar_menu_cuentas()
                    opcion_seleccionada_cuentas = menu_cuenta_bancaria.pedir_opcion_de_menu_valida()
                    if opcion_seleccionada_cuentas == 4:
                        print('Ir para atras')
                    else:
                        cuil = int(input('Ingrese el CUIL del cliente: '))
                        if cuil not in gestor.clientes:
                            print('El cliente no existe.')
                            continue
                        gestor_cuenta = GestionCuentasBancarias(gestor.obtener_cliente(cuil))

                    match opcion_seleccionada_cuentas:
                        case 1:
                            print('Alta de la cuenta')
                            numero_cuenta = int(input('Ingrese el número de cuenta: '))

                            tipo_cuenta = input('Ingrese el tipo de cuenta (C: Cuenta Corriente, A: Caja de Ahorro, S: Cuenta Sueldo): ')
                            saldo = input('Ingrese el saldo de la cuenta: ').replace(',', '.')
                            saldo = float(saldo)
                            moneda = input('Ingrese la moneda de la cuenta (ARS, USD, BRL): ')
                            gestor_cuenta.crear_cuenta(numero_cuenta, tipo_cuenta, saldo, moneda)
                        case 2:
                            print('Modificacion de la cuenta')
                            numero_cuenta = int(input('Ingrese el número de cuenta a modificar: '))
                            saldo = input('Ingrese el nuevo saldo de la cuenta: ').replace(',', '.')
                            saldo = float(saldo)
                            tipo_cuenta = input('Ingrese el nuevo tipo de cuenta (C: Cuenta Corriente, A: Caja de Ahorro, S: Cuenta Sueldo): ')
                            gestor_cuenta.modificar_cuenta_bancaria(numero_cuenta, saldo, tipo_cuenta)
                        case 3:
                            print('Mostrando cuentas')
                            gestor_cuenta.ver_cuentas()
                        case 4:
                            bandera = False
                        case _:
                            print('Opción no válida. Por favor, seleccione una opción válida.')
            case 3:
                print('Saliendo del programa')
                input()
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')


main()
