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