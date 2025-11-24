from entidades.usuario import Usuario
from entidades.recopilacion import Recopilacion
from excepciones.errores_negocio import UsuarioNoEncontradoError

class UsuarioService:
    def __init__(self):
        self.usuarios = {}  # id -> Usuario

    def registrar_usuario(self, id: int, nombre: str, correo: str):
        if id in self.usuarios:
            raise ValueError("Usuario ya existe")
        u = Usuario(id, nombre, correo)
        self.usuarios[id] = u
        return u

    def obtener_usuario(self, id: int):
        if id not in self.usuarios:
            raise UsuarioNoEncontradoError(f"Usuario {id} no encontrado")
        return self.usuarios[id]

    def crear_recopilacion(self, usuario_id: int, recopilacion_id: int, nombre: str):
        usuario = self.obtener_usuario(usuario_id)
        r = Recopilacion(recopilacion_id, nombre, usuario_id)
        usuario.crear_recopilacion(r)
        return r
    
    def agregar_al_carrito(self, usuario_id, vinilo):
    usuario = self.buscar_usuario_por_id(usuario_id)
    if usuario is None:
        raise ValueError("Usuario no encontrado")

    usuario.carrito.append(vinilo)
    return True