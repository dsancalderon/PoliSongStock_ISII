from typing import Dict, List, Callable, Optional
from entidades.pedido import Pedido, EstadoPedido

class PedidoService:
    def __init__(self, usuario_service, vinilo_service):
        # dependencias
        self.usuario_service = usuario_service
        self.vinilo_service = vinilo_service

        # almacenar pedidos por id
        self.pedidos: Dict[int, Pedido] = {}
        self._next_id = 1

    def _nuevo_id(self) -> int:
        nid = self._next_id
        self._next_id += 1
        return nid

    def crear_pedido_desde_carrito(self, usuario_id: int, medio_pago: str, observacion: str = "") -> Pedido:
        usuario = self.usuario_service.obtener_usua

