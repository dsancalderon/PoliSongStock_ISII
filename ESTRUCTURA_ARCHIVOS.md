# 📂 Estructura y Descripción de Archivos - PoliSongStock

## 📄 Archivos HTML (Páginas)

### `index.html` - Página Principal
- **Descripción**: Página de inicio de PoliSongStock
- **Contenido**: 
  - Banner de bienvenida
  - Galería de artistas destacados
  - Navegación a secciones principales
  - Footer con información
- **Scripts**: carrito.js
- **Tamaño aproximado**: 8 KB

### `login.html` - Sistema de Autenticación
- **Descripción**: Página de login y registro del usuario
- **Contenido**:
  - Formulario de inicio de sesión
  - Formulario de registro (deshabilitado)
  - Dashboard de usuario administrador
  - Perfil y historial de compras
- **Scripts**: carrito.js, auth-log.js
- **Usuarios**: Solo admin@admin.com / admin
- **Tamaño aproximado**: 25 KB

### `catalogo.html` - Catálogo de MP3
- **Descripción**: Catálogo de canciones digitales
- **Contenido**:
  - Lista de 12 canciones
  - Búsqueda y filtros avanzados
  - Vista en grilla y lista
  - Información técnica (BPM, duración)
- **Scripts**: database.js, carrito.js
- **Productos**: 12 canciones
- **Tamaño aproximado**: 20 KB

### `vinilos.html` - Catálogo de Vinilos
- **Descripción**: Colección de vinilos coleccionables
- **Contenido**:
  - Lista de 8 vinilos
  - Información detallada de álbumes
  - Canciones destacadas por vinilo
  - Filtros por género y artista
- **Scripts**: database.js, carrito.js
- **Productos**: 8 vinilos
- **Tamaño aproximado**: 15 KB

### `carrito.html` - Carrito de Compras
- **Descripción**: Página principal del carrito
- **Contenido**:
  - Lista de productos agregados
  - Gestión de cantidades
  - Cálculo de totales
  - Códigos de descuento
  - Resumen de compra
- **Scripts**: database.js, carrito.js
- **Funcionalidad**: Compra y pago
- **Tamaño aproximado**: 18 KB

### `recopilaciones.html` - Recopilaciones Especiales
- **Descripción**: Compilados y colecciones especiales
- **Contenido**: A completar según necesidades
- **Tamaño aproximado**: 5 KB (en desarrollo)

### `registro.html` - Página de Registro
- **Descripción**: Formulario de registro de usuarios
- **Nota**: El registro está deshabilitado (solo admin)
- **Tamaño aproximado**: 3 KB (no funcional)

---

## 🎨 Archivos CSS

### `style.css` - Estilos Globales
- **Descripción**: Hoja de estilos principal del proyecto
- **Contiene**:
  - Estilos del header y navegación
  - Estilos generales del cuerpo
  - Clases reutilizables
  - Variables CSS (colores principales)
  - Media queries para responsividad
- **Colores principales**:
  - Primario: #6a00b8 (púrpura)
  - Secundario: #b26fff (púrpura claro)
  - Fondo: #f4f0ff (gris púrpura)
  - Texto: #2d013e (púrpura oscuro)
- **Tamaño aproximado**: 5 KB

---

## 🔧 Archivos JavaScript

### `database.js` - API de Productos
- **Descripción**: Sistema de gestión de base de datos de productos
- **Funciones principales**:
  - getAllVinilos()
  - getViniloById(id)
  - getAllMusica()
  - getMusicaById(id)
  - searchVinilos(termino)
  - searchMusica(termino)
- **Datos**: 8 vinilos + 12 canciones
- **Inicialización**: Automática al cargar
- **Tamaño aproximado**: 8 KB

### `carrito.js` - Sistema de Carrito
- **Descripción**: Gestión completa del carrito de compras
- **Funciones principales**:
  - agregar(producto, tipo)
  - eliminar(id, tipo)
  - actualizarCantidad(id, tipo, cantidad)
  - obtenerPrecioTotal()
  - obtenerImpuesto()
  - aplicarDescuento(codigo)
- **Almacenamiento**: localStorage
- **IVA**: 19%
- **Descuentos**: 5 códigos disponibles
- **Tamaño aproximado**: 10 KB

### `auth-log.js` - Sistema de Registro de Accesos
- **Descripción**: Registro de intentos de inicio de sesión
- **Funciones principales**:
  - registrarIntento(email, exitoso, razon)
  - obtenerHistorial()
  - obtenerIntentsFallidos()
  - detectarAccesoNoAutorizado(email)
- **Almacenamiento**: localStorage
- **Límite de logs**: 100 intentos
- **Protección**: Bloqueo después de 5 intentos fallidos en 24h
- **Tamaño aproximado**: 3 KB

---

## 📊 Archivos de Datos

### `database.json` - Base de Datos de Productos
- **Descripción**: Todos los productos disponibles en JSON
- **Estructura**:
  ```json
  {
    "vinilos": [...],
    "musica": [...]
  }
  ```
