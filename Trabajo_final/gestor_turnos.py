import pickle as pk
import generales as gen
import gestor_paciente as gestor_pac
import gestor_medico as gestor_med
from paciente import Paciente
from medico import Medico
from turno import Turno

class GestorTurnos:
    def __init__(self, gestor_pacientes: gestor_pac, gestor_medicos: gestor_med, file_bin: str = "../Datos/turnos.bin", file_csv: str = "../Datos/turnos.csv",informe_csv: str = "../Datos/informe_turnos.csv"):
        self.gestor_pacientes = gestor_pacientes
        self.gestor_medicos = gestor_medicos
        self.file_bin = file_bin
        self.file_csv = file_csv
        self.informe_csv = informe_csv
        try:
            with open(self.file_bin, 'rb') as bfile:
                self.turnos: list[Turno] = pk.load(bfile)
        except (FileNotFoundError, EOFError):
            self.turnos: list[Turno] = []
            with open(self.file_bin, 'wb') as bfile:
                pk.dump(self.turnos, bfile)

    def guardar_cambios(self):
        """Guarda los turnos en binario y CSV."""
        try:
            with open(self.file_bin, 'wb') as bfile:
                pk.dump(self.turnos, bfile)
        except Exception as e:
            print(f"Error al guardar los cambios: {e}")

    def exportar_a_csv(self):
        """Exporta los turnos actuales a un archivo CSV."""
        try:
            with open(self.file_csv, 'w', newline='', encoding='utf-8') as cfile:
                cfile.write('Nro_turno;Medico_Matricula;Medico_Nombre;Paciente_DNI;Paciente_Nombre;Fecha\n')
                for turno in self.turnos:
                    linea = f"{turno.nro_turno};{turno.medico.matricula};{turno.medico.nombre};{turno.paciente.dni};{turno.paciente.nombre};{turno.fecha}\n"
                    cfile.write(linea)
        except Exception as e:
            print(f"Error al exportar a CSV: {e}")


    def _obtener_fecha_valida(self, fecha_str: str, horario_str: str = None) -> gen.Fecha:
        """Solicita una fecha válida al usuario hasta que sea correcta."""
        while True:
            try:
                return gen.Fecha(fecha_str, horario_str)
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente de nuevo.")
                fecha_str = input("Ingrese la fecha (dd/mm/aaaa): ")
                horario_str = input("Ingrese la hora (hh:mm): ")

    def _validar_solapamiento(self, matricula: str, fecha: gen.Fecha)-> bool:
        """Verifica si el médico ya tiene un turno agendado en la misma fecha y hora. SI tiene da True."""
        for turno in self.turnos:
            if (turno.medico.matricula == matricula and
                turno.fecha.dt_objeto == fecha.dt_objeto):
                    return True
        return False

    def _encontrar_paciente(self)-> Paciente | None:
        """Encuentra un paciente por su DNI."""
        dni = input("Ingrese el DNI del paciente: ")
        paciente = self.gestor_pacientes.buscar_DNI(dni)
        if paciente is None:
            print("Paciente no encontrado.")
            return None
        return paciente

    def _encontrar_medico(self)-> Medico | None:
        """Encuentra un médico por su matrícula."""
        matricula = input('Ingrese la matrícula del médico: ')
        medico = self.gestor_medicos.buscar_matricula(matricula)
        if medico is None:
            print("Médico no encontrado.")
            return None
        return medico

    def _generar_nro_unico(self)-> int:
        """Genera un número único para el turno."""
        if not self.turnos:
            return 1
        return max(turno.nro_turno for turno in self.turnos) + 1

    def listar_turnos(self):
        """listar turnos."""
        if not self.turnos:
            print("No hay turnos registrados.")
        else:
            print("Lista de Turnos:")
            for turno in self.turnos:
                print(turno)
                print("---------------------")

    def listar_turno_por_paciente_o_medico(self):
        """Listar turnos por paciente o médico."""
        print("1. Buscar por Paciente")
        print("2. Buscar por Médico")
        opcion = input("Seleccione una opción (1-2): ")
        if opcion == '1':
            paciente = self._encontrar_paciente()
            if paciente is None:
                return
            print(f"Turnos del Paciente {paciente.nombre} (DNI: {paciente.dni}):")
            for turno in self.turnos:
                if turno.paciente.dni == paciente.dni:
                    print(turno)
                    print("---------------------")
                else:
                    print('No hay turnos registrados para este paciente.')
        elif opcion == '2':
            medico = self._encontrar_medico()
            if medico is None:
                return
            print(f"Turnos del Médico {medico.nombre} (Matrícula: {medico.matricula}):")
            for turno in self.turnos:
                if turno.medico.matricula == medico.matricula:
                    print(turno)
                    print("---------------------")
                else:
                    print('No hay turnos registrados para este médico.')
        else:
            print('Opción no válida. Debe ser 1 o 2.')

    def buscar_por_fecha(self):
        """Buscar turnos por fecha."""
        fecha_a_buscar = input("Ingrese la fecha a buscar (dd/mm/aaaa): ")
        fecha_a_buscar = self._obtener_fecha_valida(fecha_a_buscar)
        for turno in self.turnos:
            if turno.fecha.dt_objeto == fecha_a_buscar.dt_objeto:
                print(turno)
                print("---------------------")
            else:
                print("No se encontraron turnos para la fecha especificada.")

    def agregar_turno(self):
        """agregar turno."""
        paciente = self._encontrar_paciente()
        if not paciente: return
        self.gestor_medicos.listar_medicos()
        medico = self._encontrar_medico()
        if not medico: return
        while True:
            fecha_turno_str = input("Ingrese la fecha del turno (dd/mm/aaaa): ")
            horario_turno_str = input("Ingrese la hora del turno (hh:mm): ")
            fecha_turno = self._obtener_fecha_valida(fecha_turno_str, horario_turno_str)
            solapamiento = self._validar_solapamiento(medico.matricula,fecha_turno)
            if solapamiento:
                print("El médico ya tiene un turno agendado en esa fecha y hora.")
                return
            break
        motivo = input("Ingrese el motivo del turno: ")
        nro_turno = self._generar_nro_unico()
        nuevo_turno = Turno(nro_turno,paciente, medico, motivo, fecha_turno)
        self.turnos.append(nuevo_turno)
        self.guardar_cambios()
        print(f"Turno agregado correctamente:\n{nuevo_turno}")

    def eliminar_turno(self):
        """Eliminar un turno"""
        paciente = self._encontrar_paciente()
        if paciente is None:
            return
        print(f"Turnos del Paciente {paciente.nombre} (DNI: {paciente.dni}):")
        for turno in self.turnos:
            if turno.paciente.dni == paciente.dni:
                print(turno)
                print("---------------------")
            else:
                print('No hay turnos registrados para este paciente.')
        medico = self._encontrar_medico()
        if not medico: return
        fecha_turno_str = input("Ingrese la fecha del turno a eliminar (dd/mm/aaaa): ")
        horario_turno_str = input("Ingrese la hora del turno a eliminar (hh:mm): ")
        fecha_turno = self._obtener_fecha_valida(fecha_turno_str, horario_turno_str)

        turno_a_eliminar = None
        for turno in self.turnos:
            if (turno.paciente.dni == paciente.dni and
                    turno.medico.matricula == medico.matricula and
                    turno.fecha.dt_objeto == fecha_turno.dt_objeto):
                turno_a_eliminar = turno
                break

        if turno_a_eliminar:
            opcion = input('¿Estás seguro de que deseas eliminar este turno? (s/n): ')
            if opcion.lower() == 's':
                self.turnos.remove(turno_a_eliminar)
                self.guardar_cambios()
                print(f"Turno eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un turno con los datos proporcionados.")

    def _informe_csv(self, medico: Medico):
        nombre_archivo = f"Datos/informe_turnos_{medico.nombre}.csv"
        try:
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as cfile:
                cfile.write('Nro_turno;Medico_Matricula;Medico_Nombre;Paciente_DNI;Paciente_Nombre;Fecha\n')
                turnos_medico = [turno for turno in self.turnos if turno.medico.matricula == medico.matricula]
                turnos_medicos_ordenados = gen.merge_sort().main(turnos_medico)

                for turno in turnos_medicos_ordenados:
                    linea = f"{turno.nro_turno};{turno.medico.matricula};{turno.medico.nombre};{turno.paciente.dni};{turno.paciente.nombre};{turno.fecha}\n"
                    cfile.write(linea)
        except Exception as e:
            print(f"Error al generar el informe: {e}")

    def informe_medico(self):
        """Genera un informe de turnos por médico."""
        self.gestor_medicos.listar_medicos()
        matricula = input("Ingrese la matrícula del médico: ")
        medico = self.gestor_medicos.buscar_matricula(matricula)
        if medico is None:
            print("Médico no encontrado.")
            return
        print(f"Generando informe de turnos para el médico {medico.nombre} (Matrícula: {medico.matricula})...")
        self._informe_csv(medico)
