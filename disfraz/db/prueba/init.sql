--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Debian 14.6-1.pgdg110+1)
-- Dumped by pg_dump version 14.6 (Debian 14.6-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: mesa; Type: TABLE; Schema: public; Owner: postgres
--
CREATE TABLE usuarios (
  id_rut INTEGER NOT NULL,
  tipo VARCHAR NOT NULL,
  contraseña VARCHAR NOT NULL,
  nombre VARCHAR NOT NULL,
  PRIMARY KEY (id_rut)
);

CREATE TABLE historial (
  id_Historial INTEGER NOT NULL,
  id_rut INTEGER NOT NULL,
  id_prestamo INTEGER NOT NULL,
  multa INTEGER NOT NULL,
  PRIMARY KEY (id_Historial),
  FOREIGN KEY (id_rut) REFERENCES usuarios (id_rut),
  FOREIGN KEY (id_prestamo) REFERENCES prestamo (id_prestamo)
);

CREATE TABLE prestamo (
  id_prestamo INTEGER NOT NULL,
  id_producto INTEGER NOT NULL,
  fecha DATE NOT NULL,
  canProducto INTEGER NOT NULL,
  direccion VARCHAR NOT NULL,
  nombre_cliente VARCHAR NOT NULL,
  numero_cliente VARCHAR NOT NULL,
  PRIMARY KEY (id_prestamo),
  FOREIGN KEY (id_producto) REFERENCES producto (id_producto)
);

CREATE TABLE producto (
  id_producto INTEGER NOT NULL,
  nombre VARCHAR NOT NULL,
  precio INTEGER NOT NULL,
  talla INTEGER NOT NULL,
  stock INTEGER NOT NULL,
  PRIMARY KEY (id_producto)
);

ALTER TABLE producto
ADD CONSTRAINT fk_producto_historial
FOREIGN KEY (precio) REFERENCES historial (id_prestamo);


INSERT INTO usuarios (id_rut, tipo, contraseña, nombre) VALUES
(1, 'Administrador', 'admin123', 'Juan Pérez'),
(2, 'Usuario', 'user456', 'María Gómez'),
(3, 'Usuario', 'pass789', 'Carlos Rodríguez');

-- Tabla producto
INSERT INTO producto (id_producto, nombre, precio, talla, stock) VALUES
(1, 'Camiseta', 20, 42, 10),
(2, 'Pantalón', 35, 34, 5),
(3, 'Zapatos', 50, 40, 3);

-- Tabla prestamo
INSERT INTO prestamo (id_prestamo, id_producto, fecha, canProducto, direccion, nombre_cliente, numero_cliente) VALUES
(1, 'PRD001', '2023-06-01', 2, 'Calle Principal 123', 'Juan Pérez', '555-1234'),
(2, 'PRD002', '2023-06-02', 1, 'Avenida Central 456', 'María Gómez', '555-5678'),
(3, 'PRD003', '2023-06-03', 3, 'Plaza Mayor 789', 'Carlos Rodríguez', '555-9012');

-- Tabla historial
INSERT INTO historial (id_Historial, id_rut, id_prestamo, multa) VALUES
(1, 1, 1, 0),
(2, 2, 2, 0),
(3, 3, 3, 10);