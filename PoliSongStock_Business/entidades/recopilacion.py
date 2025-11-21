class Recopilacion:
    def __init__(self, id: int, nombre: str, usuario_id: int):
        self.id = id
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.canciones = []
        self.publica = False

    def agregar_cancion(self, cancion):
        if any(c.id == cancion.id for c in self.canciones):
            raise ValueError("CancionDuplicadaError")
        self.canciones.append(cancion)

    def eliminar_cancion(self, cancion_id):
        self.canciones = [c for c in self.canciones if c.id != cancion_id]

    def hacer_publica(self):
        self.publica = True
