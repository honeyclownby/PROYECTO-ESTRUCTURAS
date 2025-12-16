from Lista import Lista
# clases.py
from datetime import datetime

# --- CLASE CONTACTO  ---
class Contacto:
    def __init__(self, nombre, ape_pat, ape_mat, direccion, estado, ciudad, 
                 fecha_nac, telefono, email_pers, matricula, email_inst, 
                 facultad, programa, fecha_ingreso, id_contacto, edad, antiguedad):
        # Datos básicos
        self.id = id_contacto # Hay que calcularlo por Hash de la matricula
        self.nombre = nombre
        self.ape_pat = ape_pat
        self.ape_mat = ape_mat
        self.direccion = direccion
        self.estado = estado
        self.ciudad = ciudad
        self.fecha_nac = fecha_nac
        self.edad = edad #Hay que calcularlo con fecha de nacimiento
        self.telefono = telefono
        self.email_pers = email_pers
        self.matricula = matricula
        self.email_inst = email_inst
        self.facultad = facultad
        self.programa = programa
        self.fecha_ingreso = fecha_ingreso
        self.antiguedad = antiguedad #Calcularlo a partir de fecha de ingreso
        
        # Fechas de sistema
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y") # Toma la fecha del sistema
        self.tiempo_actualizacion = None 

    def __str__(self):
        # Formato para mostrar en consola y reportes Aqui me apoyo chat porque no sabia que hacer
        update_str = self.tiempo_actualizacion if self.tiempo_actualizacion else "Sin cambios"
        return (f"ID: {self.id} | Matrícula: {self.matricula}\n"
                f"Nombre: {self.nombre} {self.ape_pat} {self.ape_mat}\n"
                f"Edad: {self.edad} | Antigüedad: {self.antiguedad}\n"
                f"Registro: {self.fecha_registro} | Última Act.: {update_str}\n"
                f"----------------------------------------")