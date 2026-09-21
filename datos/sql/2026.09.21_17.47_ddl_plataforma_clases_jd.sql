USE plataforma_clases;

--algunos inserts
-- =========================================
-- 1. PAISES
-- =========================================

INSERT INTO paises (pais) VALUES
('Chile'),
('Argentina'),
('Peru'),
('Bolivia'),
('Brasil'),
('Colombia'),
('Mexico'),
('Ecuador'),
('Uruguay'),
('Paraguay');


-- =========================================
-- 2. COMUNAS
-- =========================================

INSERT INTO comunas (comuna) VALUES
('Temuco'),
('Padre Las Casas'),
('Lautaro'),
('Nueva Imperial'),
('Villarrica'),
('Pitrufquen'),
('Angol'),
('Victoria'),
('Carahue'),
('Cunco');


-- =========================================
-- 3. DIRECCIONES
-- =========================================

INSERT INTO direcciones (comuna, pais, calle, numero) VALUES
(1, 1, 'Av. Alemania', 100),
(2, 1, 'Av. Las Encinas', 200),
(3, 1, 'Calle Balmaceda', 300),
(4, 1, 'Calle Prat', 400),
(5, 1, 'Av. Pedro de Valdivia', 500),
(6, 1, 'Calle O Higgins', 600),
(7, 1, 'Av. Dillman Bullock', 700),
(8, 1, 'Calle Lagos', 800),
(9, 1, 'Calle Caupolican', 900),
(10, 1, 'Calle Comercio', 1000);


-- =========================================
-- 4. PERSONAS
-- =========================================

INSERT INTO personas
(nombre, apellido, rut, correo, celular, fecha_nacimiento, direccion)
VALUES
('Juan', 'Perez', '11111111-1', 'juan.perez@email.com', '911111111', '2000-01-15', 1),
('Maria', 'Gonzalez', '22222222-2', 'maria.gonzalez@email.com', '922222222', '1998-03-20', 2),
('Pedro', 'Soto', '33333333-3', 'pedro.soto@email.com', '933333333', '2001-05-10', 3),
('Ana', 'Rojas', '44444444-4', 'ana.rojas@email.com', '944444444', '1999-07-25', 4),
('Carlos', 'Munoz', '55555555-5', 'carlos.munoz@email.com', '955555555', '1997-09-12', 5),
('Sofia', 'Diaz', '66666666-6', 'sofia.diaz@email.com', '966666666', '2002-02-18', 6),
('Diego', 'Contreras', '77777777-7', 'diego.contreras@email.com', '977777777', '2000-11-30', 7),
('Camila', 'Vargas', '88888888-8', 'camila.vargas@email.com', '988888888', '2003-04-05', 8),
('Felipe', 'Torres', '99999999-9', 'felipe.torres@email.com', '999999999', '1996-06-14', 9),
('Laura', 'Martinez', '10101010-0', 'laura.martinez@email.com', '910101010', '1995-12-22', 10);


-- =========================================
-- 5. ESTUDIANTES
-- =========================================

INSERT INTO estudiantes
(info_persona, login_estudiante)
VALUES
(1, 'juanp'),
(2, 'mariag'),
(3, 'pedros'),
(4, 'anar'),
(5, 'carlosm'),
(6, 'sofiad'),
(7, 'diegoc'),
(8, 'camilav'),
(9, 'felipet'),
(10, 'lauram');


-- =========================================
-- 6. INSTRUCTORES
-- =========================================

INSERT INTO instructores
(info_persona, fecha_contratacion, login_instructor)
VALUES
(1, '2023-01-10', 'instructor01'),
(2, '2023-02-15', 'instructor02'),
(3, '2023-03-20', 'instructor03'),
(4, '2023-04-12', 'instructor04'),
(5, '2023-05-18', 'instructor05'),
(6, '2023-06-22', 'instructor06'),
(7, '2023-07-14', 'instructor07'),
(8, '2023-08-19', 'instructor08'),
(9, '2023-09-25', 'instructor09'),
(10, '2023-10-30', 'instructor10');


-- =========================================
-- 7. CURSOS
-- =========================================

INSERT INTO cursos
(titulo_curso, descripcion, duracion_dias, asistencia_min, nota_min)
VALUES
('Programacion Web', 'Introduccion al desarrollo web', 60, 75, 4.0),
('Base de Datos', 'Fundamentos de bases de datos', 45, 75, 4.0),
('Python', 'Programacion con Python', 50, 80, 4.0),
('Java', 'Programacion orientada a objetos', 60, 75, 4.0),
('HTML y CSS', 'Desarrollo de paginas web', 30, 70, 4.0),
('JavaScript', 'Programacion para sitios web', 45, 75, 4.0),
('Redes', 'Fundamentos de redes', 40, 75, 4.0),
('Ciberseguridad', 'Seguridad informatica basica', 50, 80, 4.0),
('Sistemas Operativos', 'Fundamentos de sistemas operativos', 45, 75, 4.0),
('Ingenieria de Software', 'Conceptos de desarrollo de software', 60, 80, 4.0);


