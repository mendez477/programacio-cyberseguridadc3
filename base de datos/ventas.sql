-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS ventas;
USE ventas;

-- 2. Crear tabla clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50)
);

-- 3. Crear tabla productos
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

-- 4. Crear tabla facturas
CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    id_cliente INT,
    id_producto INT,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);


-- Insertar clientes
INSERT INTO clientes (nombre, correo, ciudad)
VALUES ('Ana Pérez', 'ana@email.com', 'Madrid'),
       ('Carlos Gómez', 'carlos@email.com', 'Barcelona'),
       ('Lucía Fernández', 'lucia@email.com', 'Valencia');

-- Insertar productos
INSERT INTO productos (nombre, precio, stock)
VALUES ('Laptop', 1200.00, 10),
       ('Teléfono', 800.00, 20),
       ('Tablet', 500.00, 15);

-- Insertar facturas
INSERT INTO facturas (fecha, id_cliente, id_producto, cantidad)
VALUES ('2025-12-15', 1, 1, 2),  -- Ana compra 2 laptops
       ('2025-12-16', 2, 2, 1),  -- Carlos compra 1 teléfono
       ('2025-12-17', 3, 3, 3);  -- Lucía compra 3 tablets
       
       
       
select * from clientes;

select * from productos;

select * from facturas;


SELECT f.id_factura, f.fecha, c.nombre AS cliente, p.nombre AS producto, f.cantidad,
       (f.cantidad * p.precio) AS total
FROM facturas f
JOIN clientes c ON f.id_cliente = c.id_cliente
JOIN productos p ON f.id_producto = p.id_producto;

SELECT c.nombre, SUM(f.cantidad * p.precio) AS total_compras
FROM facturas f
JOIN clientes c ON f.id_cliente = c.id_cliente
JOIN productos p ON f.id_producto = p.id_producto
GROUP BY c.nombre;


SELECT p.nombre, SUM(f.cantidad) AS total_vendidos
FROM facturas f
JOIN productos p ON f.id_producto = p.id_producto
GROUP BY p.nombre
ORDER BY total_vendidos DESC;








