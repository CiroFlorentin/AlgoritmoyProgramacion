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
                raise ValueError('Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


LIMITE_CEPO = 200
CEPO = True


##nombre,dni,tipoDeCaja,fecha

class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}"


class GestorBancario:
    def __init__(self):
        self.cliente_bancario = []  # [[NOMBRE, APELLIDO, DNI],[Monto,Fecha]]

    def transacciones(self):
        dni = input("Ingrese su DNI: ")
        cliente_existe = None
        for cliente in self.cliente_bancario:  # [[cliente],[monto,fecha]]
            ## cliente[0] = [Nombre,Apellido,DNI]
            datos_personales: Cliente = cliente[0]
            if datos_personales.dni == dni:
                cliente_existe = cliente
                break
        if cliente_existe:
            self._agregar_transaccion_si_cliente_existe(cliente_existe)
        else:
            self._agregar_transaccion_si_cliente_no_existe(dni)

    def _agregar_transaccion_si_cliente_existe(self, cliente_existe):  ##[[Nombre,Apellido,DNI],[Monto,Fecha]]
        cliente_obj: Cliente = cliente_existe[0]  ##[Nombre,Apellido,DNI]
        transaccion = cliente_existe[1]  ##[Monto,Fecha]
        monto = int(input("Ingrese el monto de la compra: "))
        fecha = input("Ingrese la fecha de compra (dd/mm/aaaa): ")
        fecha = Fecha(fecha)
        compras_totales = 0
        for t in transaccion:
            if t[1].mes == fecha.mes and t[1].anio == fecha.anio:
                compras_totales += t[0]
        if compras_totales + monto > LIMITE_CEPO and CEPO:
            print(f"⚠️ El monto mensual excede el límite de {LIMITE_CEPO} USD para este cliente.")
            return
        transaccion.append((monto, fecha))
        print(f"✅ Transacción agregada para cliente existente: {cliente_obj.nombre} {cliente_obj.apellido}, Monto: {monto} USD, Fecha: {fecha}")

    def _agregar_transaccion_si_cliente_no_existe(self, dni):
        ## PASA SI EL CLIENTE NO EXISTE
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cliente = Cliente(nombre, apellido, dni)
        monto = float(input("Ingrese el monto a comprar en USD: "))
        fecha_str = input("Ingrese la fecha de compra (dd/mm/aaaa): ")
        fecha = Fecha(fecha_str)
        nuevo_cliente = [
            cliente,
            [(monto, fecha)]
        ]
        self.cliente_bancario.append(nuevo_cliente)

    def mostrar_transacciones(self):
        if not self.cliente_bancario:
            print("No hay transacciones registradas.")
            return
        print("Historial de transacciones:")
        for i, cliente in enumerate(self.cliente_bancario, 1):
            print(f'cliente{i}')
            datos_cliente: Cliente = cliente[0]
            transacciones = cliente[1]
            print(f"Cliente: {datos_cliente.nombre} {datos_cliente.apellido}, DNI: {datos_cliente.dni}")
            print("Transacciones:")
            for monto, fecha in transacciones:
                print(f"  Monto: {monto} USD, Fecha: {fecha}")


def menu():
    gestor = GestorBancario()
    while True:
        print("1 - Procesar compra de divisas")
        print("2 - Mostrar transacciones")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                gestor.transacciones()
            case "2":
                gestor.mostrar_transacciones()
            case "3":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                continue


menu()
