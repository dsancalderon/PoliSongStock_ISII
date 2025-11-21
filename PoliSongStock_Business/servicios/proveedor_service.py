from entidades.proveedor import Proveedor
from excepciones.errores_negocio import ProveedorNoAutenticadoError

class ProveedorService:
    def __init__(self):
        self.proveedores = {}  # id -> Proveedor
        self.authenticated = set()

    def registrar_proveedor(self, id:int, nombre:str, correo:str):
        if id in self.proveedores:
            raise ValueError("Proveedor ya existe")
        p = Proveedor(id, nombre, correo)
        self.proveedores[id] = p
        return p

    def autenticar(self, proveedor_id:int):
        if proveedor_id not in self.proveedores:
            raise ProveedorNoAutenticadoError("Proveedor no registrado")
        self.authenticated.add(proveedor_id)
        return True

    def esta_autenticado(self, proveedor_id:int):
        return proveedor_id in self.authenticated
