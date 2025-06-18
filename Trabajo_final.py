#----------IMPORTS---------------------------------------------------
import pickle as pk
from datetime import datetime
from pathlib import Path

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
    def __init__(self, fecha_str: str, horario_str: str = None):
        self.dt_objeto = None
        formato_fecha = "%d/%m/%Y"
        formato_fecha_hora = "%d/%m/%Y %H:%M"
        if horario_str:
            fecha_hora = f"{fecha_str} {horario_str}"
            try:
                fecha_dt = datetime.strptime(fecha_hora, formato_fecha_hora)
            except ValueError:
                raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")

            if fecha_dt < datetime.now():
                raise ValueError("La fecha no puede ser anterior a la fecha actual.")
        else:
            try:
                fecha_dt = datetime.strptime(fecha_str, formato_fecha)
            except ValueError:
                raise ValueError("Formato de fecha no válido. Debe ser dd/mm/aaaa")

        self.dt_objeto = fecha_dt
        self.dia = self.dt_objeto.day
        self.mes = self.dt_objeto.month
        self.anio = self.dt_objeto.year
        self.hora = self.dt_objeto.hour if horario_str else None
        self.minuto = self.dt_objeto.minute if horario_str else None

    def __str__(self):
        if self.hora is not None and self.minuto is not None:
            return self.dt_objeto.strftime("%d/%m/%Y %H:%M")
        else:
            return self.dt_objeto.strftime("%d/%m/%Y")

class merge_sort:
    """Clase para ordenar una lista de Turnos por fecha y hora usando el algoritmo Merge Sort."""

    def merge(self, lista: list, list_temp, inicio, medio, fin):
        fin_primera_parte = medio - 1
        indice_temp = inicio
        tamano_lista = fin - inicio + 1

        while inicio <= fin_primera_parte and medio <= fin:
            if lista[inicio].fecha.dt_objeto <= lista[medio].fecha.dt_objeto:
                list_temp[indice_temp] = lista[inicio]
                inicio += 1
            else:
                list_temp[indice_temp] = lista[medio]
                medio += 1
            indice_temp += 1
        while inicio <= fin_primera_parte:
            list_temp[indice_temp] = lista[inicio]
            inicio += 1
            indice_temp += 1
        while medio <= fin:
            list_temp[indice_temp] = lista[medio]
            medio += 1
            indice_temp += 1
        for i in range(0, tamano_lista):
            lista[fin] = list_temp[fin]
            fin -= 1

    def merge_sort(self,lista, list_temp, inicio, fin):
        if inicio < fin:
            medio = (inicio + fin) // 2
            self.merge_sort(lista, list_temp, inicio, medio)
            self.merge_sort(lista, list_temp, medio + 1, fin)
            self.merge(lista, list_temp, inicio, medio + 1, fin)

    def main(self,lista):
        tamano_lista = len(lista)
        lista_temp = [0] * tamano_lista
        self.merge_sort(lista, lista_temp, 0, tamano_lista - 1)
        return lista


