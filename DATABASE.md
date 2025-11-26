# 📀 Base de Datos PoliSongStock

## Descripción
Sistema completo de base de datos para la plataforma PoliSongStock con información de vinilos y música digital en formato JSON.

## Estructura de la Base de Datos

### 📁 Archivos

#### `database.json`
Archivo JSON que contiene toda la información de vinilos y canciones disponibles.

**Secciones:**
- **vinilos**: Array con 8 vinilos de diferentes géneros
- **musica**: Array con 12 canciones de diversos artistas

#### `database.js`
Script JavaScript que proporciona una API para acceder a los datos de forma fácil y eficiente.

## Estructura de Datos

### Vinilo
```json
{
  "id": 1,
  "titulo": "All Eyez on Me",
  "artista": "2Pac",
  "año": 1996,
  "genero": "Hip Hop",
  "precio": 45000,
  "imagen": "imagenes/2pac.png",
  "descripcion": "Descripción del álbum...",
  "canciones": ["California Love", "All Eyez on Me", "Hit 'Em Up"]
}
```

### Canción
```json
{
  "id": 1,
  "titulo": "California Love",
  "artista": "2Pac ft. Dr. Dre",
  "album": "All Eyez on Me",
  "año": 1995,
  "genero": "Hip Hop",
  "duracion": "4:42",
  "precio": 1500,
  "bpm": 88
}
```

## API de Base de Datos

### Métodos Disponibles

#### Inicialización
```javascript
// Inicializa la base de datos (se ejecuta automáticamente)
await Database.init()
```

#### Vinilos
```javascript
// Obtener todos los vinilos
Database.getAllVinilos()

// Obtener vinilo por ID
Database.getViniloById(id)

// Obtener vinilos por artista
Database.getVinilosByArtista("2Pac")

// Obtener vinilos por género
Database.getVinilosByGenero("Hip Hop")

// Buscar vinilos
Database.searchVinilos("Dark Side")

// Obtener géneros únicos
Database.getViniloGeneros()

// Obtener artistas únicos
Database.getViniloArtistas()

// Filtrar por rango de precio
Database.getVinilosByPriceRange(30000, 60000)

// Obtener vinilos recientes
Database.getVinilosRecientes(5)
```

#### Música
```javascript
// Obtener todas las canciones
Database.getAllMusica()

// Obtener canción por ID
Database.getMusicaById(id)

// Obtener canciones por artista
Database.getMusicaByArtista("Michael Jackson")

// Obtener canciones por género
Database.getMusicaByGenero("Pop")

// Obtener canciones por álbum
Database.getMusicaByAlbum("Thriller")

// Buscar canciones
Database.searchMusica("Billie")

// Obtener géneros únicos
Database.getMusicaGeneros()

// Obtener artistas únicos
Database.getMusicaArtistas()

// Obtener canciones populares
Database.getMusicaPopular(10)
```

## Artistas en la Base de Datos

### Hip Hop & Reggaeton
- **2Pac** - Leyenda del hip hop de los 90s
- **Bad Bunny** - Reggaeton y trap latino moderno
- **Sende** - Reggaeton/Trap latino contemporáneo
- **Yeison** - Reggaeton melódico

### Rock & Pop
- **The Beatles** - Leyenda del rock clásico
- **Pink Floyd** - Rock progresivo experimental
- **Fleetwood Mac** - Rock/Pop de los 70s
- **Michael Jackson** - Rey del pop

## Géneros Incluidos

- Hip Hop
- Reggaeton
- Trap Latino
- Rock Progresivo
- Rock
- Pop
- Funk
- Regional Mexicano

## Rango de Precios

- **Canciones**: COP $1.200 - COP $2.000
- **Vinilos**: COP $35.000 - COP $70.000

## Páginas que Usan la Base de Datos

### 📀 vinilos.html
- Mostrador de vinilos en grilla
- Filtros por género, artista y búsqueda
- Información completa de cada vinilo
- Precios y botón de compra

### 🎧 catalogo.html
- Catálogo de canciones MP3
- Vista en grilla y lista
- Filtros avanzados
- Información técnica (BPM, duración)
- Búsqueda en tiempo real

## Características

✅ Base de datos en formato JSON (sin dependencias externas)
✅ API JavaScript simple y clara
✅ Búsqueda y filtros en tiempo real
✅ Información completa de artistas y canciones
✅ Compatible con navegadores modernos
✅ Integración lista en las páginas HTML
✅ Formateo automático de precios en COP

## Próximas Mejoras

- Agregar más artistas y canciones
- Implementar ratings/reseñas
- Sistema de favoritos
- Carrito de compras persistente
- Integración con backend para persistencia de datos

## Notas Importantes

- La base de datos se carga automáticamente cuando se abre una página que usa `database.js`
- Los datos se cargan en memoria del navegador
- Para producción, considera usar una base de datos real (MongoDB, PostgreSQL, etc.)
- El archivo `database.json` debe estar en la misma carpeta que las páginas HTML

---

**Última actualización**: 25 de noviembre de 2025
