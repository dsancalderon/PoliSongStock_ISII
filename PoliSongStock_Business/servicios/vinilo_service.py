from entidades.vinilo import Vinilo

class ViniloService:
    def __init__(self):
        self.vinilos = {}  # id -> Vinilo

    def registrar_vinilo(self, id:int, nombre:str, artista:str, anio:int, precio:float, stock:int):
        if id in self.vinilos:
            raise ValueError("Vinilo ya existe")
        v = Vinilo(id, nombre, artista, anio, precio, stock)
        self.vinilos[id] = v
        return v

    def asociar_cancion(self, vinilo_id:int, cancion):
        if vinilo_id not in self.vinilos:
            raise ValueError("Vinilo no encontrado")
        v = self.vinilos[vinilo_id]
        v.asociar_cancion(cancion)
        return v

    def consultar_disponibles(self):
        return [v for v in self.vinilos.values() if v.consultar_disponibilidad()]
