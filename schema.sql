
CREATE TABLE IF NOT EXISTS boleta
(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  fecha TEXT NOT NULL,
  nombre TEXT NOT NULL,
  direccion TEXT NOT NULL,
  dni TEXT NOT NULL
  
);


CREATE TABLE IF NOT EXISTS producto
(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  stock INT NOT NULL,
  precio REAL NOT NULL
  
);


CREATE TABLE IF NOT EXISTS detalle_boleta
(
  boleta_id INTEGER NOT NULL,
  producto_id INTEGER NOT NULL,
  cantidad INTEGER NOT NULL,
  PRIMARY KEY (boleta_id, producto_id),
  CONSTRAINT fk_detalle_boleta_boleta
    FOREIGN KEY (boleta_id)
    REFERENCES 	boleta (id)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT fk_detalle_boleta_producto
    FOREIGN KEY (producto_id)
    REFERENCES producto (id)
    ON DELETE NO ACTION
    ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS empresa
(
  id INTEGER NOT NULL PRIMARY KEY,
  ruc TEXT NOT NULL,
  nombre TEXT NOT NULL,
  direccion TEXT NOT NULL,
  celular TEXT NOT NULL,
  email TEXT NOT NULL
);

-- INSERT INTO empresa (id, ruc, nombre, direccion, celular, email)
-- VALUES (1, 'ruc', 'nombre', 'direccion', 'celular', 'email')
-- ON CONFLICT DO NOTHING;

-- INSERT INTO empresa(id, ruc, nombre, direccion, celular, email)
-- SELECT 1, 'ruc', 'nombre', 'direccion', 'celular', 'email'
-- WHERE NOT EXISTS(SELECT 1 FROM empresa WHERE id=1);

-- INSERT OR IGNORE INTO empresa (id, ruc, nombre, direccion, celular, email)
-- VALUES (1, 'ruc', 'nombre', 'direccion', 'celular', 'email');


-- INSERT INTO producto
-- VALUES
-- (6, 'Cuaderno espiral', 100, 8.00),
-- (2, 'Caja de colores', 100, 2.00),
-- (3, 'Regla de 30cm', 100, 3.00),
-- (4, 'Lapiz 2B', 100, 1.00),
-- (5, 'Resaltador', 100, 2.50);
