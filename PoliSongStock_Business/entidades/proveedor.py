from typing import List

class Proveedor:
    def __init__(self, id: int, nombre: str, correo: str):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.catalogo = {}        # vinilo_id -> Vinilo
        self.pedidos_recibidos = []  # list of Pedido ids

    def registrar_vinilo(self, vinilo):
        if vinilo.id in self.catalogo:
            raise ValueError("Vinilo ya registrado por este proveedor")
        self.catalogo[vinilo.id] = vinilo

    def consultar_pedidos(self):
        return list(self.pedidos_recibidos)
