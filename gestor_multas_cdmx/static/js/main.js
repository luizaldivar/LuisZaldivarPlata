document.addEventListener('DOMContentLoaded', () => {
    // Inicializar mapa si el contenedor existe
    const mapContainer = document.getElementById('map');
    
    if (mapContainer) {
        const lat = parseFloat(mapContainer.dataset.lat);
        const lng = parseFloat(mapContainer.dataset.lng);
        const title = mapContainer.dataset.title;

        // Validar coordenadas
        if (!isNaN(lat) && !isNaN(lng)) {
            // Inicializar Leaflet map
            const map = L.map('map').setView([lat, lng], 16);

            // Agregar capa de OpenStreetMap
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            // Icono personalizado para CDMX (opcional, usando el por defecto por ahora)
            // Agregar marcador
            const marker = L.marker([lat, lng]).addTo(map);
            marker.bindPopup(`<b>${title}</b><br>Ubicación exacta del vehículo.`).openPopup();
            
            // Efecto de pulse en el marcador (CSS)
            const icon = marker._icon;
            if(icon) {
                icon.style.filter = "hue-rotate(150deg)"; // Cambiar color a rojo
            }
        } else {
            mapContainer.innerHTML = '<p class="text-center p-2">Coordenadas de mapa no válidas.</p>';
        }
    }
});
