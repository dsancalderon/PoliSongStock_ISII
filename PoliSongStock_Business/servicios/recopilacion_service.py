from excepciones.errores_negocio import RecopilacionNoPublicaError

class RecopilacionService:
    def __init__(self, usuario_service):
        self.usuario_service = usuario_service

    def clonar_recopilacion(self, usuario_id:int, origen_usuario_id:int, recopilacion_id:int, nuevo_id:int):
        origen = self.usuario_service.obtener_usuario(origen_usuario_id)
        recopilacion = next((r for r in origen.recopilaciones if r.id==recopilacion_id), None)
        if not recopilacion:
            raise ValueError("Recopilacion origen no encontrada")
        if not recopilacion.publica:
            raise RecopilacionNoPublicaError("Solo se pueden clonar recopilaciones públicas")
        usuario = self.usuario_service.obtener_usuario(usuario_id)
        nueva = type(recopilacion)(nuevo_id, recopilacion.nombre + " (copia)", usuario_id)
        # copiar canciones (shallow copy)
        for c in recopilacion.canciones:
            nueva.canciones.append(c)
        usuario.crear_recopilacion(nueva)
        return nueva
