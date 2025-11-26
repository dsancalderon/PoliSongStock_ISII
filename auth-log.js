// Sistema de autenticación y registro de sesiones para PoliSongStock
// Este archivo documenta todas las operaciones de autenticación

const AUTH_LOG = {
    // Registrar intento de inicio de sesión
    registrarIntento(email, exitoso, razon = '') {
        const log = {
            timestamp: new Date().toISOString(),
            email: email,
            exitoso: exitoso,
            razon: razon,
            userAgent: navigator.userAgent,
            ip: 'localhost' // En producción, obtenido del servidor
        };

        let logs = JSON.parse(localStorage.getItem('polisongstock_auth_logs') || '[]');
        logs.push(log);
        
        // Mantener solo los últimos 100 logs
        if (logs.length > 100) {
            logs = logs.slice(-100);
        }
        
        localStorage.setItem('polisongstock_auth_logs', JSON.stringify(logs));
    },

    // Obtener historial de accesos
    obtenerHistorial() {
        return JSON.parse(localStorage.getItem('polisongstock_auth_logs') || '[]');
    },

    // Obtener intentos fallidos
    obtenerIntentsFallidos() {
        const logs = this.obtenerHistorial();
        return logs.filter(log => !log.exitoso);
    },

    // Detectar acceso no autorizado
    detectarAccesoNoAutorizado(email) {
        const logs = this.obtenerHistorial();
        const hoy = new Date();
        const hace24h = new Date(hoy.getTime() - 24 * 60 * 60 * 1000);
        
        const intentosFallidos = logs.filter(log => 
            log.email === email && 
            !log.exitoso && 
            new Date(log.timestamp) > hace24h
        );

        return intentosFallidos.length > 5; // Más de 5 intentos fallidos en 24h
    },

    // Limpiar historial
    limpiarHistorial() {
        localStorage.removeItem('polisongstock_auth_logs');
    }
};

// Exportar para uso en otros scripts (si es necesario)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AUTH_LOG;
}
