
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
