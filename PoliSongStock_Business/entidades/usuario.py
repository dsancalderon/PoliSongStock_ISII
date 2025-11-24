class Usuario:
    def __init__(self, id: int, nombre: str, correo: str, password: str):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.password = password

        # PB-05 – Carrito de compra (lista de items; aquí guardamos objetos vinilo o referencias)
        self.carrito = []

        # Ya tenías estos atributos:
        self.compras = []          # lista de IDs de pedidos realizados
        self.recopilaciones = []   # lista de objetos Recopilacion

    def crear_recopilacion(self, recopilacion):
        self.recopilaciones.append(recopilacion)

    def publicar_recopilacion(self, recopilacion_id):
        for r in self.recopilaciones:
            if getattr(r, "id", None) == recopilacion_id:
                # Asumo que Recopilacion tiene método hacer_publica()
                if hasattr(r, "hacer_publica"):
                    r.hacer_publica()
                return r
        raise ValueError("Recopilación no encontrada")

