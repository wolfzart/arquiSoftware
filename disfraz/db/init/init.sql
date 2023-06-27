--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Debian 14.8-1.pgdg110+1)
-- Dumped by pg_dump version 14.8 (Debian 14.8-1.pgdg110+1)

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
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id_cli integer NOT NULL,
    direccion character varying NOT NULL,
    nombre character varying NOT NULL,
    telefono character varying NOT NULL
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- Name: historial; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.historial (
    id_historial integer NOT NULL,
    id_rut integer NOT NULL,
    id_prestamo integer NOT NULL,
    id_cli integer NOT NULL,
    multa integer NOT NULL,
    pagado boolean NOT NULL
);


ALTER TABLE public.historial OWNER TO postgres;

--
-- Name: prestamo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prestamo (
    id_prestamo integer NOT NULL,
    id_producto integer NOT NULL,
    id_cli integer NOT NULL,
    fecha date NOT NULL,
    cantproducto integer NOT NULL,
    devolucion boolean NOT NULL
);


ALTER TABLE public.prestamo OWNER TO postgres;

--
-- Name: producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto (
    id_producto integer NOT NULL,
    nombre character varying NOT NULL,
    precio integer NOT NULL,
    talla integer NOT NULL,
    stock integer NOT NULL
);


ALTER TABLE public.producto OWNER TO postgres;

--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id_rut integer NOT NULL,
    tipo character varying NOT NULL,
    "contraseña" character varying NOT NULL,
    nombre character varying NOT NULL
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id_cli, direccion, nombre, telefono) FROM stdin;
1	Calle Principal 123	Ana Sánchez	555-1234
2	Avenida Central 456	Pedro Torres	555-5678
3	Plaza Mayor 789	Laura Méndez	555-9012
\.


--
-- Data for Name: historial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.historial (id_historial, id_rut, id_prestamo, id_cli, multa, pagado) FROM stdin;
1	1	1	1	0	t
2	2	2	2	0	f
3	3	3	3	10	f
\.


--
-- Data for Name: prestamo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prestamo (id_prestamo, id_producto, id_cli, fecha, cantproducto, devolucion) FROM stdin;
1	1	1	2023-06-01	2	t
2	2	2	2023-06-02	1	f
3	3	3	2023-06-03	3	f
\.


--
-- Data for Name: producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producto (id_producto, nombre, precio, talla, stock) FROM stdin;
1	Camiseta	20	42	10
2	Pantalón	35	34	5
3	Zapatos	50	40	3
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id_rut, tipo, "contraseña", nombre) FROM stdin;
1	Administrador	admin123	Juan Pérez
2	Usuario	user456	María Gómez
3	Usuario	pass789	Carlos Rodríguez
\.


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id_cli);


--
-- Name: historial historial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_pkey PRIMARY KEY (id_historial);


--
-- Name: prestamo prestamo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT prestamo_pkey PRIMARY KEY (id_prestamo);


--
-- Name: producto producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (id_producto);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id_rut);


--
-- Name: historial historial_id_cli_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_id_cli_fkey FOREIGN KEY (id_cli) REFERENCES public.clientes(id_cli);


--
-- Name: historial historial_id_prestamo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_id_prestamo_fkey FOREIGN KEY (id_prestamo) REFERENCES public.historial(id_historial);


--
-- Name: historial historial_id_rut_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_id_rut_fkey FOREIGN KEY (id_rut) REFERENCES public.usuarios(id_rut);


--
-- Name: prestamo prestamo_id_cli_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT prestamo_id_cli_fkey FOREIGN KEY (id_cli) REFERENCES public.clientes(id_cli);


--
-- Name: prestamo prestamo_id_producto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamo
    ADD CONSTRAINT prestamo_id_producto_fkey FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto);


--
-- PostgreSQL database dump complete
--

