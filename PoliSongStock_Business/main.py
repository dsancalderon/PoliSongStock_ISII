"""
Ejemplo de uso de la capa de negocio PoliSongStock MarketPlace.
Contiene un flujo simulado: registrar proveedor, registrar vinilo y canción,
registrar usuario, crear pedido y confirmar pedido por proveedor.
"""
from servicios.usuario_service import UsuarioService
from servicios.proveedor_service import ProveedorService
from servicios.cancion_service import CancionService
from servicios.vinilo_service import ViniloService
from servicios.pedido_service import PedidoService
from utilidades.notificador import enviar_correo_simulado

