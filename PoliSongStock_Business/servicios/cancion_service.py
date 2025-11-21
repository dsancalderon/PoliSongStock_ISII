from entidades.cancion import Cancion

class CancionService:
    def __init__(self):
        self.canciones = {}  # id -> Cancion

    def registrar_cancion(self, id:int, nombre:str, artista:str, precio:float, duracion:float, tamano_kb:int, calidad:str):
        if id in self.canciones:
            raise ValueError("Cancion ya existe")
        c = Cancion(id, nombre, artista, precio, duracion, tamano_kb, calidad)
        self.canciones[id] = c
        return c

    def buscar_por_nombre(self, termino:str):
        return [c for c in self.canciones.values() if termino.lower() in c.nombre.lower()]
