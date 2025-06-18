from generales import Fecha

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