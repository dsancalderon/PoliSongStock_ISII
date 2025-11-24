from typing import List

class Usuario:
    def __init__(self, id: int, nombre: str, correo: str):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.compras = []          # list of Pedido IDs
        self.recopilaciones = []   # list of Recopilacion objects

    def crear_recopilacion(self, recopilacion):
        self.recopilaciones.append(recopilacion)

    def publicar_recopilacion(self, recopilacion_id):
        for r in self.recopilaciones:
            if r.id == recopilacion_id:
                r.hacer_publica()
                return r
        raise ValueError("Recopilación no encontrada")
