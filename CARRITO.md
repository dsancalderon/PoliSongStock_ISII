# 🛒 Sistema de Carrito de Compras - PoliSongStock

## Descripción General

Sistema completo de carrito de compras con almacenamiento persistente en localStorage. Permite a los usuarios agregar vinilos y canciones a su carrito, modificar cantidades, aplicar códigos de descuento y proceder al pago.

## Archivos del Sistema

### 1. **carrito.js**
Script principal que contiene toda la lógica del carrito de compras.

**Características:**
- ✅ Almacenamiento persistente en localStorage
- ✅ Agregar/eliminar productos
- ✅ Actualizar cantidades
- ✅ Cálculo automático de IVA (19%)
- ✅ Sistema de códigos de descuento
- ✅ Badge de cantidad en el header
- ✅ Notificaciones visuales

### 2. **carrito.html**
Página principal del carrito de compras con:
- 📋 Lista de productos agregados
- 💰 Resumen de precios
- 🎟️ Aplicación de códigos de descuento
- 🛒 Gestión de cantidades

## API del Carrito

### Métodos Disponibles

#### Gestión de Productos

```javascript
// Agregar producto al carrito
Carrito.agregar(producto, tipo)
// tipo: 'musica' o 'vinilo'

// Eliminar producto
Carrito.eliminar(id, tipo)

// Actualizar cantidad
Carrito.actualizarCantidad(id, tipo, cantidad)

// Vaciar carrito completamente
Carrito.vaciar()
```

#### Cálculos y Totales

```javascript
// Obtener cantidad total de items
Carrito.obtenerCantidadTotal()

// Obtener precio total (subtotal)
Carrito.obtenerPrecioTotal()

// Obtener impuesto (IVA 19%)
Carrito.obtenerImpuesto()

// Obtener total con impuesto
Carrito.obtenerTotalConImpuesto()

// Obtener total con descuento aplicado
Carrito.obtenerPrecioConDescuento(codigo)

// Obtener resumen completo
Carrito.obtenerResumen()
```

#### Códigos de Descuento

```javascript
// Verificar si código es válido y retorna descuento
Carrito.aplicarDescuento(codigo)

// Códigos disponibles:
// 'WELCOME10'    → 10% descuento
// 'MUSICA20'     → 20% descuento
// 'VINILOS15'    → 15% descuento
// 'BLACKFRIDAY30' → 30% descuento
// 'POLISONG5'    → 5% descuento
```

#### Utilidades

```javascript
// Verificar si el carrito tiene productos
Carrito.tieneProductos()

// Formatear precio en COP
Carrito.formatearPrecio(precio)

// Inicializar carrito
Carrito.init()

// Guardar en localStorage
Carrito.guardar()

// Mostrar notificación
Carrito.mostrarNotificacion(mensaje)
```

## Integración en Páginas

### En `catalogo.html` y `vinilos.html`

Para agregar un producto al carrito desde cualquier página:

```html
<!-- En el botón de compra -->
<button onclick="agregarAlCarrito(id, 'musica')">
    🛒 Comprar
</button>

<!-- Script necesario en la página -->
<script src="carrito.js"></script>
```

### En el Header (Todas las páginas)

```html
<a href="carrito.html" class="nav-link carrito-link">
    🛒 Carrito
    <span id="carrito-badge" style="display: none;">0</span>
</a>
```

El badge se actualiza automáticamente cuando se agregan/eliminan productos.

## Estructura del Producto en el Carrito

```javascript
{
  id: 1,
  titulo: "California Love",
  artista: "2Pac ft. Dr. Dre",
  album: "All Eyez on Me",
  precio: 1500,
  cantidad: 2,
  tipo: "musica",
  fechaAgregado: "2025-11-25T15:30:00.000Z"
}
```

## Almacenamiento Local

Los datos se guardan en `localStorage` con la clave: **`polisongstock_carrito`**

El carrito persiste incluso después de cerrar el navegador.

## Cálculos de Precios

### Fórmula de Cálculo

```
Subtotal = Precio1 × Cantidad1 + Precio2 × Cantidad2 + ...
IVA (19%) = Subtotal × 0.19
Total = Subtotal + IVA

Con Descuento:
Subtotal con Descuento = Subtotal × (1 - DescuentoPorcentaje)
IVA (19%) = Subtotal con Descuento × 0.19
Total Final = Subtotal con Descuento + IVA
```

### Ejemplo
```
- Canción: $1.500 × 2 = $3.000
- Vinilo: $45.000 × 1 = $45.000
- Subtotal: $48.000
- IVA (19%): $9.120
- Total: $57.120

Con código WELCOME10 (10%):
- Subtotal con Descuento: $48.000 × 0.9 = $43.200
- IVA (19%): $43.200 × 0.19 = $8.208
- Total Final: $51.408
```

## Notificaciones

El sistema muestra notificaciones automáticas cuando:
- ✅ Se agrega un producto
- ✅ Se aplica un descuento
- ✅ Se vacía el carrito
- ❌ Se intenta usar un código inválido

Las notificaciones aparecen en la esquina superior derecha y desaparecen automáticamente después de 3 segundos.

## Ejemplo de Uso Completo

```javascript
// 1. Agregar un producto
const cancion = {
  id: 1,
  titulo: "California Love",
  artista: "2Pac",
  precio: 1500
};
Carrito.agregar(cancion, 'musica');

// 2. Verificar cantidad
console.log(Carrito.obtenerCantidadTotal()); // 1

// 3. Obtener total
console.log(Carrito.obtenerPrecioTotal()); // 1500

// 4. Aplicar descuento
console.log(Carrito.aplicarDescuento('WELCOME10')); // 0.10

// 5. Obtener total con descuento
console.log(Carrito.obtenerPrecioConDescuento('WELCOME10')); // 1350
```

## Flujo de Compra

1. **Exploración**: Usuario navega por catálogo (`catalogo.html` o `vinilos.html`)
2. **Agregar al carrito**: Click en botón "Comprar" 
3. **Confirmación**: Notificación visual confirma la acción
4. **Ver carrito**: Click en enlace "🛒 Carrito" en el header
5. **Revisar pedido**: Usuario revisa productos y cantidades
6. **Aplicar descuento**: (Opcional) Ingresa código de descuento
7. **Proceder al pago**: Click en "Proceder al Pago"
8. **Redirigir a login**: Sistema redirige a página de login para completar compra

## Validaciones

- ✅ No permite cantidades negativas
- ✅ Valida códigos de descuento
- ✅ Verifica si el carrito está vacío antes de procesar compra
- ✅ Confirma antes de vaciar carrito
- ✅ Sincroniza entre pestañas del navegador

## Próximas Mejoras

- 🔄 Integración con backend real
- 💳 Pasarela de pago
- 📦 Seguimiento de pedidos
- 🎁 Sistema de cupones más avanzado
- 💝 Favoritos y listas de deseos
- 📧 Confirmación por email

## Compatibilidad

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Navegadores móviles

## Notas Técnicas

- El localStorage tiene límite de ~5-10MB
- Los datos se guardan en JSON
- Se sincroniza automáticamente entre pestañas
- El IVA se calcula sobre el valor final (después de descuento)

---

**Última actualización**: 25 de noviembre de 2025
