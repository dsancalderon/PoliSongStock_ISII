from typing import List

class Usuario:
   def __init__(self, id: int, nombre: str, correo: str, password: str):
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
    
    def agregar_al_carrito(self, usuario_id, vinilo):
    usuario = self.buscar_usuario_por_id(usuario_id)
    if usuario is None:
        raise ValueError("Usuario no encontrado")

    usuario.carrito.append(vinilo)
    return True
