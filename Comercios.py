# Una empresa comercializa 10 artículos en 3 sucursales. Se debe realizar un programa que permita gestionar el inventario y el stock por sucursal para dicha empresa. Para ello se solicita que el programa posea un menú con las siguientes opciones:
#
#     A) Gestión de sucursales. CRUD considerando que toda sucursal tiene un código único (entero), un nombre y una dirección.
#     B) Gestión de artículos. CRUD considerando que todo artículo tiene un código único (entero), un nombre, una categoría y una descripción.
#     C) Carga de stock: se registrará el ingreso en depósito de la cantidad de un determinado artículo en una sucursal.
#     D) Venta de artículos: se registran las ventas realizadas informando sucursal, artículo y cantidad vendida. Se debe verificar que la cantidad vendida no exceda el stock de ese producto en esa sucursal, informando si la venta no se puede realizar por este motivo
#     E) Existencia de mercaderías: listar por pantalla cantidad existentes de mercaderías por sucursal
#     F) Salir del programa


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


class Articulo:
    def __init__(self, codigo: int, nombre: str, categoria: str, descripcion: str, cantidad: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __str__(self):
        return f"""
        \n[🆔 Código: {self.codigo}]
        \n📦 Nombre: {self.nombre}
        \n📁 Categoría: {self.categoria}
        \n📝 Descripción: {self.descripcion}
        \n📊 Cantidad: {self.cantidad} Unidades"""


class GestorArticulos:
    def __init__(self):
        self.articulos: list[Articulo] = []

    def agregar_articulo(self):
        codigo = int(input("Ingrese el código del artículo: "))

        for articulo in self.articulos:
            if articulo.codigo == codigo:
                restock = input("El artículo ya existe. ¿Desea restockearlo? (s/n): ")
                if restock.lower() == 's':
                    cantidad = int(input("Ingrese la cantidad a agregar: "))
                    articulo.cantidad += cantidad
                    print(f"Artículo {articulo} actualizado con éxito.")
                return
        else:
            nombre = input("Ingrese el nombre del artículo: ")
            categoria = input("Ingrese la categoría del artículo: ")
            descripcion = input("Ingrese la descripción del artículo: ")
            cantidad = int(input("Ingrese la cantidad del artículo: "))
            articulo = Articulo(codigo, nombre, categoria, descripcion, cantidad)
            self.articulos.append(articulo)
            print(articulo)

    def obtener_articulo_por_codigo(self, codigo: int):
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                return articulo
        print("❌ Artículo no encontrado.")
        return None

    def listar_articulos(self):
        if not self.articulos:
            print("\n❌ No hay artículos registrados.")
        else:
            print("\n📋 Lista de Artículos Registrados:")
            print("=" * 40)
            for articulo in self.articulos:
                print(articulo)
                print("=" * 40)

    def actualizar_articulo(self):
        codigo = int(input("ingrese el código del artículo a actualizar: "))
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                nombre = input("Ingrese el nuevo nombre del artículo: ")
                categoria = input("Ingrese la nueva categoría del artículo: ")
                descripcion = input("Ingrese la nueva descripción del artículo: ")
                cantidad = int(input("Ingrese la nueva cantidad del artículo: "))
                if nombre: articulo.nombre = nombre
                if categoria: articulo.categoria = categoria
                if descripcion: articulo.descripcion = descripcion
                if cantidad: articulo.cantidad = cantidad
                print(f"Artículo {articulo} actualizado con éxito.")
                return
        print("Artículo no encontrado.")

    def borrar_articulo(self):
        codigo = int(input("ingrese el código del artículo a actualizar: "))
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                self.articulos.remove(articulo)
                print(f"Artículo {articulo} borrado con éxito.")
                return


class Sucursal:
    def __init__(self, codigo: int, nombre: str, direccion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.articulos = []

    def __str__(self):
        if self.articulos:
            articulos_str = ""
            for c in self.articulos:
                articulos_str += str(c) + "\n" + "-" * 40 + "\n"
        else:
            articulos_str = "📭 No hay artículos."
        return f"""
        \n🏢 Sucursal: {self.nombre} (Código: {self.codigo})
        \n📍 Dirección: {self.direccion}
        \n📦 Artículos:\n{articulos_str}"""


class GestorSucursales:
    def __init__(self, gestor_articulos: GestorArticulos):
        self.sucursales: list[Sucursal] = []
        self.gestor = gestor_articulos

    def _validar_sucursal(self, codigo: int):
        for sucursal in self.sucursales:
            if sucursal.codigo == codigo:
                return sucursal
        return False

    def agregar_sucursal(self):
        codigo = int(input("Ingrese el código de la sucursal: "))
        if self._validar_sucursal(codigo):
            print("El código de la sucursal ya existe.")
            return

        nombre = input("Ingrese el nombre de la sucursal: ")
        direccion = input("Ingrese la dirección de la sucursal: ")
        sucursal = Sucursal(codigo, nombre, direccion)
        self.sucursales.append(sucursal)
        print(sucursal)

    def agregar_articulo_a_sucursal(self):
        "agrega un articulo a una sucursal"
        codigo_sucursal = int(input("Ingrese el código de la sucursal: "))
        sucursal = self._validar_sucursal(codigo_sucursal)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        codigo_articulo = int(input("Ingrese el código del artículo: "))
        articulo = self.gestor.obtener_articulo_por_codigo(codigo_articulo)
        if not articulo:
            return
        for s in self.sucursales:
            if articulo in s.articulos:
                print("El artículo ya esta en una sucursal.")
                return
        sucursal.articulos.append(articulo)
        print(f"Artículo {articulo} agregado a la sucursal {sucursal}.")

    def listar_sucursales(self):
        if not self.sucursales:
            print("\n❌ No hay sucursales registradas.")
        else:
            print("\n🏢 Sucursales Registradas:")
            print("=" * 50)
            for sucursal in self.sucursales:
                print(sucursal)
                print("-" * 50)
            print("\n" + "=" * 50)

    def encontrar_sucursal(self):
        codigo = int(input("Ingrese el código de la sucursal: "))
        sucursal = self._validar_sucursal(codigo)
        if sucursal:
            print(f"Sucursal encontrada: {sucursal}")
        else:
            print("Sucursal no encontrada.")

    def actualizar_sucursal(self):
        codigo = int(input("Ingrese el código de la sucursal a actualizar: "))
        sucursal = self._validar_sucursal(codigo)
        if sucursal:
            nombre = input("Ingrese el nombre del sucursal: ")
            direccion = input("Ingrese la dirección del sucursal: ")
            if nombre: sucursal.nombre = nombre
            if direccion: sucursal.direccion = direccion
            print(f"Sucursal {sucursal} actualizada con éxito.")
        else:
            print("Sucursal no encontrada.")

    def borrar_sucursal(self):
        codigo = int(input("Ingrese el código de la sucursal a borrar: "))
        sucursal = self._validar_sucursal(codigo)
        if sucursal:
            self.sucursales.remove(sucursal)
            print(f"Sucursal {sucursal} borrada con éxito.")
        else:
            print("Sucursal no encontrada.")

    def vender_articulo(self):
        codigo_sucursal = int(input("Ingrese el código de la sucursal: "))
        sucursal = self._validar_sucursal(codigo_sucursal)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        codigo_articulo = int(input("Ingrese el código del artículo: "))
        articulo = self.gestor.obtener_articulo_por_codigo(codigo_articulo)
        if not articulo:
            return
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        if cantidad_vendida > articulo.cantidad:
            print("No hay suficiente stock para realizar la venta.")
            return
        articulo.cantidad -= cantidad_vendida
        print(f"Venta realizada con éxito. Artículo {articulo.nombre} vendido en la sucursal {sucursal.nombre}.")

    def existencia_mercaderias(self):
        codigo_sucursal = int(input("Ingrese el código de la sucursal: "))
        sucursal = self._validar_sucursal(codigo_sucursal)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        if not sucursal.articulos:
            print("No hay artículos registrados en esta sucursal.")
            return
        print(f"Artículos en la sucursal {sucursal}:")
        for articulo in sucursal.articulos:
            print(f"Artículo: {articulo.nombre}, Cantidad: {articulo.cantidad}")


class Aplicacion:
    def __init__(self):
        self.menu_principal = Menu("Menu Principal",
                                   ['1- Gestion de Sucursales', '2- Gestion de Articulos', '3- Carga de Stock', '4- Venta de Articulos',
                                    '5- Existencia de Mercaderias', '6- Salir'])
        self.articulo = GestorArticulos()
        self.sucursales = GestorSucursales(self.articulo)

    def _menu_gestor_sucursales(self):
        while True:
            menu_sucursal = Menu("Menu Sucursales",
                                 ['1- Crear Sucursal', '2- Ver Sucursales', '3- Encontrar Sucursal', '4- Actualizar Sucursal', '5- Borrar Sucursal',
                                  '6- Volver'])
            menu_sucursal.mostrar_menu()
            opcion_sucursarl = menu_sucursal.pedir_opcion_de_menu_valida()
            match opcion_sucursarl:
                case 1:
                    self.sucursales.agregar_sucursal()
                case 2:
                    self.sucursales.listar_sucursales()
                case 3:
                    self.sucursales.encontrar_sucursal()
                case 4:
                    self.sucursales.actualizar_sucursal()
                case 5:
                    self.sucursales.borrar_sucursal()
                case 6:
                    input("Volviendo al menu principal...")
                    break
                case _:
                    print("Opción no válida. Debe ser un número entre 1 y 5.")

    def _menu_gestor_articulos(self):
        while True:
            menu_articulos = Menu("Menu Articulos",
                                  ['1- Crear Articulo', '2- Ver Articulos por codigo', '3- Listar articulos', '4- Actualizar Articulo',
                                   '5- Borrar Articulo', '6- Volver'])
            menu_articulos.mostrar_menu()
            opcion_articulo = menu_articulos.pedir_opcion_de_menu_valida()
            match opcion_articulo:
                case 1:
                    self.articulo.agregar_articulo()
                case 2:
                    codigo = int(input("Ingrese el código del artículo: "))
                    self.articulo.obtener_articulo_por_codigo(codigo)
                case 3:
                    self.articulo.listar_articulos()
                case 4:
                    self.articulo.actualizar_articulo()
                case 5:
                    self.articulo.borrar_articulo()
                case 6:
                    input("Volviendo al menu principal...")
                    break
                case _:
                    print("Opción no válida. Debe ser un número entre 1 y 5.")

    def ejecutar(self):
        while True:
            self.menu_principal.mostrar_menu()
            opcion = self.menu_principal.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self._menu_gestor_sucursales()
                case 2:
                    self._menu_gestor_articulos()
                case 3:
                    self.sucursales.agregar_articulo_a_sucursal()
                case 4:
                    self.sucursales.vender_articulo()
                case 5:
                    self.sucursales.existencia_mercaderias()
                case 6:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no válida. Debe ser un número entre 1 y 6.")


Aplicacion = Aplicacion()
Aplicacion.ejecutar()
