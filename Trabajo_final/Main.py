#----------IMPORTS---------------------------------------------------
from pathlib import Path
from gestor_medico import GestorMedicos
from gestor_paciente import GestorPacientes
from gestor_turnos import GestorTurnos
from generales import Menu





#--------------------------MENU---------------------------------------------------
class App:
    def __init__(self):
        Path("../Datos").mkdir(exist_ok=True)  #Asegurara que carpeta datos exista, sino la crea. Yo almaceno en esa carpeta.
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