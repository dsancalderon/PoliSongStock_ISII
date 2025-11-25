from typing import Dict, Optional
from entidades.proveedor import Proveedor  # asumo que existe esta clase con id, nombre, correo

class ProveedorService:
    def __init__(self, pedido_service=None):
        self.proveedores: Dict[int, Proveedor] = {}
        self.pedido_service = pedido_service  # optional dependency

    def registrar_proveedor(self, id: int, nombre: str, correo: str) -> Proveedor:
        if id in self.proveedores:
            raise ValueError("Proveedor ya existe con ese id")
        p = Proveedor(id=id, nombre=nombre, correo=correo)
        self.proveedores[id] = p
        return p

    def obtener_proveedor(self, id: int) -> Optional[Proveedor]:
        return self.proveedores.get(id)

    def consultar_pedidos(self, proveedor_id: int):
        if self.pedido_service is None:
            raise ValueError("PedidoService no inyectado en ProveedorService")
        return self.pedido_service.obtener_pedidos_proveedor(proveedor_id)