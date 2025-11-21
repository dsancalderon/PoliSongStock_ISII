class Cancion:
    def __init__(self, id: int, nombre: str, artista: str, precio: float, duracion: float, tamano_kb: int, calidad: str):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.precio = precio
        self.duracion = duracion
        self.tamano_kb = tamano_kb
        self.calidad = calidad

    def mostrar_detalle(self):
        return f"{self.nombre} - {self.artista} ({self.duracion} min) - ${self.precio:.2f}"