# ---------------------------CLASES BASES---------------------------------------------------
class Paciente:
    def __init__(self,dni:str,nombre:str,fecha_nacimiento: Fecha,obra_social:str = None ):
        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("El DNI debe ser numérico y tener al menos 8 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.dni = dni
        self.nombre = nombre
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return (
            f"👤 Paciente\n"
            f"🔹 Nombre: {self.nombre}\n"
            f"🔹 DNI: {self.dni}\n"
            f"🔹 Fecha de nacimiento: {self.fecha_nacimiento}\n"
            f"🔹 Obra social: {self.obra_social if self.obra_social else 'No tiene'}"
        )

class Medico:
    def __init__(self,matricula:str,nombre:str,especialidad:str):
        if not matricula.isdigit() or len(matricula) < 6:
            raise ValueError("La matrícula debe ser numérica y tener al menos 6 dígitos.")
        self.matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return (
            f"👨‍⚕️ Médico/a\n"
            f"🔹 Nombre: Dr/a. {self.nombre}\n"
            f"🔹 Matrícula: {self.matricula}\n"
            f"🔹 Especialidad: {self.especialidad}"
        )

class Turno:
    def __init__(self,nro_turno:int, paciente:Paciente,medico:Medico,motivo:str,fecha:Fecha):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico.")
        if not isinstance(fecha, Fecha):
            raise TypeError("La fecha debe ser una instancia de la clase Fecha.")
        self.nro_turno = nro_turno
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo
        self.fecha = fecha

    def __str__(self):
        return (
            f"🔹 Turno Médico 🔹\n"
            f"📅 Fecha: {self.fecha}\n"
            f"👤 Paciente: {self.paciente.nombre} (DNI: {self.paciente.dni})\n"
            f"🏥 Obra Social: {self.paciente.obra_social or 'No tiene'}\n"
            f"🩺 Médico: Dr/a. {self.medico.nombre} (Matrícula: {self.medico.matricula})\n"
            f"📌 Motivo: {self.motivo}"
        )
# --------------------------------GESTORES---------------------------------------------------

class GestorPacientes:
    def __init__(self,file: str = "Datos/pacientes.bin"):
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

class GestorMedicos:
    def __init__(self,file: str = "Datos/medicos.bin"):
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

class GestorTurnos:
    def __init__(self, gestor_pacientes: GestorPacientes, gestor_medicos: GestorMedicos, file_bin: str = "Datos/turnos.bin", file_csv: str = "Datos/turnos.csv",informe_csv: str = "Datos/informe_turnos.csv"):
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


    def _obtener_fecha_valida(self, fecha_str: str, horario_str: str = None) -> Fecha:
        """Solicita una fecha válida al usuario hasta que sea correcta."""
        while True:
            try:
                return Fecha(fecha_str, horario_str)
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente de nuevo.")
                fecha_str = input("Ingrese la fecha (dd/mm/aaaa): ")
                horario_str = input("Ingrese la hora (hh:mm): ")

    def _validar_solapamiento(self, matricula: str, fecha: Fecha)-> bool:
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
            return
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
                turnos_medicos_ordenados = merge_sort().main(turnos_medico)

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


#--------------------------MENU---------------------------------------------------
class App:
    def __init__(self):
        Path("Datos").mkdir(exist_ok=True)  #Asegurara que carpeta datos exista, sino la crea. Yo almaceno en esa carpeta.
        self.gestor_pacientes = GestorPacientes()
        self.gestor_medicos = GestorMedicos()
        self.gestor_turnos = GestorTurnos(self.gestor_pacientes, self.gestor_medicos)
        self.gestor_medicos.gestor_turnos = self.gestor_turnos
        self.gestor_pacientes.gestor_turnos = self.gestor_turnos
        self.menu_principal = Menu(['1. Gestionar Pacientes','2. Gestionar Médicos','3. Gestionar Turnos','4. Salir'],'Menú Principal')
        self.menu_pacientes =  self._Menu_pacientes()
        self.menu_medicos = self._Menu_medicos()
        self.menu_turnos = self._Menu_turnos()

    def _Menu_pacientes(self):
        opciones = ['1. Listar Pacientes','2. Buscar Paciente por DNI','3. Agregar Paciente','4. Modificar','5. Eliminar','6. Guardar cambios','7. Volver al menú principal']
        return Menu(opciones, "Menu Pacientes")

    def _Menu_medicos(self):
        opciones = ['1. Listar Médicos','2. Buscar Médico por Matricula','3. Agregar Médico','4. Modificar','5. Eliminar','6. Guardar cambios','7. Volver al menú principal']
        return Menu(opciones, "Menu Médicos")

    def _Menu_turnos(self):
        opciones = ['1. Listar Turnos','2. Listar Turno por Paciente o Medico','3. Buscar por fecha','4. Agregar Turno','5. Eliminar','6. Guardar cambios','7. Generar informe de turnos por medico','8. Exportar CSV','9. Volver al menú principal']
        return Menu(opciones, "Menu Turnos")

    def _Menu_pacientes_ejecucion(self):
        while True:
            self.menu_pacientes.mostrar_menu()
            opcion = self.menu_pacientes.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_pacientes.listar_pacientes()
                case 2:
                    self.gestor_pacientes.buscar_por_DNI()
                case 3:
                    self.gestor_pacientes.agregar_paciente()
                case 4:
                    self.gestor_pacientes.modificar_paciente()
                case 5:
                    self.gestor_pacientes.eliminar_paciente()
                case 6:
                    self.gestor_pacientes.guardar_cambios()
                    print("Cambios guardados correctamente.")
                case 7:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")

    def _Menu_medicos_ejecucion(self):
        while True:
            self.menu_medicos.mostrar_menu()
            opcion = self.menu_medicos.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_medicos.listar_medicos()
                case 2:
                    self.gestor_medicos.buscar_por_matricula()
                case 3:
                    self.gestor_medicos.agregar_medico()
                case 4:
                    self.gestor_medicos.modificar_medico()
                case 5:
                    self.gestor_medicos.eliminar_medico()
                case 6:
                    self.gestor_medicos.guardar_cambios()
                    print("Cambios guardados correctamente.")
                case 7:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")

    def _Menu_turnos_ejecucion(self):
        while True:
            self.menu_turnos.mostrar_menu()
            opcion = self.menu_turnos.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    self.gestor_turnos.listar_turnos()
                case 2:
                    self.gestor_turnos.listar_turno_por_paciente_o_medico()
                case 3:
                    self.gestor_turnos.buscar_por_fecha()
                case 4:
                    self.gestor_turnos.agregar_turno()
                case 5:
                    self.gestor_turnos.eliminar_turno()
                case 6:
                    self.gestor_turnos.guardar_cambios()
                    print("Cambios guardados correctamente.")
                case 7:
                    self.gestor_turnos.informe_medico()
                case 8:
                    self.gestor_turnos.exportar_a_csv()
                    print('Exportación a CSV completada.')
                case 9:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")

    def iniciar(self):
        while True:
            self.menu_principal.mostrar_menu()
            opcion = self.menu_principal.pedir_opcion_de_menu_valida()
            match opcion:
                case 1:
                    print("Gestionando Pacientes...")
                    self._Menu_pacientes_ejecucion()
                case 2:
                    print("Gestionando Médicos...")
                    self._Menu_medicos_ejecucion()
                case 3:
                    print("Gestionando Turnos...")
                    self._Menu_turnos_ejecucion()
                case 4:
                    print("Saliendo de la aplicación...")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    app = App()
    app.iniciar()