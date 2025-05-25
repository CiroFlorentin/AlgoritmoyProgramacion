"""
Desarrollar una aplicación de consola en Python que permita realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre productos de supermercado. Utilizar la clase Product como modelo de entidad y el archivo binario productos.bin como base de datos

📄 Listar todos los productos- Mostrar cada producto en una línea, con su código, nombre y precio.Permitir ordenar por precio o nombre (ascendente o descendente) OPCIONAL DESEABLE
🔍 Buscar un producto por código- Ingresar un código y mostrar los detalles si existe.
➕ Agregar un nuevo producto- Solicitar al usuario: código, nombre y precio.Verificar que el código no esté duplicado.Guardar el nuevo producto en el archivo productos.bin.
✏️ Modificar un producto existente- Buscar el producto por código. Permitir modificar su nombre y/o precio. Guardar los cambios en el archivo.
🗑️ Eliminar un producto-Ingresar el código del producto a eliminar. Confirmar la acción antes de eliminar.
💾 Guardar cambios- Todos los cambios deben persistirse en el archivo productos.bin usando pickle.
🚪 Salir- Terminar el programa de forma segura.

"""

import pickle as pk


class Menu:
    def __init__(self, opciones: [str]):
        if not isinstance(opciones, list):
            raise ValueError("El parametro opciones debe ser una lista de opciones")
        self.opciones_menu = opciones

    def mostrar_menu(self) -> None:
        """Muestra las opciones del menú en la consola."""
        print("\n--- SUPERMERCADO ---")
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


class GestorProductos:
    def __init__(self):
        self.file = "productos.bin"
        with open(self.file, 'rb') as bfile:
            self.productos: list[Product] = pk.load(bfile)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

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
                print('Poducto no encontrado')

    def guardar(self):
        with open(self.file, 'wb') as bfile:
            pk.dump(self.productos, bfile)

    def _validar_precio(self):
        while True:
            precio = input('Ingrese un precio: ').replace(',', '.')
            if precio.isnumeric() or float(precio):
                return float(precio)
            else:
                print('Ingrese un precio valido')

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
class Aplicacion:
    def __init__(self):
        self.menu = Menu(['1- Listar productos', '2- Buscar por codigo', '3- Agregar producto', '4- Modificar producto',
                          '5- Eliminar Producto', '6- Guardar Archivos', '7- Salir'])
        self.gestor_productos = GestorProductos()

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            opcion = self.menu.pedir_opcion_de_menu_valida()
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


app = Aplicacion()
app.ejecutar()
