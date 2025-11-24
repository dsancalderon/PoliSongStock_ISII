from typing import Dict, Optional
from entidades.usuario import Usuario

class UsuarioService:
    def __init__(self):
        # almacena usuarios por id
        self.usuarios: Dict[int, Usuario] = {}

    def registrar_usuario(self, id: int, nombre: str, correo: str, password: str) -> Usuario:
        if id in self.usuarios:
            raise ValueError(f"Usuario con id {id} ya existe")
        usuario = Usuario(id, nombre, correo, password)
        self.usuarios[id] = usuario
        return usuario

    def obtener_usuario(self, id: int) -> Optional[Usuario]:
        return self.usuarios.get(id)

    def autenticar(self, correo: str, password: str) -> Optional[Usuario]:
        # sencillo: buscar por correo
        for u in self.usuarios.values():
            if u.correo == correo and u.password == password:
                return u
        return None

    def agregar_al_carrito(self, usuario_id: int, item) -> bool:
        usuario = self.obtener_usuario(usuario_id)
        if usuario is None:
            raise ValueError("Usuario no encontrado")
        usuario.carrito.append(item)
        return True

    def vaciar_carrito(self, usuario_id: int) -> None:
        usuario = self.obtener_usuario(usuario_id)
        if usuario is None:
            raise ValueError("Usuario no encontrado")
        usuario.carrito.clear()

