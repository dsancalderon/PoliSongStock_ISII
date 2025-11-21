from enum import Enum
from datetime import datetime

class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    RECHAZADO = "rechazado"
    ENVIADO = "enviado"
    RECIBIDO = "recibido"

class Pedido:
    def __init__(self, id: int, usuario_id: int, items: list, medio_pago: str, observacion: str = ""):
        self.id = id
        self.usuario_id = usuario_id
        self.items = items   # list of dicts: {"tipo":"vinilo"/"cancion", "id": int, "cantidad": int}
        self.estado = EstadoPedido.PENDIENTE
        self.fecha = datetime.now()
        self.medio_pago = medio_pago
        self.observacion = observacion
        self.fecha_envio_estimada = None

    def calcular_total(self, catalog_lookup):
        total = 0.0
        for it in self.items:
            obj = catalog_lookup(it["tipo"], it["id"])
            total += obj.precio * it.get("cantidad", 1)
        return total

    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        self.estado = nuevo_estado

    def confirmar_recepcion(self):
        self.estado = EstadoPedido.RECIBIDO
