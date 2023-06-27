CREATE TABLE public.platillo (
    id integer NOT NULL,
    precio integer,
    nombre character varying(50),
    stock integer
);

COPY public.platillo (id, precio, stock, nombre) FROM stdin;
1	8000	1	Spiderman   
2	10000	3	Superman        
\.