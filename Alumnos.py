from datetime import datetime


class GestorAlumnos:
    def __init__(self):
        self.alumnos: list[dict] = []
        self.codigo_alumno = 1

    def crear_alumno(self, nombre: str, apellido: str, telefono: str, fecha_nacimiento):
        codigo_alumno_codificado = f"{self.codigo_alumno:03d}"
        # corroborar que el alumno no existe
        for alumno in self.alumnos:
            if alumno["nombre"] == nombre and alumno["apellido"] == apellido:
                raise ValueError(f"El alumno {nombre} {apellido} ya existe.")
        # Generar alumno
        fecha = Fecha(fecha_nacimiento)
        nuevo_alumno = {
            "codigo_alumno": codigo_alumno_codificado,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "fecha_nacimiento": fecha
        }
        self.alumnos.append(nuevo_alumno)
        self.codigo_alumno += 1

    def modificar_alumno(self, codigo_alumno: str, nombre: str = None, apellido: str = None, telefono: str = None):
        for alumno in self.alumnos:
            if alumno["codigo_alumno"] == codigo_alumno:
                if nombre:
                    alumno["nombre"] = nombre
                if apellido:
                    alumno["apellido"] = apellido
                if telefono:
                    alumno["telefono"] = telefono
                return
        raise ValueError(f"El alumno con código {codigo_alumno} no existe.")

    def elimar_alumno(self, codigo_alumno: str):
        for alumno in self.alumnos:
            if alumno["codigo_alumno"] == codigo_alumno:
                self.alumnos.remove(alumno)
                return
        raise ValueError(f"El alumno con código {codigo_alumno} no existe.")

    def mostrar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return
        print("Lista de Alumnos:")
        for alumno in self.alumnos:
            print(
                f"{alumno['codigo_alumno']} - Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}, Telefono: {alumno['telefono']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}")

    def buscar_alumno(self, codigo_alumno: str):
        for alumno in self.alumnos:
            if alumno["codigo_alumno"] == codigo_alumno:
                return alumno
        raise ValueError(f"El alumno con código {codigo_alumno} no existe.")


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
                raise ValueError('Formato de fecha no válido. No existe el día o mes indicado.')

            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"


gestor = GestorAlumnos()
while True:
    print("""\t ---MENU DE ALUMNOS---
    1. Crear nuevo alumno
    2. Modificar alumno
    3. Eliminar alumno
    4. Ver alumnos
    5. Buscar alumno por Codigo de Alumno
    6. Salir del programa""")
    opcion = input("\tIngrese una opción: ")

    match opcion:
        case "1":
            print("Creando alumno...")
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            telefono = input("Ingrese el teléfono del alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")
            gestor.crear_alumno(nombre, apellido, telefono, fecha_nacimiento)
        case "2":
            codigo = input("Ingrese el código del alumno a modificar: ")
            if codigo != gestor.alumnos[0]["codigo_alumno"]:
                print(f"El código {codigo} no existe.")
                continue
            nombre = input("Ingrese el nuevo nombre del alumno (dejar vacío para no modificar): ")
            apellido = input("Ingrese el nuevo apellido del alumno (dejar vacío para no modificar): ")
            telefono = input("Ingrese el nuevo teléfono del alumno (dejar vacío para no modificar): ")
            gestor.modificar_alumno(codigo, nombre, apellido, telefono)
        case "3":
            codigo = input("Ingrese el código del alumno a eliminar: ")
            gestor.elimar_alumno(codigo)
            input("\nElimanando alumno...\n")
        case "4":
            gestor.mostrar_alumnos()
            input()
        case "5":
            print('Buscando alumno por código...')
            codigo = input("Ingrese el código del alumno (000): ")
            if len(codigo) > 3:
                print("El código debe tener 3 dígitos.")
                continue
            gestor.buscar_alumno(codigo)
        case "6":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
