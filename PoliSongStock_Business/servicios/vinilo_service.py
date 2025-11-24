from typing import Dict, Optional

from entidades.vinilo import Vinilo  # asumo que existe esta clase y tiene atributos id, precio, proveedor_id

class ViniloService:
    def __init__(self):
        self.vinilos: Dict[int, Vinilo] = {}

    def registrar_vinilo(self, id: int, titulo: str, artista: str, precio: float, proveedor_id: int, stock: int = 1) -> Vinilo:
        vinilo = Vinilo(id=id, titulo=titulo, artista=artista, precio=precio, proveedor_id=proveedor_id, stock=stock)
        self.vinilos[id] = vinilo
        return vinilo

    def obtener_vinilo(self, id: int) -> Optional[Vinilo]:
        return self.vinilos.get(id)

    def buscar_vinilos(self, termino: str):
        termino_lower = termino.lower()
        return [v for v in self.vinilos.values() if termino_lower in getattr(v, "titulo", "").lower() or termino_lower in getattr(v, "artista", "").lower()]
