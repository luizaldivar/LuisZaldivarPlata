# pyrefly: ignore [missing-import]
import pytest
import os
import tempfile
import sqlite3
from app import app, get_db

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    # Inicializar DB en memoria o temp file para pruebas
    with app.app_context():
        db = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
        
        # Leemos el esquema
        schema_path = os.path.join(os.path.dirname(__file__), '../database/schema.sql')
        with open(schema_path, 'r', encoding='utf-8') as f:
            db.executescript(f.read())
        db.close()
            
    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index(client):
    """Prueba que el index cargue correctamente."""
    rv = client.get('/')
    assert b'Gestor de Multas CDMX' in rv.data

def test_login_page(client):
    """Prueba que la página de login cargue."""
    rv = client.get('/login')
    assert b'Iniciar Sesi' in rv.data

def test_redirect_consulta_sin_login(client):
    """Prueba que se redireccione si no hay sesión."""
    rv = client.get('/consulta', follow_redirects=True)
    assert b'Por favor inicia sesi' in rv.data
