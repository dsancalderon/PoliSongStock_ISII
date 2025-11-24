from typing import List

class Usuario:
   def _init_(self, id: int, nombre: str, correo: str, password: str):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.password = password
        # PB-05 Carrito de compra
        self.carrito = []
        # Ya tenías esto:
        self.compras = []          # lista de IDs de pedidos realizados
        self.recopilaciones = []   # lista de objetos Recopilacion

    def crear_recopilacion(self, recopilacion):
        self.recopilaciones.append(recopilacion)

    def publicar_recopilacion(self, recopilacion_id):
        for r in self.recopilaciones:
            if r.id == recopilacion_id:
                r.hacer_publica()
                return r
        raise ValueError("Recopilación no encontrada")
    
