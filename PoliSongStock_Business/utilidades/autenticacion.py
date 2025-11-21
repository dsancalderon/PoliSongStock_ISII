# Simulación simple de sesión
class AuthSession:
    def __init__(self):
        self.usuario_activo = None
        self.proveedor_activo = None

    def login_usuario(self, usuario_id:int):
        self.usuario_activo = usuario_id

    def logout_usuario(self):
        self.usuario_activo = None

    def login_proveedor(self, proveedor_id:int):
        self.proveedor_activo = proveedor_id

    def logout_proveedor(self):
        self.proveedor_activo = None
