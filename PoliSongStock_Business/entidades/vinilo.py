from typing import List

class Vinilo:
    def __init__(self, id: int, nombre: str, artista: str, anio: int, precio: float, stock: int):
        if precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        if stock < 0:
            raise ValueError("Stock no puede ser negativo")
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.anio = anio
        self.canciones = []  # list of Cancion
        self.precio = precio
        self.stock = stock

    def asociar_cancion(self, cancion):
        if any(c.id == cancion.id for c in self.canciones):
            raise ValueError("Canción ya asociada al vinilo")
        self.canciones.append(cancion)

    def consultar_disponibilidad(self):
        return self.stock > 0

    def reducir_stock(self, cantidad=1):
        if self.stock < cantidad:
            raise ValueError("ViniloSinStockError")
        self.stock -= cantidad
