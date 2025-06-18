import pickle as pk
from medico import Medico


class GestorMedicos:
    def __init__(self,file: str = "../Datos/medicos.bin"):
        try:
            self.file = file
            self.gestor_turnos = None
            with open(self.file, 'rb') as bfile:
                self.medicos: list[Medico] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.medicos: list[Medico] = []
            with open(self.file, 'wb') as bfile:
                pk.dump(self.medicos, bfile)

    def _validar_matricula(self, matricula: str) -> str:
        """Valida la matricula"""
        if not matricula.isdigit() or len(matricula) <= 5:
            raise ValueError("La matrícula debe ser numérica y tener al menos 5 dígitos.")
        return matricula

    def buscar_matricula(self, matricula: str) -> Medico | None:
        """Buscar un medico por su matrícula."""
        try:
            matricula_validada = self._validar_matricula(matricula)
            for medico in self.medicos:
                if medico.matricula == matricula_validada:
                    return medico
            return None
        except ValueError as e:
            print(f"Error al buscar médico: {e}")
            return None

    def guardar_cambios(self):
        """Guarda los cambios realizados en la lista de médicos."""
        with open(self.file, 'wb') as bfile:
            pk.dump(self.medicos, bfile)


    def listar_medicos(self):
        """Lista Todos los médicos."""
        if not self.medicos:
            print("No hay médicos registrados.")
        else:
            print("Lista de Médicos:")
            for medico in self.medicos:
                print(medico)
                print("---------------------")

    def buscar_por_matricula(self):
        matricula = input("Introduce la matrícula: ")
        medico = self.buscar_matricula(matricula)
        if medico is None:
            print("Médico no encontrado.")
            return
        print(f"Médico encontrado:\n{medico}")

    def agregar_medico(self):
        """Agregar nuevo medico."""
        while True:
            matricula = input("Introduce la matrícula: ")
            medico = self.buscar_matricula(matricula)
            if medico is not None:
                print("Ya existe un médico con esa matrícula.")
                continue
            break
        nombre = input("Introduce el nombre del médico: ")
        especialidad = input("Introduce la especialidad del médico: ")
        nuevo_medico = Medico(matricula, nombre, especialidad)
        self.medicos.append(nuevo_medico)
        self.guardar_cambios()
        print(f"Médico {nuevo_medico.nombre} agregado correctamente.")

    def modificar_medico(self):
        """modificar a un medico."""
        matricula  = input("Introduce la matrícula: ")
        medico = self.buscar_matricula(matricula)
        if medico is None:
            print("Médico no encontrado.")
            return
        print(f"Médico encontrado:\n{medico}")
        nombre = input("Introduce el nuevo nombre del médico (o dejar vacio para no modificar): ")
        especialidad = input("Introduce la nueva especialidad del médico (o dejar vacio para no modificar): ")
        if nombre:
            medico.nombre = nombre
        else:
            print("nombre no modificado")
        if especialidad:
            medico.especialidad = especialidad
        else:
            print("especialidad no modificada")
        self.guardar_cambios()

    def eliminar_medico(self):
        """Elimina un médico por su matrícula."""
        matricula = input("Introduce la matrícula: ")
        medico = self.buscar_matricula(matricula)
        if medico is None:
            print("Médico no encontrado.")
            return
        print(f"Médico encontrado:\n{medico}")
        opcion = input(f"¿Estás seguro de que deseas eliminar al médico {medico.nombre} (Matrícula: {medico.matricula})? (s/n): ")
        if opcion.lower() == 's':
            self.medicos.remove(medico)
            if self.gestor_turnos:
                # Eliminar turnos asociados al médico
                turnos = [turno for turno in self.gestor_turnos.turnos if turno.medico.matricula == medico.matricula]
                for turno in turnos:
                    self.gestor_turnos.turnos.remove(turno)
            # Guardar cambios en médicos y turnos
            self.gestor_turnos.guardar_cambios()
            self.guardar_cambios()
            print(f"Médico {medico.nombre} eliminado correctamente.")