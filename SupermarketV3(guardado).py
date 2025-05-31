#----------IMPORTS---------------------------------------------------
import pickle as pk
from datetime import datetime
import re
#--------------------------------------------------------------------

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
        self.mostrar_hora = False
        if not fecha_str:
            ahora = datetime.now()
            self.dia = ahora.day
            self.mes = ahora.month
            self.anio = ahora.year
            self.hora = ahora.hour
            self.minuto = ahora.minute
            self.segundo = ahora.second
            self.mostrar_hora = True
        else:
            if not self.es_fecha_valida(fecha_str):
                raise ValueError('Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = fecha_str.split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])


    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        if self.mostrar_hora:
            return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        else:
            return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"
# -------------------------------CLASES BASE-----------------------------------------------------

class Cliente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: Fecha):
        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("El DNI debe ser numérico y tener al menos 7 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Cliente: {self.nombre} - DNI: {self.dni} - Nacimiento: {self.fecha_nacimiento}"

class Product:
    def __init__(self, cod: int, name: str, price: float, stock):
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.codigo: int = cod
        self.nombre: str = name
        self.precio: float = price
        self.stock:int = stock

    def __str__(self):
        return f"Producto ({self.codigo}): {self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"

    def aplicar_descuento(self, porcentaje: float) -> float:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        if not (1 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 1 y 100.")

        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)
class Compra:
    def __init__(self,cliente:Cliente,producto:Product,cantidad:int,total,fecha = None):
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente debe ser una instancia de la clase Cliente.")
        if not isinstance(producto, Product):
            raise TypeError("El producto debe ser una instancia de la clase Product.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
        if not isinstance(total, (int, float)) or total < 0:
            raise ValueError("El total debe ser un número positivo.")
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha

# -------------------------------GESTORES-----------------------------------------------------
class GestorProductos:
    def __init__(self):
        self.file = "Datos/productos_con_stock.bin"
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
            if not precio:
               return None
            try:
                return float(precio)
            except ValueError:
                print('reingrese un precio valido')

    def validar_codigo(self, cod_str: str = None) -> int | None:
        while True:
            if cod_str is None:
                cod_str = input('Ingrese un código: ')
            if not cod_str:
                return None
            if cod_str.isnumeric():
                return int(cod_str)
            else:
                print('Reingrese un código válido (solo números).')
                cod_str = None

    def _buscar_codigo(self, cod: str = None) -> Product | False:
        codigo_validado = self.validar_codigo(cod)
        if codigo_validado is None:
            return False
        for producto in self.productos:
            if producto.codigo == codigo_validado:
                return producto
        return False

    def _validar_stock(self):
        while True:
            try:
                stock = int(input('Ingrese el stock del producto: '))
                if stock >= 0:
                    return stock
                else:
                    print('El stock no puede ser negativo.')
            except ValueError:
                print('Ingrese un valor numérico válido para el stock.')

    def listar_productos(self):
        print('-Productos-')
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
            stock = self._validar_stock()
            nuevo_producto = Product(int(cod), nombre, precio,stock)
            self.productos.append(nuevo_producto)
            self.guardar()

    def modificar(self):
        codigo = input('Ingrese el codigo del producto a modificar: ')
        producto = self._buscar_codigo(codigo)
        if producto:
            nombre = input('Ingrese el nombre nuevo: ')
            precio = self._validar_precio()
            stock = self._validar_stock()
            if nombre: producto.nombre = nombre
            if precio: producto.precio = precio
            if stock: producto.stock = stock
            self.guardar()
        else:
            print('Producto no encontrado.')

    def agregar_stock(self):
        codigo = input('Ingrese el codigo del producto a agregar stock: ')
        producto = self._buscar_codigo(codigo)
        if producto:
            stock = self._validar_stock()
            if stock is not None:
                producto.stock += stock
                self.guardar()
                print(f'Stock actualizado. Nuevo stock: {producto.stock}')


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


    def _validar_fecha(self):
        while True:
            fecha_nacimiento_str = input('Ingrese la fecha de nacimiento (dd/mm/aaaa): ')
            try:
                fecha_nacimiento = Fecha(fecha_nacimiento_str)
                return fecha_nacimiento
            except ValueError as e:
                print(e)


    def _validar_nombre(self, nombre):
        if not re.match(r'^[a-zA-Z\s]+$', nombre):
            print('El nombre solo puede contener letras y espacios.')
            return False
        return True

    def encontrar_cliente_por_dni(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def pedir_dni(self):
        while True:
            dni = input('Ingrese el DNI del cliente: ')
            dni_validado = self._validar_dni(dni)
            if dni_validado:
                return dni_validado

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente_por_dni(self):
        dni = self.pedir_dni()
        cliente = self.encontrar_cliente_por_dni(dni)
        if cliente:
            print('-Cliente-')
            print(cliente)
            print('-' * 70)
        else:
            print('Cliente no encontrado.')

    def agregar_cliente(self,dni = None):
        if dni is None:
            dni = self.pedir_dni()
        if self.encontrar_cliente_por_dni(dni):
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
        dni = self.pedir_dni()
        cliente = self.encontrar_cliente_por_dni(dni)
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
        dni = self.pedir_dni()
        cliente = self.encontrar_cliente_por_dni(dni)
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

class GestorCompras:
    def __init__(self,gestor_productos: GestorProductos , gestor_clientes: GestorClientes):
        self.file = "Datos/compras.bin"
        self.gestor_productos = gestor_productos
        self.gestor_clientes = gestor_clientes
        try:
            with open(self.file, 'rb') as bfile:
                self.compras: list[Compra] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.compras: list[Compra] = []
            with open(self.file, 'wb') as bfile:
                pk.dump(self.compras, bfile)

    def guardar_cambios(self):
        with open(self.file, 'wb') as bfile:
            pk.dump(self.compras, bfile)

    def comprar(self):
        dni = self.gestor_clientes.pedir_dni()
        cliente = self._encontrar_cliente(self.gestor_clientes,dni)
        if not cliente:
            opcion = input('Cliente no encontrado. ¿Desea agregar un nuevo cliente? (s/n): ')
            if opcion.lower() == 's':
                print('Procediendo a agregar el cliente.')
                cliente = self._crear_cliente(self.gestor_clientes,dni)
            else:
                print('Compra cancelada.')
                return
        producto = self._obtener_producto_valido(self.gestor_productos)
        if not producto:
            print('No se pudo obtener un producto válido. Compra cancelada.')
            return
        cantidad = self._obtener_cantidad_valida(producto.stock)
        if cantidad is None:
            print('Cantidad no válida. Compra cancelada.')
            return
        producto.stock -= cantidad
        total = round(producto.precio * cantidad,2)
        fecha = Fecha()
        compra = Compra(cliente, producto, cantidad, total,fecha)
        self.compras.append(compra)
        self.gestor_productos.guardar()
        self.guardar_cambios()
        print(f"Compra realizada con éxito:\nCliente: {cliente.nombre}\nProducto: {producto.nombre}\nCantidad: {cantidad}\nTotal a pagar: ${total:.2f}")

    def ver_compras_por_dni(self,dni = None):
        if dni is None:
            dni = self.gestor_clientes.pedir_dni()
        cliente = self._encontrar_cliente(self.gestor_clientes,dni)
        if not cliente:
            print('Cliente no encontrado.')
            return
        print(f"Compras realizadas por {cliente.nombre} (DNI: {cliente.dni}):")
        compras_cliente = []
        for compra in self.compras:
            if compra.cliente.dni == cliente.dni:
                compras_cliente.append(compra)
        if not compras_cliente:
            print('No se encontraron compras para este cliente.')
            return
        for compra in compras_cliente:
            print(f"Fecha: {compra.fecha}, Producto: {compra.producto.nombre}, Cantidad: {compra.cantidad}, Total: ${compra.total:.2f}")

    def listar_compras(self):
        if not self.compras:
            print('No hay compras registradas.')
            return
        print('-Compras-')
        for compra in self.compras:
            print(f"Fecha: {compra.fecha}, Cliente: {compra.cliente.nombre} (DNI: {compra.cliente.dni}), Producto: {compra.producto.nombre}, Cantidad: {compra.cantidad}, Total: ${compra.total:.2f}")

    def eliminar_compra(self):
        if not self.compras:
            print('No hay compras registradas.')
            return
        cliente = self._compras_por_dni()
        self.ver_compras_por_dni(cliente.dni)
        compras_cliente =[]
        for compra in self.compras:
            if compra.cliente.dni == cliente.dni:
                compras_cliente.append(compra)
        if not compras_cliente:
            print('No se encontraron compras para este cliente.')
            return
        while True:
            try:
                indice = int(input(f'Ingrese el número de la compra a eliminar (1-{len(compras_cliente)}): ')) - 1
                if 0 <= indice < len(compras_cliente):
                    break
                else:
                    print(f'Número inválido. Debe estar entre 1 y {len(compras_cliente)}.')
            except ValueError:
                print('Entrada no válida. Debe ser un número entero.')

        compra_eliminar = compras_cliente[indice]
        confirmacion = input(f"¿Está seguro de eliminar la compra realizada por {compra_eliminar.cliente.nombre} (DNI: {compra_eliminar.cliente.dni})? (s/n): ")

        if confirmacion.lower() == 's':
            producto = self.gestor_productos._buscar_codigo(compra_eliminar.producto.codigo)
            if producto:
                producto.stock += compra_eliminar.cantidad
            else:
                print("Advertencia: No se encontró el producto para devolver el stock.")

            self.compras.remove(compra_eliminar)
            self.gestor_productos.guardar()
            self.guardar_cambios()
            print('Compra eliminada correctamente.')
        else:
            print('Eliminación cancelada.')

    def _compras_por_dni(self):
        while True:
            dni = self.gestor_clientes.pedir_dni()
            cliente = self._encontrar_cliente(self.gestor_clientes, dni)
            if not dni:
                return None
            if cliente:
                print()
                return cliente
            print('Cliente no encontrado. Reintente.')


    def _encontrar_cliente(self, gestor_clientes,dni):
        cliente = gestor_clientes.encontrar_cliente_por_dni(dni)
        if cliente:
            return cliente
        return None

    def _crear_cliente(self, gestor_clientes, dni):
        gestor_clientes.agregar_cliente(dni)
        return gestor_clientes.encontrar_cliente_por_dni(dni)

    def _obtener_producto_valido(self, gestor_productos):
        while True:
            codigo = input('Ingrese el código del producto a comprar: ')
            producto = gestor_productos._buscar_codigo(codigo)
            if not producto:
                print('Producto no encontrado. Reintente.')
                continue
            if producto.stock <= 0:
                print('Producto sin stock.')
                return None


            return producto
    def _obtener_cantidad_valida(self, stock):
        while True:
            cantidad = input('Ingrese la cantidad a comprar: ')
            if not cantidad.isdigit() or int(cantidad) <= 0:
                print('Cantidad no válida. Debe ser un número entero positivo.')
                continue
            cantidad = int(cantidad)
            if cantidad > stock:
                print(f'Stock insuficiente. Solo hay {stock} unidades disponibles.')
                continue
            return cantidad

# -------------------------------APPLICACION-----------------------------------------------------
class Aplicacion:
    def __init__(self):
        self.menu_super= self.menu_supermercado()
        self.menu_clien = self.menu_clientes()
        self.menu_compra = self.menu_compra()
        self.menu_principal = Menu(['1- Gestion de Clientes', '2- Gestion de Supermercado','3- Menu Compras','4- Salir'], "Menu Principal")
        self.gestor_productos = GestorProductos()
        self.gestor_clientes = GestorClientes()
        self.gestor_compras = GestorCompras(self.gestor_productos, self.gestor_clientes)


    def menu_clientes(self):
        opciones = ['1- Listar clientes', '2- Buscar cliente por DNI', '3- Agregar cliente',
                    '4- Modificar cliente', '5- Eliminar cliente', '6- Guardar cambios', '7- Volver al menú principal']
        return Menu(opciones, "Clientes")

    def menu_supermercado(self):
        opciones = ['1- Listar productos', '2- Buscar por codigo', '3- Agregar producto',
                    '4- Modificar producto','5- Agregar stock', '6- Eliminar Producto', '7- Guardar Archivos', '8- Volver al menú principal']
        return Menu(opciones, "Supermercado")

    def menu_compra(self):
        opciones = ['1- Comprar Producto','2- Ver Productos','3- Ver Compras por dni','4- Listar Compras','5- Eliminar Compra','6- Guardar Cambios', '7- Volver al menú principal']
        return Menu(opciones, "Menu Compras")

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
                    self.gestor_productos.agregar_stock()
                case 6:
                    self.gestor_productos.eliminar()
                case 7:
                    self.gestor_productos.guardar()
                    print('Cambios guardados correctamente.')
                case 8:
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
                    print('Cambios guardados correctamente.')
                case 7:
                    print('Volviendo al menú principal...')
                    break
                case _:
                    print('Opción no válida. Reintente.')

    def menu_compras_ej(self):
        while True:
            self.menu_compra.mostrar_menu()
            opcion = self.menu_compra.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    print('Comprando Producto')
                    self.gestor_compras.comprar()
                case 2:
                    print('Ver Productos')
                    self.gestor_productos.listar_productos()
                case 3:
                    self.gestor_compras.ver_compras_por_dni()
                case 4:
                    self.gestor_compras.listar_compras()
                case 5:
                    self.gestor_compras.eliminar_compra()
                case 6:
                    self.gestor_compras.guardar_cambios()
                    print('Cambios guardados correctamente.')
                case 7:
                    print('Volver al menú principal')
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
                    self.menu_compras_ej()
                case 4:
                    print('Saliendo de la aplicación...')
                    return
                case _:
                    print('Opción no válida. Reintente.')

app = Aplicacion()
app.ejecutar()
