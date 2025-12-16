
from datetime import datetime, date

def calcularEdad(fecha_nacimiento_str):
    try:
        dia, mes, anio = map(int, fecha_nacimiento_str.split('/'))
        fecha_nac = date(anio, mes, dia)
        hoy = date.today()
        edad_calculada = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad_calculada
    except:
        return 0 

def generarId(matricula_str):
    return abs(hash(matricula_str)) % 1000000

def obtenerFechaHoraActual(formato):
    return datetime.now().strftime(formato)

def calcularAntiguedad(fecha_ingreso_str):
    try:
        dia, mes, anio = map(int, fecha_ingreso_str.split('/'))
        fecha_ingreso = date(anio, mes, dia)
        hoy = date.today()
        antiguedad_calculada = hoy.year - fecha_ingreso.year - ((hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day))
        return antiguedad_calculada
    except:
        return 0

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
        lineas = []
        lineas.append(f"+++ CONTACTO DE ALUMNO: {self.matricula} ({self.id}) +++")
        lineas.append(f"  Nombre completo: {self.nombres} {self.apellido_paterno} {self.apellido_materno}")
        lineas.append(f"  Dirección: {self.direccion}, {self.ciudad}, {self.estado}")
        lineas.append(f"  Teléfono: {self.telefono} | Correo Personal: {self.correo_personal}")
        lineas.append(f"  Correo Institucional: {self.correo_institucional}")
        lineas.append(f"  Facultad / Programa: {self.facultad} / {self.programa_educativo}")
        lineas.append(f"  Datos Calculados:")
        lineas.append(f"    Fecha Nacimiento: {self.fecha_nacimiento} (Edad: {self.edad} años)")
        lineas.append(f"    Fecha Ingreso: {self.fecha_ingreso} (Antigüedad: {self.antiguedad} años)")
        lineas.append(f"    Fecha de Registro: {self.fecha_registro}")
        lineas.append(f"    Tiempo de Actualización: {self.tiempo_actualizacion if self.tiempo_actualizacion else 'N/A'}")

        return "\n".join(lineas)

        
