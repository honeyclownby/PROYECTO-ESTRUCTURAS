class Contacto:
    def __init__(self, nombres, apellido_paterno, apellido_materno, direccion, estado, ciudad, fecha_nacimiento, telefono, correo_personal, matricula, correo_institucional, facultad, programa_educativo, fecha_ingreso):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.direccion = direccion
        self.estado = estado
        self.ciudad = ciudad
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.correo_personal = correo_personal
        self.matricula = matricula
        self.correo_institucional = correo_institucional
        self.facultad = facultad
        self.programa_educativo = programa_educativo
        self.fecha_ingreso = fecha_ingreso
        
        self.id = generarId(matricula)
        self.edad = calcularEdad(fecha_nacimiento )
        self.antiguedad = calcularAntiguedad(fecha_ingreso)
        self.fechaRegistro = FechaRegistroActu(%d/%m/%Y)
        self.tiempoActualizacion = "" 
        
        def mostrarInformacion(self):
            info = f"ID: {self.id}\n"
            info += f"Nombres: {self.nombres} {self.apellido_paterno} {self.apellido_materno}\n"
            info += f"Dirección: {self.direccion}, {self.ciudad}, {self.estado}\n"
            info += f"Fecha de Nacimiento: {self.fecha_nacimiento} (Edad: {self.edad})\n"
            info += f"Teléfono: {self.telefono}\n"
            info += f"Correo Personal: {self.correo_personal}\n"
            info += f"Matrícula: {self.matricula}\n"
            info += f"Correo Institucional: {self.correo_institucional}\n"
            info += f"Facultad: {self.facultad}\n"
            info += f"Programa Educativo: {self.programa_educativo}\n"
            info += f"Fecha de Ingreso: {self.fecha_ingreso} (Antigüedad: {self.antiguedad})\n"
            info += f"Fecha de Registro: {self.fechaRegistro}\n"
            info += f"Tiempo desde la última actualización: {self.tiempoActualizacion}\n"
            return info

        
