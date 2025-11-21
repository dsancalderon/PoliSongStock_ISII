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

def demo():
    # Inicializar servicios
    usuario_svc = UsuarioService()
    proveedor_svc = ProveedorService()
    cancion_svc = CancionService()
    vinilo_svc = ViniloService()
    pedido_svc = PedidoService(vinilo_svc, cancion_svc, proveedor_svc)

    # Registrar proveedor y autenticar
    prov = proveedor_svc.registrar_proveedor(1, "Vinilos S.A.", "ventas@vinilossa.com")
    proveedor_svc.autenticar(prov.id)

    # Registrar vinilo
    v = vinilo_svc.registrar_vinilo(101, "Greatest Hits", "La Banda", 1985, 45.0, 3)

    # Registrar canciones y asociarlas
    c1 = cancion_svc.registrar_cancion(201, "Cancion A", "La Banda", 1.99, 3.5, 3500, "320kbps")
    c2 = cancion_svc.registrar_cancion(202, "Cancion B", "La Banda", 1.49, 4.0, 4200, "320kbps")
    vinilo_svc.asociar_cancion(v.id, c1)
    vinilo_svc.asociar_cancion(v.id, c2)

    # Registrar usuario y crear recopilacion
    u = usuario_svc.registrar_usuario(11, "Juan", "juan@example.com")
    rec = usuario_svc.crear_recopilacion(11, 301, "Mi mejor playlist")
    rec.agregar_cancion(c1)
    rec.hacer_publica()

    # Crear pedido (vinilo x1 + canción individual)
    items = [
        {"tipo":"vinilo", "id": v.id, "cantidad": 1},
        {"tipo":"cancion", "id": c2.id, "cantidad": 1}
    ]
    pedido = pedido_svc.crear_pedido(401, u.id, items, medio_pago="tarjeta", observacion="Por favor enviar rápido")
    print("Pedido creado:", pedido.id, pedido.estado)

    # Calcular total
    total = pedido_svc.calcular_total(pedido.id)
    print(f"Total del pedido {pedido.id}: ${total:.2f}")

    # Confirmar pedido por proveedor autenticado
    pedido_confirmado = pedido_svc.confirmar_pedido(pedido.id, prov.id)
    print("Pedido confirmado. Nuevo estado:", pedido_confirmado.estado)
    print("Stock restante del vinilo:", vinilo_svc.vinilos[v.id].stock)

    # Simular notificación
    enviar_correo_simulado(u.correo, f"Su pedido {pedido.id} fue confirmado", "Gracias por su compra.")

if __name__ == '__main__':
    demo()