-- =========================================
-- 8. INSTRUCTOR_CURSOS
-- =========================================

INSERT INTO instructor_cursos
(instructor, curso)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


-- =========================================
-- 9. ESPECIALIDADES
-- =========================================

INSERT INTO especialidades (especialidad) VALUES
('Programacion'),
('Bases de Datos'),
('Desarrollo Web'),
('Python'),
('Java'),
('Redes'),
('Ciberseguridad'),
('Sistemas Operativos'),
('Analisis de Sistemas'),
('Ingenieria de Software');


-- =========================================
-- 10. INSTRUCTORES_ESPECIALIDADES
-- =========================================

INSERT INTO instructores_especialidades
(instructor, especialidad)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


-- =========================================
-- 11. INSCRIPCIONES
-- =========================================

INSERT INTO inscripciones
(estudiante, curso, fecha_inscripcion, avance, nota_final)
VALUES
(1, 1, '2026-03-01', 90, 6.2),
(2, 2, '2026-03-02', 85, 5.8),
(3, 3, '2026-03-03', 75, 5.5),
(4, 4, '2026-03-04', 80, 6.0),
(5, 5, '2026-03-05', 95, 6.5),
(6, 6, '2026-03-06', 70, 5.0),
(7, 7, '2026-03-07', 88, 5.9),
(8, 8, '2026-03-08', 92, 6.4),
(9, 9, '2026-03-09', 78, 5.7),
(10, 10, '2026-03-10', 83, 6.1);


-- =========================================
-- 12. MODULOS
-- =========================================

INSERT INTO modulos
(curso, nombre_modulo)
VALUES
(1, 'Introduccion a la Web'),
(2, 'Modelo Relacional'),
(3, 'Fundamentos de Python'),
(4, 'Programacion Orientada a Objetos'),
(5, 'Estructura HTML'),
(6, 'Fundamentos de JavaScript'),
(7, 'Conceptos de Redes'),
(8, 'Seguridad Informatica'),
(9, 'Introduccion a Sistemas'),
(10, 'Ciclo de Desarrollo');


-- =========================================
-- 13. CONTENIDOS
-- =========================================

INSERT INTO contenidos
(modulo, descripcion)
VALUES
(1, 'Conceptos basicos de desarrollo web'),
(2, 'Tablas y relaciones'),
(3, 'Variables y tipos de datos'),
(4, 'Clases y objetos'),
(5, 'Etiquetas HTML'),
(6, 'Variables y funciones JavaScript'),
(7, 'Modelo TCP IP'),
(8, 'Amenazas informaticas'),
(9, 'Procesos y memoria'),
(10, 'Metodologias de desarrollo');


-- =========================================
-- 14. ACTIVIDADES
-- =========================================

INSERT INTO actividades
(contenido, nombre, descripcion, evaluacion)
VALUES
(1, 'Actividad Web', 'Crear una pagina web simple', TRUE),
(2, 'Actividad BD', 'Crear tablas relacionadas', TRUE),
(3, 'Actividad Python', 'Crear un programa basico', TRUE),
(4, 'Actividad Java', 'Crear una clase en Java', TRUE),
(5, 'Actividad HTML', 'Crear una pagina HTML', TRUE),
(6, 'Actividad JS', 'Crear funciones JavaScript', TRUE),
(7, 'Actividad Redes', 'Identificar protocolos de red', TRUE),
(8, 'Actividad Seguridad', 'Identificar amenazas', TRUE),
(9, 'Actividad Sistemas', 'Analizar procesos del sistema', TRUE),
(10, 'Actividad Software', 'Crear ciclo de desarrollo', TRUE);


-- =========================================
-- 15. NOTAS_ACTIVIDADES
-- =========================================

INSERT INTO notas_actividades
(actividad, estudiante, nota_actividad)
VALUES
(1, 1, 6.0),
(2, 2, 5.5),
(3, 3, 6.2),
(4, 4, 5.8),
(5, 5, 6.5),
(6, 6, 5.0),
(7, 7, 5.9),
(8, 8, 6.4),
(9, 9, 5.7),
(10, 10, 6.1);


-- =========================================
-- 16. CURSOS_ASISTENCIAS
-- =========================================

INSERT INTO cursos_asistencias
(estudiante, curso, asistencia)
VALUES
(1, 1, 95),
(2, 2, 90),
(3, 3, 85),
(4, 4, 88),
(5, 5, 97),
(6, 6, 80),
(7, 7, 92),
(8, 8, 96),
(9, 9, 87),
(10, 10, 91);


-- =========================================
-- 17. CURSOS_PROMEDIOS
-- =========================================

INSERT INTO cursos_promedios
(estudiante, curso, promedio)
VALUES
(1, 1, 6.2),
(2, 2, 5.8),
(3, 3, 5.5),
(4, 4, 6.0),
(5, 5, 6.5),
(6, 6, 5.0),
(7, 7, 5.9),
(8, 8, 6.4),
(9, 9, 5.7),
(10, 10, 6.1);