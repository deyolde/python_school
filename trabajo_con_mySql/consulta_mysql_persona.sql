-- creacion de la tabla
CREATE TABLE persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    nombre_persona VARCHAR(50) NOT NULL,
    apellido_persona VARCHAR(50) NOT NULL,
    edad_persona INT NOT NULL,
    create_persona TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_persona TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
DESCRIBE persona;
DROP TABLE persona;
-- selecciona todos los registros
SELECT * FROM PERSONA;

/* inserta un registro */
INSERT INTO persona (nombre_persona, apellido_persona, edad_persona)
VALUES ('Juan', 'Perez', 56);





