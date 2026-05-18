import sqlite3
import os
from werkzeug.security import generate_password_hash

# Rutas absolutas para evitar problemas al ejecutar desde otros directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'multas.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

def init_db():
    print(f"Inicializando base de datos en: {DB_PATH}")
    
    # Conectar (creará el archivo si no existe)
    connection = sqlite3.connect(DB_PATH)
    
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        connection.executescript(f.read())
        
    cursor = connection.cursor()
    
    # Agregar usuario por defecto
    hashed_password = generate_password_hash('admin123')
    cursor.execute(
        "INSERT INTO usuarios (email, contraseña, nombre) VALUES (?, ?, ?)",
        ('admin@cdmx.gob.mx', hashed_password, 'Administrador CDMX')
    )
    
    # Usuario normal para pruebas
    user_password = generate_password_hash('ciudadano123')
    cursor.execute(
        "INSERT INTO usuarios (email, contraseña, nombre) VALUES (?, ?, ?)",
        ('ciudadano@email.com', user_password, 'Juan Pérez')
    )

    connection.commit()
    connection.close()
    
    print("Base de datos inicializada correctamente con datos de prueba.")

if __name__ == '__main__':
    init_db()
