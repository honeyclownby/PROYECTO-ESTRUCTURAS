from Contacto import Contacto, generarId, calcularEdad, calcularAntiguedad
from Nodo import Nodo

class Lista:
    def __init__(self):
        self.cabeza = None 
        self.longitud = 0

    def insertar_contacto(self, nuevo_contacto):
        nuevo_nodo = Nodo(nuevo_contacto)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
        self.longitud += 1
        return True
    def buscar_por_id(self, id_buscado):
        actual = self.cabeza
        
        while actual is not None:
            if actual.dato.id == id_buscado:
                return actual.dato
            actual = actual.siguiente
        return None
      
    def actualizar_contacto(self, id_a_actualizar, nuevos_datos_contacto):
        actual = self.cabeza
        
        while actual is not None:
            if actual.dato.id == id_a_actualizar:
                contacto_existente = actual.dato
              
                if nuevos_datos_contacto.nombres: 
                    contacto_existente.nombres = nuevos_datos_contacto.nombres
                if nuevos_datos_contacto.apellido_paterno: 
                    contacto_existente.apellido_paterno = nuevos_datos_contacto.apellido_paterno
                if nuevos_datos_contacto.apellido_materno: 
                    contacto_existente.apellido_materno = nuevos_datos_contacto.apellido_materno
                if nuevos_datos_contacto.direccion: 
                    contacto_existente.direccion = nuevos_datos_contacto.direccion
                if nuevos_datos_contacto.estado: 
                    contacto_existente.estado = nuevos_datos_contacto.estado
                if nuevos_datos_contacto.ciudad: 
                    contacto_existente.ciudad = nuevos_datos_contacto.ciudad
                if nuevos_datos_contacto.telefono: 
                    contacto_existente.telefono = nuevos_datos_contacto.telefono
                if nuevos_datos_contacto.correo_personal: 
                    contacto_existente.correo_personal = nuevos_datos_contacto.correo_personal
                if nuevos_datos_contacto.correo_institucional: 
                    contacto_existente.correo_institucional = nuevos_datos_contacto.correo_institucional
                if nuevos_datos_contacto.facultad: 
                    contacto_existente.facultad = nuevos_datos_contacto.facultad
                if nuevos_datos_contacto.programa_educativo: 
                    contacto_existente.programa_educativo = nuevos_datos_contacto.programa_educativo

                if nuevos_datos_contacto.fecha_nacimiento: 
                    contacto_existente.fecha_nacimiento = nuevos_datos_contacto.fecha_nacimiento
                    contacto_existente.edad = calcularEdad(contacto_existente.fecha_nacimiento)
                  
                if nuevos_datos_contacto.fecha_ingreso:
                    contacto_existente.fecha_ingreso = nuevos_datos_contacto.fecha_ingreso
                    contacto_existente.antiguedad = calcularAntiguedad(contacto_existente.fecha_ingreso)

                contacto_existente.actualizar_tiempo() 
                return True 
            
            actual = actual.siguiente
            
        return False

    def eliminar_contacto(self, id_a_eliminar):
        actual = self.cabeza
        anterior = None
        
        if actual is None:
            return False
            
        while actual is not None and actual.dato.id != id_a_eliminar:
            anterior = actual
            actual = actual.siguiente
            
        if actual is None:
            return False
            
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente 
            
        self.longitud -= 1
        return True
        
    def obtener_todos_los_contactos(self):
        contactos = []
        actual = self.cabeza
        while actual is not None:
            contactos.append(actual.dato)
            actual = actual.siguiente
        return contactos

  
