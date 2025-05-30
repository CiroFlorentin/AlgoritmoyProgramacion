"""
📌 Añadir al menú principal una sección "Gestión de Clientes", con las siguientes operaciones:
📄 Listar clientes: Mostrar nombre, DNI y fecha de nacimiento.
🔍 Buscar cliente por DNI: Mostrar información si existe.
➕ Agregar cliente: Ingresar nombre, DNI y fecha de nacimiento (dd/mm/aaaa). Validar formato y que no exista duplicado por DNI. Almacenar en clientes.bin.
✏️ Modificar cliente existente: Permitir cambiar nombre o fecha de nacimiento.
🗑️ Eliminar cliente: Confirmar antes de eliminar.
💾 Guardar cambios: Usar pickle para guardar clientes.bin.
⬅️ Volver al menú principal
"""
import pickle as pk
from datetime import datetime
import re

# -------------------------------DEFAULT-----------------------------------------------------
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
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
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
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"
# -------------------------------CLASES BASE-----------------------------------------------------

class Cliente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: Fecha):
        if not dni.isdigit() or len(dni) < 7:
            raise ValueError("El DNI debe ser numérico y tener al menos 7 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Cliente {self.nombre} - DNI: {self.dni} - Nacimiento: {self.fecha_nacimiento}"

class Product:
    def __init__(self, cod: int, name: str, price: float):
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.codigo: int = cod
        self.nombre: str = name
        self.precio: float = price

    def __str__(self):
        return f"Producto ({self.codigo}): {self.nombre} - Precio: ${self.precio:.2f}"

    def aplicar_descuento(self, porcentaje: float) -> float:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        if not (1 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 1 y 100.")

        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)

# -------------------------------GESTORES-----------------------------------------------------
class GestorProductos:
    def __init__(self):
        self.file = "Datos/productos.bin"
        try:
            with open(self.file, 'rb') as bfile:
                self.productos: list[Product] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.productos: list[Product] = []
            with open(self.file, 'wb') as bfile:
                pk.dump(self.productos, bfile)

    def guardar(self):
        with open(self.file, 'wb') as bfile:
            pk.dump(self.productos, bfile)

    def _validar_precio(self):
        while True:
            precio = input('Ingrese un precio: ').replace(',', '.')
            try:
                return float(precio)
            except ValueError:
                print('reingrese un precio valido')


    def _validar_codigo(self, cod):
        while True:
            if cod.isnumeric():
                return int(cod)
            else:
                print('reingrese un codigo valido')

    def _buscar_codigo(self, codigo):
        cod = self._validar_codigo(codigo)
        for producto in self.productos:
            if producto.codigo == cod:
                return producto
        return False

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def buscar_codigo(self):
        while True:
            cod = input('Ingrese un codigo: ')
            producto = self._buscar_codigo(cod)
            if producto:
                print('-Producto-')
                print(producto)
                print('-' * 70)
                break
            else:
                print('Producto no encontrado')

    def agregar_producto(self):
        cod = input('Ingrese un codigo: ')
        codigo = self._buscar_codigo(cod)
        if not codigo:
            nombre = input('Ingrese el nombre del produto: ')
            precio = self._validar_precio()
            nuevo_producto = Product(int(cod), nombre, precio)
            self.productos.append(nuevo_producto)
            self.guardar()

    def modificar(self):
        codigo = input('Ingrese el codigo del producto a modificar: ')
        producto = self._buscar_codigo(codigo)
        if producto:
            nombre = input('Ingrese el nombre nuevo: ')
            precio = self._validar_precio()
            if nombre: producto.nombre = nombre
            if precio: producto.precio = precio
            self.guardar()
        else:
            print('Producto no encontrado.')

    def eliminar(self):
        codigo = input('Ingrese el codigo del producto a modificar: ')
        producto = self._buscar_codigo(codigo)
        if producto:
            self.productos.remove(producto)
            self.guardar()
        else:
            print('Producto no encontrado.')

class GestorClientes:
    def __init__(self):
        self.file = "Datos/Clientes.bin"
        try:
            with open(self.file, 'rb') as bfile:
                self.clientes: list[Cliente] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.clientes: list[Cliente] = []
            with open(self.file, 'wb') as bfile:
                pk.dump(self.clientes, bfile)

    def guardar_cambios(self):
        with open(self.file, 'wb') as bfile:
            pk.dump(self.clientes, bfile)

    def _validar_dni(self, dni):
        if dni.isdigit() and len(dni) == 8:
            return dni
        else:
            print('Ingrese un DNI válido (numérico y de 8 dígitos).')
            return None

    def _buscar_cliente_por_dni(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def _pedir_dni(self):
        while True:
            dni = input('Ingrese el DNI del cliente: ')
            dni_validado = self._validar_dni(dni)
            if dni_validado:
                return dni_validado

    def _validar_fecha(self):
        while True:
            fecha_nacimiento_str = input('Ingrese la fecha de nacimiento (dd/mm/aaaa): ')
            try:
                fecha_nacimiento = Fecha(fecha_nacimiento_str)
                return fecha_nacimiento
            except ValueError as e:
                print(e)
                continue
    def _validar_nombre(self, nombre):
        if not re.match(r'^[a-zA-Z\s]+$', nombre):
            print('El nombre solo puede contener letras y espacios.')
            return False
        return True

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente_por_dni(self):
        dni = self._pedir_dni()
        cliente = self._buscar_cliente_por_dni(dni)
        if cliente:
            print('-Cliente-')
            print(cliente)
            print('-' * 70)
        else:
            print('Cliente no encontrado.')

    def agregar_cliente(self):
        dni = self._pedir_dni()
        if self._buscar_cliente_por_dni(dni):
            print('El cliente ya existe.')
            return
        while True:
            nombre = input('Ingrese el nombre del cliente: ')
            if not nombre:
                print('El nombre no puede estar vacío.')
                continue
            if self._validar_nombre(nombre):
                break
        fecha = self._validar_fecha()
        nuevo_cliente = Cliente(dni, nombre, fecha)
        self.clientes.append(nuevo_cliente)
        self.guardar_cambios()

    def modificar_cliente(self):
        dni = self._pedir_dni()
        cliente = self._buscar_cliente_por_dni(dni)
        if cliente:
            while True:
                nombre = input('Ingrese el nombre del cliente: ')
                if not nombre:
                    break
                if self._validar_nombre(nombre):
                    cliente.nombre = nombre
                    break
            cambio_fecha= input('¿Desea cambiar la fecha de nacimiento? (s/n): ')
            if cambio_fecha.lower() == 's':
                fecha = self._validar_fecha()
                cliente.fecha_nacimiento = fecha
            print('Cliente modificado correctamente.')
            self.guardar_cambios()
        else:
            print('Cliente no encontrado.')

    def eliminar_cliente(self):
        dni = self._pedir_dni()
        cliente = self._buscar_cliente_por_dni(dni)
        if cliente:
            confirmacion = input(f"¿Está seguro de eliminar al cliente {cliente.nombre} (DNI: {cliente.dni})? (s/n): ")
            if confirmacion.lower() == 's':
                self.clientes.remove(cliente)
                self.guardar_cambios()
                print('Cliente eliminado.')
            else:
                print('Eliminación cancelada.')
        else:
            print('Cliente no encontrado.')


# -------------------------------APPLICACION-----------------------------------------------------
class Aplicacion:
    def __init__(self):
        self.menu_super= self.menu_supermercado()
        self.menu_clien = self.menu_clientes()
        self.menu_principal = Menu(['1- Gestion de Clientes', '2- Gestion de Supermercado', '3- Salir'], "Menu Principal")
        self.gestor_productos = GestorProductos()
        self.gestor_clientes = GestorClientes()

    def menu_clientes(self):
        opciones = ['1- Listar clientes', '2- Buscar cliente por DNI', '3- Agregar cliente',
                    '4- Modificar cliente', '5- Eliminar cliente', '6- Guardar cambios', '7- Volver al menú principal']
        return Menu(opciones, "Clientes")

    def menu_supermercado(self):
        opciones = ['1- Listar productos', '2- Buscar por codigo', '3- Agregar producto',
                    '4- Modificar producto', '5- Eliminar Producto', '6- Guardar Archivos', '7- Salir']
        return Menu(opciones, "Supermercado")

    def menu_supermercado_ej(self):
        while True:
            self.menu_super.mostrar_menu()
            opcion = self.menu_super.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_productos.listar_productos()
                case 2:
                    self.gestor_productos.buscar_codigo()
                case 3:
                    self.gestor_productos.agregar_producto()
                case 4:
                    self.gestor_productos.modificar()
                case 5:
                    self.gestor_productos.eliminar()
                case 6:
                    self.gestor_productos.guardar()
                case 7:
                    print('saliendo...')
                    break
                case _:
                    print('Opcion no valida. Reintente')

    def menu_clientes_ej(self):
        while True:
            self.menu_clien.mostrar_menu()
            opcion = self.menu_clien.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_clientes.listar_clientes()
                case 2:
                    self.gestor_clientes.buscar_cliente_por_dni()
                case 3:
                    self.gestor_clientes.agregar_cliente()
                case 4:
                    self.gestor_clientes.modificar_cliente()
                case 5:
                    self.gestor_clientes.eliminar_cliente()
                case 6:
                    self.gestor_clientes.guardar_cambios()
                case 7:
                    print('Volviendo al menú principal...')
                    break
                case _:
                    print('Opción no válida. Reintente.')

    def ejecutar(self):
        while True:
            self.menu_principal.mostrar_menu()
            opcion = self.menu_principal.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.menu_clientes_ej()
                case 2:
                    self.menu_supermercado_ej()
                case 3:
                    print('Saliendo de la aplicación...')
                    return
                case _:
                    print('Opción no válida. Reintente.')

app = Aplicacion()
app.ejecutar()
