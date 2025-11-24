from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional

class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    RECHAZADO = "rechazado"
    ENVIADO = "enviado"
    RECIBIDO = "recibido"

class Pedido:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        items: List[Dict],
        medio_pago: str,
        observacion: str = "",
        proveedor_id: Optional[int] = None
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.items = items   # list of dicts: {"tipo":"vinilo"/"cancion", "id": int, "cantidad": int}
        self.estado = EstadoPedido.PENDIENTE
        self.fecha = datetime.now()
        self.medio_pago = medio_pago
        self.observacion = observacion
        self.fecha_envio_estimada = None
        self.proveedor_id = proveedor_id  # nuevo: opcional para PB-15

    def calcular_total(self, catalog_lookup):
        total = 0.0
        for it in self.items:
            obj = catalog_lookup(it["tipo"], it["id"])
            # asume que el objeto tiene atributo 'precio'
            total += getattr(obj, "precio", 0.0) * it.get("cantidad", 1)
        return total

    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        self.estado = nuevo_estado

    def confirmar_recepcion(self):
        self.estado = EstadoPedido.RECIBIDO
