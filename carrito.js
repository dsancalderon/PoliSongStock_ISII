// Sistema de carrito de compras con almacenamiento local
const Carrito = {
  items: [],
  
  // Inicializar carrito desde localStorage
  init() {
    const stored = localStorage.getItem('polisongstock_carrito');
    if (stored) {
      try {
        this.items = JSON.parse(stored);
      } catch (e) {
        this.items = [];
      }
    }
    this.actualizarUI();
  },

  // Agregar producto al carrito
  agregar(producto, tipo = 'musica') {
    // Verificar si el producto ya existe en el carrito
    const existe = this.items.find(item => 
      item.id === producto.id && item.tipo === tipo
    );

    if (existe) {
      // Si existe, aumentar cantidad
      existe.cantidad += 1;
    } else {
      // Si no existe, agregarlo
      this.items.push({
        ...producto,
        tipo: tipo,
        cantidad: 1,
        fechaAgregado: new Date().toISOString()
      });
    }

    this.guardar();
    this.actualizarUI();
    this.mostrarNotificacion(`"${producto.titulo}" agregado al carrito`);
  },

  // Eliminar producto del carrito
  eliminar(id, tipo) {
    this.items = this.items.filter(item => 
      !(item.id === id && item.tipo === tipo)
    );
    this.guardar();
    this.actualizarUI();
  },

  // Actualizar cantidad de un producto
  actualizarCantidad(id, tipo, cantidad) {
    const item = this.items.find(item => 
      item.id === id && item.tipo === tipo
    );
    
    if (item) {
      if (cantidad <= 0) {
        this.eliminar(id, tipo);
      } else {
        item.cantidad = cantidad;
        this.guardar();
        this.actualizarUI();
      }
    }
  },

  // Vaciar carrito
  vaciar() {
    if (confirm('¿Está seguro de que desea vaciar el carrito?')) {
      this.items = [];
      this.guardar();
      this.actualizarUI();
      this.mostrarNotificacion('Carrito vaciado');
    }
  },

  // Obtener cantidad total de items
  obtenerCantidadTotal() {
    return this.items.reduce((total, item) => total + item.cantidad, 0);
  },

  // Obtener precio total
  obtenerPrecioTotal() {
    return this.items.reduce((total, item) => 
      total + (item.precio * item.cantidad), 0
    );
  },

  // Obtener subtotal sin descuentos
  obtenerSubtotal() {
    return this.obtenerPrecioTotal();
  },

  // Calcular impuesto (IVA 19%)
  obtenerImpuesto() {
    return Math.round(this.obtenerPrecioTotal() * 0.19);
  },

  // Obtener total con impuesto
  obtenerTotalConImpuesto() {
    return this.obtenerPrecioTotal() + this.obtenerImpuesto();
  },

  // Aplicar código de descuento
  aplicarDescuento(codigo) {
    const descuentos = {
      'WELCOME10': 0.10,      // 10% descuento
      'MUSICA20': 0.20,       // 20% para música
      'VINILOS15': 0.15,      // 15% para vinilos
      'BLACKFRIDAY30': 0.30,  // 30% descuento especial
      'POLISONG5': 0.05       // 5% descuento general
    };

    return descuentos[codigo.toUpperCase()] || 0;
  },

  // Calcular descuento en precio
  obtenerPrecioConDescuento(codigoDescuento = '') {
    const descuento = this.aplicarDescuento(codigoDescuento);
    const subtotal = this.obtenerPrecioTotal();
    return Math.round(subtotal * (1 - descuento));
  },

  // Guardar en localStorage
  guardar() {
    localStorage.setItem('polisongstock_carrito', JSON.stringify(this.items));
  },

  // Actualizar elementos de la UI
  actualizarUI() {
    const badge = document.getElementById('carrito-badge');
    const cantidad = this.obtenerCantidadTotal();

    if (badge) {
      if (cantidad > 0) {
        badge.textContent = cantidad;
        badge.style.display = 'flex';
      } else {
        badge.style.display = 'none';
      }
    }
  },

  // Mostrar notificación
  mostrarNotificacion(mensaje) {
    // Crear elemento de notificación si no existe
    let notificacion = document.getElementById('notificacion-carrito');
    if (!notificacion) {
      notificacion = document.createElement('div');
      notificacion.id = 'notificacion-carrito';
      notificacion.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background: #4caf50;
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 1000;
        animation: slideIn 0.3s ease;
      `;
      document.body.appendChild(notificacion);

      // Agregar animación
      const style = document.createElement('style');
      style.textContent = `
        @keyframes slideIn {
          from {
            transform: translateX(400px);
            opacity: 0;
          }
          to {
            transform: translateX(0);
            opacity: 1;
          }
        }
        @keyframes slideOut {
          from {
            transform: translateX(0);
            opacity: 1;
          }
          to {
            transform: translateX(400px);
            opacity: 0;
          }
        }
      `;
      document.head.appendChild(style);
    }

    notificacion.textContent = mensaje;
    notificacion.style.animation = 'slideIn 0.3s ease';
    notificacion.style.display = 'block';

    setTimeout(() => {
      notificacion.style.animation = 'slideOut 0.3s ease';
      setTimeout(() => {
        notificacion.style.display = 'none';
      }, 300);
    }, 3000);
  },

  // Obtener resumen del carrito
  obtenerResumen() {
    return {
      cantidadItems: this.items.length,
      cantidadProductos: this.obtenerCantidadTotal(),
      subtotal: this.obtenerPrecioTotal(),
      impuesto: this.obtenerImpuesto(),
      total: this.obtenerTotalConImpuesto(),
      items: this.items
    };
  },

  // Validar si el carrito tiene productos
  tieneProductos() {
    return this.items.length > 0;
  },

  // Obtener detalles formateados para mostrar
  obtenerDetallesFormateados() {
    return this.items.map(item => ({
      ...item,
      precioFormato: this.formatearPrecio(item.precio),
      subtotalFormato: this.formatearPrecio(item.precio * item.cantidad)
    }));
  },

  // Formatear precio en pesos colombianos
  formatearPrecio(precio) {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0
    }).format(precio);
  },

  // Procesar compra (para uso futuro con backend)
  procesarCompra(datosEntrega) {
    if (!this.tieneProductos()) {
      alert('El carrito está vacío');
      return false;
    }

    const resumen = this.obtenerResumen();
    
    // Aquí se integraría con un backend real
    const pedido = {
      id: 'PED-' + Date.now(),
      fecha: new Date().toISOString(),
      cliente: datosEntrega,
      items: resumen.items,
      subtotal: resumen.subtotal,
      impuesto: resumen.impuesto,
      total: resumen.total,
      estado: 'pendiente'
    };

    return pedido;
  }
};

// Inicializar carrito cuando el DOM está listo
document.addEventListener('DOMContentLoaded', () => {
  Carrito.init();
});

// Agregar estilos globales para el carrito
const carritoStyles = document.createElement('style');
carritoStyles.textContent = `
  #carrito-badge {
    position: absolute;
    top: -8px;
    right: -8px;
    background: #ff4444;
    color: white;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: none;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.8em;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }

  .carrito-link {
    position: relative;
    display: inline-block;
  }

  .notificacion-agregar {
    animation: slideIn 0.3s ease;
  }
`;
document.head.appendChild(carritoStyles);
