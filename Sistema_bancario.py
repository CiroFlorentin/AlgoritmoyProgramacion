# CONSTANTES
CEPO = True
LIMITE_CEPO = 200


class GestionDeClientes:
    def __init__(self):
        # Lista de clientes: [[nombre, apellido, dni], [(monto, fecha)]]
        self.Clientes = []

    def agregar_transaccion(self, dni, monto=None, fecha_str=None):
        # Verificacar existencia del cliente
        cliente_existe = None
        for cliente in self.Clientes:  # [['nombre:Ciro' , 'apellido: florentin', 'DNI: 45072536'], [(monto, fecha)]]
            datos_personales = cliente[0]
            if datos_personales[2] == f"DNI: {dni}":
                cliente_existe = cliente
                break

        # Si existe procesar transaccion directamente
        if cliente_existe:
            fecha = FechaTransaccion(fecha_str)
            self.agregar_transaccion_cliente_existente(cliente_existe, monto, fecha)
        else:
            self.agregar_transaccion_cliente_no_existente(dni)

    def agregar_transaccion_cliente_existente(self, cliente_existe, monto, fecha):
        # [['nombre:Ciro' , 'apellido: florentin', 'DNI: 45072536'], [(monto, fecha)]]
        nombre, apellido, dni = cliente_existe[0]
        transacciones = cliente_existe[1]

        # Verificar si el cliente ya tiene transacciones
        total_mes = 0
        for t in transacciones:
            if t[1].mes == fecha.mes and t[1].anio == fecha.anio:
                total_mes += t[0]
        if CEPO and total_mes + monto > LIMITE_CEPO:
            print(f"⚠️ El monto mensual excede el límite de {LIMITE_CEPO} USD para este cliente.")
            return

        # Agregar transacción al cliente existente
        transacciones.append((monto, fecha))
        print(f"✅ Transacción agregada para cliente existente: {nombre} {apellido}, Monto: {monto} USD, Fecha: {fecha}")

    def agregar_transaccion_cliente_no_existente(self, dni):
        print('Generando Nuevo Cliente ...')
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        monto = float(input("Ingrese el monto en USD a comprar: "))

        # Verificar que no se pase del límite mensual
        if CEPO and monto > LIMITE_CEPO:
            print(f"⚠️ El monto excede el límite mensual de {LIMITE_CEPO} USD.")
            return

        fecha_str = input("Ingrese la fecha de la transacción (DD/MM/AAAA): ")
        fecha = FechaTransaccion(fecha_str)

        # Crear nuevo cliente y agregar transacción
        nuevo_cliente = [
            [f"Nombre: {nombre}", f"Apellido: {apellido}", f"DNI: {dni}"],
            [(monto, fecha)]
        ]
        self.Clientes.append(nuevo_cliente)
        print(f"\n✅ Nuevo cliente registrado y transacción agregada: {nombre} {apellido}, Monto: {monto} USD, Fecha: {fecha}")

    def ver_historial_transacciones(self):
        if not self.Clientes:
            print("\nNo hay transacciones registradas.")
            return

        for i, cliente in enumerate(self.Clientes, 1):
            datos, transacciones = cliente
            print(f"\nCliente #{i}:")
            for campo in datos:
                print(f"  {campo}")
            print("  Transacciones:")
            for monto, fecha in transacciones:
                print(f"    Monto: {monto} USD, Fecha: {fecha}")


class FechaTransaccion:
    def __init__(self, fecha_str: str):
        fecha_split = fecha_str.split("/")
        if len(fecha_split) == 3:
            self.dia = int(fecha_split[0])
            self.mes = int(fecha_split[1])
            self.anio = int(fecha_split[2])
        else:
            raise ValueError(f"Error al crear al fecha, datos invalidos: {fecha_split}")

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


# Menu principal
GESTION = GestionDeClientes()
while True:
    print("Sistema Bancario USD")
    print("1. Procesar compra de divisas")
    print("2. Ver historial de transacciones")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("Procesando compra de divisas...")
            dni = input("Ingrese su DNI: ")

            cliente_existe = None
            for cliente in GESTION.Clientes:
                if cliente[0][2] == f"DNI: {dni}":
                    cliente_existe = cliente
                    break

            # Si el cliente no existe, registrar datos personales
            if not cliente_existe:
                GESTION.agregar_transaccion(dni)

            # Si el cliente ya existe, solo procesar la transacción
            else:
                print("Cliente existente")
                monto = float(input("Ingrese el monto en USD a comprar: "))
                fecha = input("Ingrese la fecha de la transacción (DD/MM/AAAA): ")
                GESTION.agregar_transaccion(dni, monto, fecha)
        case "2":
            GESTION.ver_historial_transacciones()
        case "3":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")
            continue
