# Gestor de Pagos de Multas CDMX

Sistema web en Python (Flask) para consulta, pago y liberación de multas vehiculares en la CDMX.

## Requisitos Previos

- Python 3.8+
- Git

## Instalación y Ejecución Local

1. **Clonar / Entrar al directorio del proyecto**
   ```bash
   cd gestor_multas_cdmx
   ```

2. **Crear entorno virtual (Opcional pero recomendado)**
   ```bash
   python -m venv venv
   # Activar en Windows:
   venv\Scripts\activate
   # Activar en Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicializar la base de datos (SQLite)**
   ```bash
   python database/init_db.py
   ```
   *Esto creará `multas.db` con datos iniciales de prueba (multas, corralones, etc).*

5. **Ejecutar la aplicación Flask**
   ```bash
   python app.py
   ```
   *La aplicación estará disponible en `http://127.0.0.1:5000/`*

## Uso del Sistema (Demo)

1. Ingresa a `http://127.0.0.1:5000/`.
2. **Iniciar Sesión**:
   - Correo: `admin@cdmx.gob.mx` / `ciudadano@email.com`
   - Contraseña: `admin123` / `ciudadano123`
   *(O puedes registrarte como un usuario nuevo).*
3. **Buscar Multas**: 
   - Placas de prueba: `ABC-123-A` (Pendiente, Corralón Sur), `XYZ-987-B` (Pagada), `JKL-456-C` (Liberada).
   - Infracciones de prueba: `INF-2023-001`, `INF-2023-004`.
4. **Pago**:
   - En multas "pendientes" aparecerá el botón "Pagar Ahora".
   - Puedes simular pago en línea o pago con ficha de depósito.
5. **Liberación**:
   - Al finalizar el pago, el sistema indicará el estatus de "Liberada" y mostrará las instrucciones del corralón asignado en un mapa interactivo (Leaflet).

## Estructura
- `app.py`: Backend en Flask.
- `database/`: Scripts de SQLite (`schema.sql` y `init_db.py`).
- `templates/`: Archivos HTML.
- `static/css/style.css`: Estilos Vanilla CSS con diseño Glassmorphism.
- `static/js/main.js`: Integración de mapas Leaflet.
- `tests/`: Pruebas unitarias básicas con Pytest.
