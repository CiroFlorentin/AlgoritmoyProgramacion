import generales as gen
from generales import Fecha
import pickle as pk
from paciente import Paciente

class GestorPacientes:
    def __init__(self,file: str = "../Datos/pacientes.bin"):
        try:
            self.file = file
            self.gestor_turnos = None
            with open(self.file, 'rb') as bfile:
                self.pacientes: list[Paciente] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.pacientes: list[Paciente] = []
            with open(self.file, 'wb') as bfile:
                pk.dump(self.pacientes, bfile)

    def _validar_DNI(self,dni: str) -> str:
        """Valida el DNI ingresado por el usuario."""
        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("DNI inválido. Debe ser numérico y tener 8 dígitos.")
        return dni

    def buscar_DNI(self,dni)-> Paciente | None:
        """Buscar un paciente por su DNI."""
        try:
            dni_validado = self._validar_DNI(dni)
            for paciente in self.pacientes:
                if paciente.dni == dni_validado:
                    return paciente
            return None
        except ValueError as e:
            print(f"Error al buscar paciente: {e}")
            return None

    def _fecha_valida(self, fecha_str)-> Fecha:
        """Valida el formato de la fecha ingresada."""
        while True:
            try:
                return Fecha(fecha_str)
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente de nuevo.")
                fecha_str = input("Ingrese la fecha (dd/mm/aaaa): ")

    def guardar_cambios(self):
        """Guarda los cambios realizados en la lista de pacientes."""
        with open(self.file, 'wb') as bfile:
            pk.dump(self.pacientes, bfile)


    def listar_pacientes(self):
        """Lista Todos los pacientes."""
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            print("Lista de Pacientes:")
            for paciente in self.pacientes:
                print(paciente)
                print("---------------------")

    def buscar_por_DNI(self):
        """Busca un paciente por su DNI."""
        dni = input("Introduce el DNI: ")
        paciente = self.buscar_DNI(dni)
        if paciente is None:
            print("Paciente no encontrado.")
            return
        print(f"Paciente encontrado:\n{paciente}")

    def agregar_paciente(self):
        """Agrega un nuevo paciente."""
        while True:
            dni = input("Introduce el DNI: ")
            try:
                self._validar_DNI(dni)
                if self.buscar_DNI(dni):
                    print("Ya existe un paciente con ese DNI.")
                    continue
                break
            except ValueError as e:
                print(f"Error: {e}")

        nombre = input("Introduce el nombre del paciente: ")
        while True:
            try:
                fecha_nacimiento_str = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
                fecha_nacimiento = Fecha(fecha_nacimiento_str)
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente de nuevo.")
        obra_social = input("Introduce la obra social (opcional): ")
        nuevo_paciente = Paciente(dni, nombre, fecha_nacimiento, obra_social)
        self.pacientes.append(nuevo_paciente)
        self.guardar_cambios()
        print(f"Paciente {nuevo_paciente.nombre} agregado correctamente.")

    def modificar_paciente(self):
        """modificar a un paciente."""
        dni = input("Introduce el DNI: ")
        paciente = self.buscar_DNI(dni)
        if paciente is None:
            print("Paciente no encontrado.")
        else:
            print(f"Paciente encontrado:\n{paciente}")
        nombre = input("Introduce el nuevo nombre del paciente (o dejar vacio para no modificar): ")
        fecha_nacimiento_str = input("Introduce la nueva fecha de nacimiento (dd/mm/aaaa) (o dejar vacio para no modificar): ")
        fecha_nacimiento_str = self._fecha_valida(fecha_nacimiento_str)
        obra_social = input("Introduce la nueva obra social (opcional): ")
        if nombre:
            paciente.nombre = nombre
        else:
            print("Nombre no modificado")
        if fecha_nacimiento_str:
            paciente.fecha_nacimiento = fecha_nacimiento_str
        else:
            print("Fecha de nacimiento no modificada")
        if obra_social:
            paciente.obra_social = obra_social
        else:
            print("Obra social no modificada")
        self.guardar_cambios()

    def eliminar_paciente(self):
        """Elimina un paciente por su DNI."""
        dni = input("Introduce el DNI: ")
        paciente = self.buscar_DNI(dni)
        if paciente is None:
            print("Paciente no encontrado.")
            return
        print(f"Paciente encontrado:\n{paciente}")
        opcion = input(f"¿Estás seguro de que deseas eliminar al paciente {paciente.nombre} (DNI: {paciente.dni})? (s/n): ")
        if opcion.lower() == 's':
            self.pacientes.remove(paciente)
            if self.gestor_turnos:
                # Eliminar turnos asociados al paciente
                turnos = [turno for turno in self.gestor_turnos.turnos if turno.paciente.dni == paciente.dni]
                for turno in turnos:
                    self.gestor_turnos.turnos.remove(turno)
            # Guardar cambios en pacientes y turnos
            self.gestor_turnos.guardar_cambios()
            self.guardar_cambios()
            print(f"Paciente {paciente.nombre} eliminado correctamente.")
