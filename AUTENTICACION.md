# 🔐 Sistema de Autenticación - PoliSongStock

## Descripción General

Sistema de autenticación seguro donde solo el **Administrador** puede acceder al sistema. El registro de nuevos usuarios está deshabilitado.

## 👨‍💼 Cuenta de Administrador

### Credenciales Predefinidas

```
📧 Email:      admin@admin.com
🔑 Contraseña: admin
👤 Rol:        Administrador
```

## 🏗️ Estructura de la Base de Datos

### Almacenamiento

Los datos se almacenan en **localStorage** con la clave:
```
polisongstock_usuarios
```

### Formato de Usuario

```json
{
  "admin@admin.com": {
    "id": 1,
    "email": "admin@admin.com",
    "password": "admin",
    "nombre": "Administrador",
    "rol": "admin",
    "fechaRegistro": "2025-01-01T00:00:00.000Z",
    "compras": [
      {
        "id": 1,
        "titulo": "Thriller - Michael Jackson",
        "precio": 60000,
        "fecha": "2025-11-23",
        "estado": "Entregado"
      }
    ]
  }
}
```

### Campos de Usuario

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | number | ID único del usuario |
| `email` | string | Correo electrónico (clave primaria) |
| `password` | string | Contraseña (sin encriptar en desarrollo) |
| `nombre` | string | Nombre completo |
| `rol` | string | Rol del usuario (admin) |
| `fechaRegistro` | string | Fecha de registro (ISO 8601) |
| `compras` | array | Historial de compras |

### Estructura de Compra

```json
{
  "id": 1,
  "titulo": "Nombre del producto",
  "precio": 60000,
  "fecha": "2025-11-23",
  "estado": "Entregado"
}
```

## 🔧 API de Autenticación

### Métodos Disponibles

#### Inicializar Base de Datos

```javascript
Users.inicializar()
```

Inicializa la base de datos en localStorage con el usuario admin.

#### Buscar Usuario

```javascript
Users.buscar(email, password)
```

**Parámetros:**
- `email` (string): Correo del usuario
- `password` (string): Contraseña

**Retorna:**
- Usuario si las credenciales son correctas
- `null` si falla la autenticación

#### Obtener Usuario por Email

```javascript
Users.obtenerPorEmail(email)
```

**Parámetros:**
- `email` (string): Correo del usuario

**Retorna:**
- Objeto de usuario
- `undefined` si no existe

#### Obtener Todos los Usuarios

```javascript
Users.obtenerTodos()
```

**Retorna:**
- Array con todos los usuarios registrados

#### Registrar Nuevo Usuario

```javascript
Users.registrar(email, password, nombre)
```

**Estado:** ❌ Deshabilitado  
El registro está cerrado. Solo el admin existe.

#### Actualizar Usuario

```javascript
Users.actualizar(email, datos)
```

**Parámetros:**
- `email` (string): Correo del usuario
- `datos` (object): Datos a actualizar

**Retorna:**
- `true` si se actualiza exitosamente
- `false` si el usuario no existe

## 🔐 Sistema de Sesión

### Iniciar Sesión

```javascript
iniciarSesion()
```

Valida email y contraseña contra la base de datos:

1. Valida que el email sea formato válido
2. Valida que la contraseña tenga mínimo 6 caracteres
3. Busca el usuario en la base de datos
4. Si existe, guarda la sesión en localStorage
5. Muestra el dashboard

### Cerrar Sesión

```javascript
cerrarSesion()
```

Elimina la sesión actual y recarga la página.

### Verificar Sesión Activa

```javascript
localStorage.getItem('polisongstock_usuario_actual')
```

Si devuelve un valor, hay una sesión activa.

## 📋 Funcionalidades del Dashboard

Después de iniciar sesión, el usuario admin puede acceder a:

### 1. **Perfil de Usuario**
- 👤 Información personal
- 📧 Email (solo lectura)
- 📱 Teléfono (editable)
- 🏙️ Ciudad (editable)

### 2. **Historial de Compras**
- 🛒 Lista de compras realizadas
- 📅 Fecha de compra
- 💰 Precio pagado
- 📦 Estado del pedido

### 3. **Seguridad**
- 🔑 Cambiar contraseña
- 🔒 Activar autenticación 2FA

## 🔒 Características de Seguridad

- ✅ Validación de email
- ✅ Validación de contraseña (mínimo 6 caracteres)
- ✅ Sesión persistente en localStorage
- ✅ Protección de datos en perfil
- ✅ Confirmación antes de cerrar sesión
- ✅ Base de datos predefinida y segura

## 📱 Estados de la UI

### Login Deshabilitado
- Campo de Email
- Campo de Contraseña
- Botón "Entrar"
- Link "¿Olvidaste tu contraseña?"
- Opciones de login social (preparadas)

### Registro Deshabilitado
- Mensaje claro indicando que el registro está cerrado
- Muestra las credenciales del admin
- Indica que solo el admin puede acceder

### Dashboard (Después de Iniciar Sesión)
- Encabezado con nombre y email
- Sección de compras recientes
- Sección de perfil editable
- Sección de seguridad
- Botón para cerrar sesión

## 🧪 Pruebas

### Para Probar el Login:

1. **Abre** `login.html` en tu navegador
2. **Ingresa:**
   - Email: `admin@admin.com`
   - Contraseña: `admin`
3. **Haz clic** en "Entrar"
4. **Deberías ver** el dashboard del admin

### Para Probar la Sesión Persistente:

1. Inicia sesión como admin
2. Recarga la página (F5)
3. **Deberías ver** que la sesión se mantiene

### Para Probar el Cierre de Sesión:

1. En el dashboard, haz clic en "Cerrar Sesión"
2. Confirma la acción
3. **Deberías volver** a la pantalla de login

## 🚀 Próximas Mejoras

- 🔐 Encriptación de contraseñas (bcrypt, argon2)
- 📧 Verificación de email
- 🔑 Reset de contraseña por email
- 🔒 Autenticación 2FA funcional
- 👥 Sistema de múltiples usuarios
- 📊 Panel de administración
- 🔍 Auditoría de accesos
- 🛡️ Protección CSRF

## 📌 Notas Importantes

1. **En producción**, las contraseñas DEBEN encriptarse
2. Los datos están en localStorage (inseguro para producción)
3. Se recomienda usar un backend seguro
4. Implementar HTTPS es obligatorio
5. Validar siempre en el servidor, no solo en el cliente

## 🔗 Archivos Relacionados

- `login.html` - Página de autenticación
- `carrito.js` - Sistema de carrito (integrado)
- `DATABASE.md` - Documentación de base de datos de productos

---

**Última actualización**: 25 de noviembre de 2025
