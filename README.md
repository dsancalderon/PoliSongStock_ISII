# 🎵 PoliSongStock - Tienda de Música Online

## 📋 Descripción del Proyecto

PoliSongStock es una plataforma de comercio electrónico especializada en la venta de música digital (MP3) y vinilos coleccionables. El proyecto incluye un sistema completo de autenticación, catálogo de productos, carrito de compras y gestor de usuarios.

## 🎯 Características Principales

### 1. **Sistema de Autenticación** 🔐
- ✅ Login seguro con usuario admin predefinido
- ✅ Registro deshabilitado (solo admin)
- ✅ Sesión persistente en localStorage
- ✅ Historial de intentos de acceso
- ✅ Protección contra acceso no autorizado
- ✅ Dashboard personalizado para el usuario

**Credenciales Admin:**
```
Email:      admin@admin.com
Contraseña: admin
```

### 2. **Base de Datos de Productos** 📀
- 📦 8 vinilos de artistas legendarios
- 🎵 12 canciones MP3 con información técnica
- 💰 Sistema de precios en COP
- 🔍 Búsqueda y filtros avanzados
- 📊 Información completa de cada producto

### 3. **Carrito de Compras** 🛒
- ✅ Agregar/eliminar productos
- ✅ Gestión de cantidades
- ✅ Cálculo automático de IVA (19%)
- ✅ Códigos de descuento (WELCOME10, MUSICA20, etc.)
- ✅ Almacenamiento persistente
- ✅ Badge de cantidad en el header

### 4. **Catálogos** 📚
- **MP3**: Búsqueda y filtros por artista, género, álbum
- **Vinilos**: Vista detallada con tracks destacados
- **Recopilaciones**: Sección para compilados especiales

### 5. **Perfil de Usuario** 👤
- 📧 Información personal
- 🛍️ Historial de compras
- 🔒 Opciones de seguridad
- 📱 Datos de contacto

## 📁 Estructura de Carpetas

```
PoliSongStock/
├── index.html                 # Página principal
├── login.html                 # Sistema de autenticación
├── carrito.html              # Página del carrito
├── catalogo.html             # Catálogo de canciones MP3
├── vinilos.html              # Catálogo de vinilos
├── recopilaciones.html       # Recopilaciones especiales
├── registro.html             # Página de registro (opcional)
├── style.css                 # Estilos globales
├── database.js               # API de productos
├── database.json             # Base de datos de productos
├── carrito.js                # Sistema de carrito
├── auth-log.js               # Sistema de registro de accesos
├── DATABASE.md               # Documentación de BD productos
├── CARRITO.md                # Documentación de carrito
├── AUTENTICACION.md          # Documentación de auth
├── imagenes/                 # Carpeta de imágenes
│   ├── logo.png
│   ├── fondo.png
│   ├── 2pac.png
│   ├── bad.png
│   └── ...
└── .git/                     # Control de versiones
```

## 🚀 Cómo Usar

### 1. Clonar el Repositorio
```bash
git clone https://github.com/dsancalderon/PoliSongStock.git
cd PoliSongStock
```

### 2. Abrir en el Navegador
```bash
# Opción 1: Abrir directamente
open index.html

# Opción 2: Usar un servidor local (recomendado)
python -m http.server 8000
# Luego visita: http://localhost:8000
```

### 3. Iniciar Sesión
- Email: `admin@admin.com`
- Contraseña: `admin`

### 4. Explorar la Tienda
- Navega por el catálogo de MP3
- Explora los vinilos disponibles
- Agrega productos al carrito
- Aplica códigos de descuento
- Accede a tu perfil

## 🔑 Credenciales de Acceso

| Credencial | Valor |
|-----------|-------|
| **Email** | admin@admin.com |
| **Contraseña** | admin |
| **Rol** | Administrador |

## 💻 Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Almacenamiento**: localStorage (desarrollo)
- **Control de versiones**: Git
- **Navegadores soportados**: Chrome, Firefox, Safari, Edge

## 📊 Base de Datos

### Usuarios
```javascript
{
  "admin@admin.com": {
    id: 1,
    email: "admin@admin.com",
    password: "admin",
    nombre: "Administrador",
    rol: "admin",
    compras: [...]
  }
}
```

### Productos
- **8 Vinilos**: Abbey Road, Thriller, All Eyez on Me, etc.
- **12 Canciones**: California Love, Billie Jean, Dreams, etc.

### Carrito
```javascript
{
  id: 1,
  titulo: "California Love",
  artista: "2Pac ft. Dr. Dre",
  precio: 1500,
  cantidad: 2,
  tipo: "musica"
}
```

## 🎁 Códigos de Descuento Disponibles

| Código | Descuento | Descripción |
|--------|-----------|-------------|
| `WELCOME10` | 10% | Bienvenida general |
| `MUSICA20` | 20% | Especial para música |
| `VINILOS15` | 15% | Especial para vinilos |
| `BLACKFRIDAY30` | 30% | Descuento especial |
| `POLISONG5` | 5% | Descuento general |

## 🔒 Seguridad

- ✅ Validación de email y contraseña
- ✅ Protección contra acceso no autorizado
- ✅ Historial de intentos de acceso
- ✅ Bloqueo temporal después de múltiples intentos fallidos
- ⚠️ Las contraseñas se almacenan en texto plano (desarrollo)

**Nota para Producción:**
- Implementar encriptación de contraseñas (bcrypt, argon2)
- Usar un backend seguro (Node.js, Python, etc.)
- Implementar HTTPS obligatorio
- Usar base de datos real (MongoDB, PostgreSQL, etc.)
- Validar siempre en el servidor

## 📚 Documentación Completa

- **[DATABASE.md](DATABASE.md)** - Documentación de la base de datos de productos
- **[CARRITO.md](CARRITO.md)** - Documentación del sistema de carrito
- **[AUTENTICACION.md](AUTENTICACION.md)** - Documentación del sistema de autenticación

## 🐛 Soporte y Problemas

Si encuentras problemas:
1. Verifica que estés usando el email correcto: `admin@admin.com`
2. Comprueba que la contraseña sea: `admin`
3. Limpia el caché del navegador (Ctrl+Shift+Delete)
4. Abre las herramientas de desarrollador (F12) para ver errores en la consola

## 🚧 Próximas Mejoras

- 🔐 Encriptación de contraseñas
- 📧 Sistema de recuperación de contraseña
- 👥 Panel de administración avanzado
- 📊 Estadísticas de ventas
- 💳 Integración con pasarela de pago
- 📦 Sistema de seguimiento de pedidos
- 🔔 Notificaciones por email
- 🌍 Soporte multiidioma
