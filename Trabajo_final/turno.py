from paciente import Paciente
from medico import Medico
from generales import Fecha



class Turno:
    def __init__(self,nro_turno:int, paciente:Paciente,medico:Medico,motivo:str,fecha:Fecha):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase gestor_pac.Paciente.")
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