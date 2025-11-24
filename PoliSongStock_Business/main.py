"""
Ejemplo de uso de la capa de negocio PoliSongStock MarketPlace.
Contiene un flujo simulado: registrar proveedor, registrar vinilo y canción,
registrar usuario, crear pedido y confirmar pedido por proveedor.
"""
from servicios.usuario_service import UsuarioService
from servicios.vinilo_service import ViniloService
from servicios.pedido_service import PedidoService
from servicios.proveedor_service import ProveedorService

def demo():
    usuario_svc = UsuarioService()
    vinilo_svc = ViniloService()
    pedido_svc = PedidoService(usuario_svc, vinilo_svc)
    proveedor_svc = ProveedorService(pedido_service=pedido_svc)

    # crear proveedor
    prov = proveedor_svc.registrar_proveedor(1, "Vinilos S.A.", "ventas@vinilos.com")
    print("Proveedor creado:", prov.nombre)

    # registrar vinilos
    v1 = vinilo_svc.registrar_vinilo(id=1, titulo="Album A", artista="Artista X", precio=25.0, proveedor_id=prov.id, stock=10)
    v2 = vinilo_svc.registrar_vinilo(id=2, titulo="Album B", artista="Artista Y", precio=30.0, proveedor_id=prov.id, stock=5)
    print("Vinilos registrados:", v1.titulo, v2.titulo)

    # registrar usuario
    u = usuario_svc.registrar_usuario(id=1, nombre="Cliente 1", correo="c1@example.com", password="1234")
    print("Usuario creado:", u.nombre)

    # autenticar
    user = usuario_svc.autenticar("c1@example.com", "1234")
    print("Autenticado:", user.nombre if user else "no")

    # buscar vinilos
    encontrados = vinilo_svc.buscar_vinilos("Album")
    print("Encontrados:", [v.titulo for v in encontrados])

    # agregar al carrito
    usuario_svc.agregar_al_carrito(user.id, v1)
    usuario_svc.agregar_al_carrito(user.id, v2)
    print("Carrito:", [getattr(x, 'titulo', str(x)) for x in user.carrito])

    # crear pedido desde carrito
    pedido = pedido_svc.crear_pedido_desde_carrito(usuario_id=user.id, medio_pago="tarjeta", observacion="Entregar en puerta")
    print("Pedido creado id:", pedido.id, "Items:", pedido.items, "Proveedor asociado:", pedido.proveedor_id)

    # historial usuario
    historial = pedido_svc.obtener_historial_usuario(user.id)
    print("Historial (IDs):", [p.id for p in historial])

    # proveedor consulta pedidos
    pedidos_prov = proveedor_svc.consultar_pedidos(prov.id)
    print("Pedidos para proveedor:", [p.id for p in pedidos_prov])

if __name__ == "__main__":
    demo()


