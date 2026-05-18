DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS pagos;
DROP TABLE IF EXISTS multas;
DROP TABLE IF EXISTS corralones;

CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL,
    nombre TEXT NOT NULL
);

CREATE TABLE corralones (
    id_corralon INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL,
    area_especifica TEXT
);

CREATE TABLE multas (
    id_multa INTEGER PRIMARY KEY AUTOINCREMENT,
    placa TEXT NOT NULL,
    numero_infraccion TEXT UNIQUE NOT NULL,
    fecha_infraccion TEXT NOT NULL,
    monto REAL NOT NULL,
    estatus TEXT NOT NULL CHECK(estatus IN ('pendiente', 'pagada', 'liberada')),
    id_corralon INTEGER,
    FOREIGN KEY (id_corralon) REFERENCES corralones (id_corralon)
);

CREATE TABLE pagos (
    id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
    id_multa INTEGER NOT NULL,
    fecha_pago TEXT NOT NULL,
    monto_pagado REAL NOT NULL,
    metodo_pago TEXT NOT NULL CHECK(metodo_pago IN ('transferencia', 'deposito', 'tarjeta')),
    referencia_pago TEXT UNIQUE NOT NULL,
    FOREIGN KEY (id_multa) REFERENCES multas (id_multa)
);

-- Datos de Ejemplo para Corralones (CDMX)
INSERT INTO corralones (nombre, direccion, latitud, longitud, area_especifica) VALUES 
('Corralón Centro', 'Calle de las Vizcaínas, Centro, CDMX', 19.4294, -99.1415, 'Área A, Sección 1'),
('Corralón Sur', 'Avenida del Imán, Coyoacán, CDMX', 19.3083, -99.1764, 'Área B, Sección 12'),
('Corralón Norte', 'Eje 5 Norte, Gustavo A. Madero, CDMX', 19.4820, -99.1030, 'Área C, Sección 3');

-- Datos de Ejemplo para Usuarios (la contraseña hasheada la agregaremos desde Python, dejaremos esto comentado)
-- INSERT INTO usuarios (email, contraseña, nombre) VALUES ('admin@cdmx.gob.mx', 'hash_here', 'Administrador CDMX');

-- Datos de Ejemplo para Multas
INSERT INTO multas (placa, numero_infraccion, fecha_infraccion, monto, estatus, id_corralon) VALUES 
('ABC-123-A', 'INF-2023-001', '2023-10-15', 1500.50, 'pendiente', 2),
('XYZ-987-B', 'INF-2023-002', '2023-10-18', 3500.00, 'pagada', 1),
('JKL-456-C', 'INF-2023-003', '2023-10-20', 800.00, 'liberada', NULL),
('QWE-111-D', 'INF-2023-004', '2023-10-22', 2000.00, 'pendiente', 3),
('ABC-123-A', 'INF-2023-005', '2023-10-25', 500.00, 'pendiente', NULL);

-- Datos de Ejemplo para Pagos
INSERT INTO pagos (id_multa, fecha_pago, monto_pagado, metodo_pago, referencia_pago) VALUES 
(2, '2023-10-19', 3500.00, 'tarjeta', 'REF-TAR-001'),
(3, '2023-10-21', 800.00, 'transferencia', 'REF-TRA-002');
