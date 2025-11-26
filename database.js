// Objeto para gestionar la base de datos
const Database = {
  vinilos: [],
  musica: [],

  // Cargar datos desde JSON
  async init() {
    try {
      const response = await fetch('database.json');
      const data = await response.json();
      this.vinilos = data.vinilos;
      this.musica = data.musica;
      console.log('Base de datos cargada correctamente');
      return true;
    } catch (error) {
      console.error('Error cargando la base de datos:', error);
      return false;
    }
  },

  // Obtener todos los vinilos
  getAllVinilos() {
    return this.vinilos;
  },

  // Obtener vinilo por ID
  getViniloById(id) {
    return this.vinilos.find(v => v.id === parseInt(id));
  },

  // Obtener vinilos por artista
  getVinilosByArtista(artista) {
    return this.vinilos.filter(v => v.artista.toLowerCase().includes(artista.toLowerCase()));
  },

  // Obtener vinilos por género
  getVinilosByGenero(genero) {
    return this.vinilos.filter(v => v.genero.toLowerCase().includes(genero.toLowerCase()));
  },

  // Obtener todas las canciones
  getAllMusica() {
    return this.musica;
  },

  // Obtener canción por ID
  getMusicaById(id) {
    return this.musica.find(m => m.id === parseInt(id));
  },

  // Obtener canciones por artista
  getMusicaByArtista(artista) {
    return this.musica.filter(m => m.artista.toLowerCase().includes(artista.toLowerCase()));
  },

  // Obtener canciones por género
  getMusicaByGenero(genero) {
    return this.musica.filter(m => m.genero.toLowerCase().includes(genero.toLowerCase()));
  },

  // Obtener canciones por álbum
  getMusicaByAlbum(album) {
    return this.musica.filter(m => m.album.toLowerCase().includes(album.toLowerCase()));
  },

  // Buscar vinilos por título
  searchVinilos(termino) {
    return this.vinilos.filter(v => 
      v.titulo.toLowerCase().includes(termino.toLowerCase()) ||
      v.artista.toLowerCase().includes(termino.toLowerCase())
    );
  },

  // Buscar canciones por título
  searchMusica(termino) {
    return this.musica.filter(m =>
      m.titulo.toLowerCase().includes(termino.toLowerCase()) ||
      m.artista.toLowerCase().includes(termino.toLowerCase()) ||
      m.album.toLowerCase().includes(termino.toLowerCase())
    );
  },

  // Obtener géneros únicos de vinilos
  getViniloGeneros() {
    return [...new Set(this.vinilos.map(v => v.genero))];
  },

  // Obtener géneros únicos de música
  getMusicaGeneros() {
    return [...new Set(this.musica.map(m => m.genero))];
  },

  // Obtener artistas únicos de vinilos
  getViniloArtistas() {
    return [...new Set(this.vinilos.map(v => v.artista))];
  },

  // Obtener artistas únicos de música
  getMusicaArtistas() {
    return [...new Set(this.musica.map(m => m.artista))];
  },

  // Filtrar vinilos por rango de precio
  getVinilosByPriceRange(minPrice, maxPrice) {
    return this.vinilos.filter(v => v.precio >= minPrice && v.precio <= maxPrice);
  },

  // Obtener vinilos más recientes
  getVinilosRecientes(cantidad = 5) {
    return [...this.vinilos].sort((a, b) => b.año - a.año).slice(0, cantidad);
  },

  // Obtener canciones más populares (por precio/demanda)
  getMusicaPopular(cantidad = 10) {
    return this.musica.slice(0, cantidad);
  }
};

// Inicializar base de datos cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
  Database.init();
});
