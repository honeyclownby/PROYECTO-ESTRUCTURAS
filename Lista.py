from Nodo import Nodo
from datetime import datetime
class Lista:
    def __init__(self):
        self.head = None

    def esVacio(self):
        return self.head is None

    # Insertar al final 
    def insertar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            temp = self.head
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo

    # BUSCAR CONTACTO
    # Busca internamente usando el ID generado por el Hash
    def buscar_por_id(self, id_buscado):
        temp = self.head
        while temp:
            # Accedemos a temp.dato.id porque dato es un objeto Contacto
            if temp.dato.id == id_buscado:
                return temp.dato # Retorna el objeto Contacto
            temp = temp.siguiente
        return None

    # ACTUALIZAR CONTACTO
    # Solo actualiza el dato (valor) del nodo
    def actualizar_contacto(self, id_buscado, nuevo_contacto):
        temp = self.head
        while temp:
            if temp.dato.id == id_buscado:
                # Actualizamos el campo tiempo_actualizacion antes de guardar
                nuevo_contacto.tiempo_actualizacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                # Reemplazamos el valor del nodo
                temp.dato = nuevo_contacto
                return True
            temp = temp.siguiente
        return False

    # ELIMINAR CONTACTO 
    # Quitar el nodo completo y volver a enlazar
    def eliminar_por_id(self, id_buscado):
        if self.head is None:
            return False
        
        temp = self.head
        previo = None

        while temp:
            if temp.dato.id == id_buscado:
                if previo is None: # Es la cabeza
                    self.head = temp.siguiente
                else:
                    previo.siguiente = temp.siguiente
                return True
            previo = temp
            temp = temp.siguiente
        return False
    
    # Método auxiliar para reportes Para este me apoyo chat, hay que ver bien que pedo
    def obtener_todos(self):
        contactos = []
        temp = self.head
        while temp:
            contactos.append(temp.dato)
            temp = temp.siguiente
        return contactos