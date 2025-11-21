from entidades.pedido import Pedido, EstadoPedido
from excepciones.errores_negocio import PedidoNoValidoError, ViniloSinStockError

class PedidoService:
    def __init__(self, vinilo_service, cancion_service, proveedor_service):
        self.pedidos = {}  # id -> Pedido
        self.vinilo_service = vinilo_service
        self.cancion_service = cancion_service
        self.proveedor_service = proveedor_service

    def crear_pedido(self, id:int, usuario_id:int, items:list, medio_pago:str, observacion:str=""):
        # Validaciones básicas
        if not items:
            raise PedidoNoValidoError("Un pedido debe tener al menos un item")
        # verificar stock para vinilos
        for it in items:
            if it["tipo"] == "vinilo":
                vinilo = self.vinilo_service.vinilos.get(it["id"])
                if not vinilo:
                    raise PedidoNoValidoError("Vinilo no existe")
                if vinilo.stock < it.get("cantidad",1):
                    raise ViniloSinStockError("No hay suficiente stock")
        p = Pedido(id, usuario_id, items, medio_pago, observacion)
        self.pedidos[id] = p
        return p

    def confirmar_pedido(self, pedido_id:int, proveedor_id:int):
        # solo proveedor autenticado puede confirmar
        if not self.proveedor_service.esta_autenticado(proveedor_id):
            raise PermissionError("ProveedorNoAutenticadoError")
        p = self.pedidos.get(pedido_id)
        if not p:
            raise PedidoNoValidoError("Pedido no existe")
        p.cambiar_estado(EstadoPedido.CONFIRMADO)
        # reducir stock
        for it in p.items:
            if it["tipo"] == "vinilo":
                v = self.vinilo_service.vinilos[it["id"]]
                v.reducir_stock(it.get("cantidad",1))
        return p

    def calcular_total(self, pedido_id:int):
        p = self.pedidos.get(pedido_id)
        if not p:
            raise PedidoNoValidoError("Pedido no existe")
        return p.calcular_total(self._lookup)

    def _lookup(self, tipo, id_):
        if tipo == "vinilo":
            return self.vinilo_service.vinilos[id_]
        else:
            return self.cancion_service.canciones[id_]