- **Vinilos**: 8 álbumes con canciones destacadas
- **Música**: 12 canciones con información técnica
- **Formato**: JSON válido
- **Tamaño aproximado**: 12 KB

### `usuarios.json` - Base de Datos de Usuarios
- **Descripción**: Usuarios registrados (actualmente solo admin)
- **Estructura**: Formato JSON con detalles completos
- **Contenido actual**: 
  - 1 usuario admin (admin@admin.com)
  - Historial de 3 compras
  - Datos de perfil completos
  - Preferencias de usuario
  - Información de sesiones
- **Tamaño aproximado**: 4 KB

---

## 📚 Archivos de Documentación

### `README.md` - Documentación Principal
- **Descripción**: Información general del proyecto
- **Secciones**:
  - Descripción del proyecto
  - Características principales
  - Estructura de carpetas
  - Cómo usar
  - Tecnologías
  - Base de datos
  - Seguridad
  - Próximas mejoras
- **Tamaño aproximado**: 15 KB

### `DATABASE.md` - Documentación de Productos
- **Descripción**: Detalles técnicos de la BD de productos
- **Contenido**:
  - Estructura de datos
  - API de métodos
  - Ejemplos de uso
  - Géneros y artistas
  - Rango de precios
- **Tamaño aproximado**: 10 KB

### `CARRITO.md` - Documentación del Carrito
- **Descripción**: Guía completa del sistema de carrito
- **Contenido**:
  - Archivos del sistema
  - API del carrito
  - Códigos de descuento
  - Cálculos de precios
  - Ejemplo de uso
  - Validaciones
- **Tamaño aproximado**: 12 KB

### `AUTENTICACION.md` - Documentación de Autenticación
- **Descripción**: Sistema de login y usuarios
- **Contenido**:
  - Credenciales del admin
  - Estructura de usuario
  - API de autenticación
  - Sistema de sesión
  - Características de seguridad
  - Pruebas
- **Tamaño aproximado**: 10 KB

### `GUIA_RAPIDA.md` - Guía Rápida del Usuario
- **Descripción**: Instrucciones rápidas para usar el sistema
- **Contenido**:
  - Inicio rápido en 5 minutos
  - Funciones principales
  - Códigos de descuento
  - Solución de problemas
  - Artistas y productos
- **Tamaño aproximado**: 8 KB

### `ESTRUCTURA_ARCHIVOS.md` - Este Archivo
- **Descripción**: Documentación de la estructura del proyecto
- **Contenido**: Descripción de todos los archivos
- **Tamaño aproximado**: 8 KB

---

## 📁 Carpeta de Imágenes

### `imagenes/` - Recursos Gráficos
- **Contenido**:
  - logo.png - Logo de PoliSongStock
  - fondo.png - Imagen de fondo principal
  - 2pac.png - Portada de 2Pac
  - bad.png - Portada de Bad Bunny
  - sende.png - Portada de Sende
  - yeison.png - Portada de Yeison
  - pink-floyd.png - Pink Floyd
  - beatles.png - The Beatles
  - fleetwood-mac.png - Fleetwood Mac
  - mj.png - Michael Jackson
- **Formato**: PNG (comprimido)
- **Uso**: Portadas de artistas y productos
- **Tamaño aproximado**: 2-5 MB total

---

## 🔄 Control de Versiones

### `.git/` - Historial de Git
- **Descripción**: Control de versiones del proyecto
- **Contenido**: Commits y branches del desarrollo
- **Rama actual**: main
- **Propietario**: dsancalderon

---

## 📊 Resumen de Archivos

| Tipo | Cantidad | Descripción |
|------|----------|-------------|
| **HTML** | 7 | Páginas principales |
| **CSS** | 1 | Estilos globales |
| **JavaScript** | 3 | Lógica de la aplicación |
| **JSON** | 2 | Bases de datos |
| **Markdown** | 6 | Documentación |
| **Imágenes** | 10+ | Recursos gráficos |

---

## 💾 Tamaño Total Estimado

```
Código:       ~120 KB
Imágenes:     ~2-5 MB
Documentación: ~60 KB
────────────────────
Total:        ~2-5 MB
```

---

## 🔐 Archivos Críticos (No eliminar)

- ✅ database.json (datos de productos)
- ✅ usuarios.json (datos de usuarios)
- ✅ style.css (estilos)
- ✅ carrito.js (lógica de carrito)
- ✅ database.js (API de productos)
- ✅ login.html (autenticación)

---

## 📝 Notas Importantes

1. **localStorage** es usado para:
   - Carrito de compras
   - Sesión de usuario actual
   - Historial de intentos de acceso

2. **Los archivos JSON** se cargan dinámicamente en la página

3. **El CSS** está incrustado en los HTML para mayor compatibilidad

4. **JavaScript** es esencial - debe estar habilitado en el navegador

---

## 🚀 Para Futuro Desarrollo

Considerar separar:
- CSS en archivos externos por página
- JavaScript en módulos más pequeños
- Usar un bundler (Webpack, Vite)
- Implementar un sistema de templates

---

**Última actualización**: 25 de noviembre de 2025
