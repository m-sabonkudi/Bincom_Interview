--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

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
-- Name: colors; Type: TABLE; Schema: public; Owner: msabonkudii
--

CREATE TABLE public.colors (
    id integer NOT NULL,
    color character varying(50) NOT NULL,
    frequency integer NOT NULL
);


ALTER TABLE public.colors OWNER TO msabonkudii;

--
-- Name: colors_id_seq; Type: SEQUENCE; Schema: public; Owner: msabonkudii
--

CREATE SEQUENCE public.colors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.colors_id_seq OWNER TO msabonkudii;

--
-- Name: colors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: msabonkudii
--

ALTER SEQUENCE public.colors_id_seq OWNED BY public.colors.id;


--
-- Name: colors id; Type: DEFAULT; Schema: public; Owner: msabonkudii
--

ALTER TABLE ONLY public.colors ALTER COLUMN id SET DEFAULT nextval('public.colors_id_seq'::regclass);


--
-- Data for Name: colors; Type: TABLE DATA; Schema: public; Owner: msabonkudii
--

COPY public.colors (id, color, frequency) FROM stdin;
1	GREEN	10
2	YELLOW	5
3	GREEN	10
4	BROWN	6
5	BLUE	30
6	PINK	5
7	BLUE	30
8	YELLOW	5
9	ORANGE	9
10	CREAM	2
11	ORANGE	9
12	RED	9
13	WHITE	16
14	BLUE	30
15	WHITE	16
16	BLUE	30
17	BLUE	30
18	BLUE	30
19	GREEN	10
20	ARSH	1
21	BROWN	6
22	GREEN	10
23	BROWN	6
24	BLUE	30
25	BLUE	30
26	BLEW	1
27	PINK	5
28	PINK	5
29	ORANGE	9
30	ORANGE	9
31	RED	9
32	WHITE	16
33	BLUE	30
34	WHITE	16
35	WHITE	16
36	BLUE	30
37	BLUE	30
38	BLUE	30
39	GREEN	10
40	YELLOW	5
41	GREEN	10
42	BROWN	6
43	BLUE	30
44	PINK	5
45	RED	9
46	YELLOW	5
47	ORANGE	9
48	RED	9
49	ORANGE	9
50	RED	9
51	BLUE	30
52	BLUE	30
53	WHITE	16
54	BLUE	30
55	BLUE	30
56	WHITE	16
57	WHITE	16
58	BLUE	30
59	BLUE	30
60	GREEN	10
61	WHITE	16
62	BLUE	30
63	BROWN	6
64	PINK	5
65	YELLOW	5
66	ORANGE	9
67	CREAM	2
68	ORANGE	9
69	RED	9
70	WHITE	16
71	BLUE	30
72	WHITE	16
73	BLUE	30
74	BLUE	30
75	BLUE	30
76	GREEN	10
77	GREEN	10
78	WHITE	16
79	GREEN	10
80	BROWN	6
81	BLUE	30
82	BLUE	30
83	BLACK	1
84	WHITE	16
85	ORANGE	9
86	RED	9
87	RED	9
88	RED	9
89	WHITE	16
90	BLUE	30
91	WHITE	16
92	BLUE	30
93	BLUE	30
94	BLUE	30
95	WHITE	16
\.


--
-- Name: colors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: msabonkudii
--

SELECT pg_catalog.setval('public.colors_id_seq', 95, true);


--
-- Name: colors colors_pkey; Type: CONSTRAINT; Schema: public; Owner: msabonkudii
--

ALTER TABLE ONLY public.colors
    ADD CONSTRAINT colors_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

