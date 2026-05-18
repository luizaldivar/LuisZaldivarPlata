import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'super_secret_key_cdmx' # In a real app, use a secure random key

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'multas.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db_path = app.config.get('DATABASE', DB_PATH)
        db = g._database = sqlite3.connect(db_path)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Auth Routes ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        db = get_db()
        user = db.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        
        if user and check_password_hash(user['contraseña'], password):
            session['user_id'] = user['id_usuario']
            session['user_name'] = user['nombre']
            return redirect(url_for('consulta'))
        else:
            flash('Credenciales incorrectas.', 'error')
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        db = get_db()
        try:
            db.execute(
                'INSERT INTO usuarios (nombre, email, contraseña) VALUES (?, ?, ?)',
                (nombre, email, generate_password_hash(password))
            )
            db.commit()
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El correo electrónico ya está registrado.', 'error')
            
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# --- Main Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if 'user_id' not in session:
        flash('Por favor inicia sesión para consultar.', 'error')
        return redirect(url_for('login'))

    resultado = None
    corralon = None

    if request.method == 'POST':
        busqueda = request.form.get('busqueda', '').strip().upper()
        
        db = get_db()
        # Buscar por placa o numero de infraccion
        resultado = db.execute('''
            SELECT m.*, c.nombre as corralon_nombre, c.direccion as corralon_direccion, 
                   c.latitud, c.longitud, c.area_especifica
            FROM multas m
            LEFT JOIN corralones c ON m.id_corralon = c.id_corralon
            WHERE m.placa = ? OR m.numero_infraccion = ?
        ''', (busqueda, busqueda)).fetchall()

    return render_template('consulta.html', resultados=resultado)

@app.route('/pago/<int:id_multa>', methods=['GET', 'POST'])
def pago(id_multa):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    db = get_db()
    multa = db.execute('SELECT * FROM multas WHERE id_multa = ?', (id_multa,)).fetchone()

    if not multa:
        flash('Multa no encontrada.', 'error')
        return redirect(url_for('consulta'))

    if multa['estatus'] != 'pendiente':
        flash('Esta multa ya no está pendiente de pago.', 'error')
        return redirect(url_for('consulta'))

    if request.method == 'POST':
        metodo = request.form.get('metodo')
        monto_pagar = multa['monto']
        ref = f"REF-{metodo[:3].upper()}-{str(uuid.uuid4())[:8].upper()}"
        
        try:
            # Registrar pago
            db.execute('''
                INSERT INTO pagos (id_multa, fecha_pago, monto_pagado, metodo_pago, referencia_pago)
                VALUES (?, ?, ?, ?, ?)
            ''', (id_multa, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), monto_pagar, metodo, ref))
            
            # Actualizar estatus de multa a 'pagada' (el sistema de liberación la pasará a 'liberada' luego)
            db.execute('UPDATE multas SET estatus = ? WHERE id_multa = ?', ('pagada', id_multa))
            db.commit()
            
            # Si se generó ficha de depósito (pago físico)
            if metodo == 'deposito':
                flash('Se ha generado tu ficha de depósito.', 'success')
                return render_template('ficha_deposito.html', multa=multa, referencia=ref, metodo=metodo)
            
            # Si fue en línea
            return redirect(url_for('liberacion', id_multa=id_multa))
            
        except Exception as e:
            db.rollback()
            flash('Error procesando el pago. Intenta de nuevo.', 'error')

    return render_template('pago.html', multa=multa)

@app.route('/liberacion/<int:id_multa>')
def liberacion(id_multa):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    db = get_db()
    multa = db.execute('SELECT m.*, c.nombre as corralon_nombre FROM multas m LEFT JOIN corralones c ON m.id_corralon = c.id_corralon WHERE id_multa = ?', (id_multa,)).fetchone()
    
    if not multa or multa['estatus'] == 'pendiente':
        return redirect(url_for('consulta'))
        
    # Simulamos el proceso de liberación automatizado tras confirmación de pago
    if multa['estatus'] == 'pagada':
        db.execute('UPDATE multas SET estatus = ? WHERE id_multa = ?', ('liberada', id_multa))
        db.commit()
        multa = db.execute('SELECT m.*, c.nombre as corralon_nombre FROM multas m LEFT JOIN corralones c ON m.id_corralon = c.id_corralon WHERE id_multa = ?', (id_multa,)).fetchone()

    return render_template('liberacion.html', multa=multa)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
