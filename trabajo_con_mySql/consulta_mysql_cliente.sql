CREATE DATABASE on_fit_db;
USE on_fit_db;
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente VARCHAR(20) NOT NULL,
    apellido_cliente VARCHAR(20) NOT NULL,
    edad_cliente INT NOT NULL,
    telefono_cliente VARCHAR(15) UNIQUE,
    create_cliente TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_cliente TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
SELECT * FROM cliente;

INSERT INTO cliente (apellido_cliente, nombre_cliente, edad_cliente, telefono_cliente) 
VALUES('Victor', 'Loser', 56, 1123548799);
INSERT INTO cliente (apellido_cliente, nombre_cliente, edad_cliente, telefono_cliente) 
VALUES('Andrés', 'Cosachov', 25, 1126589877);
INSERT INTO cliente (apellido_cliente, nombre_cliente, edad_cliente, telefono_cliente) 
VALUES('Karina', 'Andreeva', 29, 022556898);
INSERT INTO cliente (apellido_cliente, nombre_cliente, edad_cliente, telefono_cliente) 
VALUES('Laura', 'Pescone', 25, 0381569878);