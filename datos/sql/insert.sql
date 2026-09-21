INSERT INTO paises (pais) VALUES
('Chile'),
('Argentina'),
('Perú'),
('Bolivia'),
('Brasil'),
('Uruguay'),
('Paraguay'),
('Colombia'),
('Ecuador'),
('Venezuela'),
('México'),
('Estados Unidos'),
('Canadá'),
('España'),
('Francia'),
('Alemania'),
('Italia'),
('Reino Unido'),
('Australia'),
('Japón');

INSERT INTO comunas (comuna) VALUES
('Santiago'),
('Maipú'),
('Puente Alto'),
('La Florida'),
('Las Condes'),
('Providencia'),
('Ñuñoa'),
('Vitacura'),
('Lo Barnechea'),
('La Reina'),
('Peñalolén'),
('Macul'),
('San Miguel'),
('La Cisterna'),
('El Bosque'),
('San Ramón'),
('La Granja'),
('San Joaquín'),
('Estación Central'),
('Quinta Normal'),
('Lo Prado'),
('Pudahuel'),
('Cerro Navia'),
('Renca'),
('Independencia'),
('Recoleta'),
('Conchalí'),
('Huechuraba'),
('Quilicura'),
('Colina'),
('Lampa'),
('Talagante'),
('Melipilla'),
('Buin'),
('Paine'),
('San Bernardo'),
('Calera de Tango'),
('Pirque'),
('San José de Maipo');

INSERT INTO direcciones (comuna, pais, calle, numero) VALUES
((SELECT id_comuna FROM comunas WHERE comuna = 'Santiago'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Libertador Bernardo O''Higgins', 1234),
((SELECT id_comuna FROM comunas WHERE comuna = 'Maipú'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Pajaritos', 2456),
((SELECT id_comuna FROM comunas WHERE comuna = 'Puente Alto'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Concha y Toro', 7890),
((SELECT id_comuna FROM comunas WHERE comuna = 'La Florida'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Vicuña Mackenna', 3456),
((SELECT id_comuna FROM comunas WHERE comuna = 'Las Condes'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Apoquindo', 5678),
((SELECT id_comuna FROM comunas WHERE comuna = 'Providencia'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Providencia', 2345),
((SELECT id_comuna FROM comunas WHERE comuna = 'Ñuñoa'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Irarrázaval', 4567),
((SELECT id_comuna FROM comunas WHERE comuna = 'Vitacura'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Vitacura', 6789),
((SELECT id_comuna FROM comunas WHERE comuna = 'Lo Barnechea'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. La Dehesa', 7891),
((SELECT id_comuna FROM comunas WHERE comuna = 'La Reina'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Larraín', 3456),
((SELECT id_comuna FROM comunas WHERE comuna = 'Peñalolén'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Grecia', 2345),
((SELECT id_comuna FROM comunas WHERE comuna = 'Macul'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Macul', 5678),
((SELECT id_comuna FROM comunas WHERE comuna = 'San Miguel'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Gran Avenida', 3456),
((SELECT id_comuna FROM comunas WHERE comuna = 'La Cisterna'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. El Parrón', 1234),
((SELECT id_comuna FROM comunas WHERE comuna = 'El Bosque'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Lo Blanco', 4567),
((SELECT id_comuna FROM comunas WHERE comuna = 'San Ramón'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Santa Rosa', 6789),
((SELECT id_comuna FROM comunas WHERE comuna = 'La Granja'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Américo Vespucio', 2345),
((SELECT id_comuna FROM comunas WHERE comuna = 'Estación Central'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Alameda', 3456),
((SELECT id_comuna FROM comunas WHERE comuna = 'Quinta Normal'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. Ecuador', 5678),
((SELECT id_comuna FROM comunas WHERE comuna = 'Lo Prado'), (SELECT id_pais FROM paises WHERE pais = 'Chile'), 'Av. José Joaquín Pérez', 7890);


INSERT INTO personas (nombre, apellido, rut, correo, celular, fecha_nacimiento, direccion) VALUES
('Juan', 'Pérez', '12.345.678-9', 'juan.perez@gmail.com', '+56912345678', '1990-05-15', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Libertador Bernardo O''Higgins' AND numero = 1234)),
('María', 'González', '13.456.789-0', 'maria.gonzalez@gmail.com', '+56923456789', '1988-08-22', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Pajaritos' AND numero = 2456)),
('Pedro', 'Ramírez', '14.567.890-1', 'pedro.ramirez@gmail.com', '+56934567890', '1992-03-10', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Concha y Toro' AND numero = 7890)),
('Camila', 'Soto', '15.678.901-2', 'camila.soto@gmail.com', '+56945678901', '1995-11-30', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Vicuña Mackenna' AND numero = 3456)),
('Diego', 'Muñoz', '16.789.012-3', 'diego.munoz@gmail.com', '+56956789012', '1987-07-18', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Apoquindo' AND numero = 5678)),
('Valentina', 'Rojas', '17.890.123-4', 'valentina.rojas@gmail.com', '+56967890123', '1996-01-25', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Providencia' AND numero = 2345)),
('Felipe', 'Contreras', '18.901.234-5', 'felipe.contreras@gmail.com', '+56978901234', '1991-09-12', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Irarrázaval' AND numero = 4567)),
('Sofía', 'Martínez', '19.012.345-6', 'sofia.martinez@gmail.com', '+56989012345', '1994-06-05', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Vitacura' AND numero = 6789)),
('Andrés', 'Silva', '20.123.456-7', 'andres.silva@gmail.com', '+56990123456', '1989-12-20', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. La Dehesa' AND numero = 7891)),
('Javiera', 'Morales', '21.234.567-8', 'javiera.morales@gmail.com', '+56911223344', '1997-04-14', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Larraín' AND numero = 3456)),
('Sebastián', 'Castillo', '22.345.678-9', 'sebastian.castillo@gmail.com', '+56922334455', '1993-10-08', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Grecia' AND numero = 2345)),
('Fernanda', 'Torres', '23.456.789-0', 'fernanda.torres@gmail.com', '+56933445566', '1998-02-17', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Macul' AND numero = 5678)),
('Nicolás', 'Vargas', '24.567.890-1', 'nicolas.vargas@gmail.com', '+56944556677', '1990-11-03', (SELECT id_direcciones FROM direcciones WHERE calle = 'Gran Avenida' AND numero = 3456)),
('Daniela', 'Fuentes', '25.678.901-2', 'daniela.fuentes@gmail.com', '+56955667788', '1995-05-27', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. El Parrón' AND numero = 1234)),
('Cristóbal', 'Espinoza', '26.789.012-3', 'cristobal.espinoza@gmail.com', '+56966778899', '1986-08-16', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Lo Blanco' AND numero = 4567)),
('Antonia', 'Araya', '27.890.123-4', 'antonia.araya@gmail.com', '+56977889900', '1999-03-29', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Santa Rosa' AND numero = 6789)),
('Matías', 'Bravo', '28.901.234-5', 'matias.bravo@gmail.com', '+56988990011', '1992-07-07', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Américo Vespucio' AND numero = 2345)),
('Carolina', 'Navarro', '29.012.345-6', 'carolina.navarro@gmail.com', '+56999001122', '1988-01-19', (SELECT id_direcciones FROM direcciones WHERE calle = 'Alameda' AND numero = 3456)),
('Tomás', 'Salazar', '30.123.456-7', 'tomas.salazar@gmail.com', '+56910112233', '1996-09-24', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. Ecuador' AND numero = 5678)),
('Constanza', 'Pizarro', '31.234.567-8', 'constanza.pizarro@gmail.com', '+56920223344', '1994-12-11', (SELECT id_direcciones FROM direcciones WHERE calle = 'Av. José Joaquín Pérez' AND numero = 7890));


INSERT INTO estudiantes (info_persona, asistencia, promedio, login_estudiante) VALUES
((SELECT id_persona FROM personas WHERE rut = '12.345.678-9'), 95.5, 6.2, 'juanperez'),
((SELECT id_persona FROM personas WHERE rut = '13.456.789-0'), 88.0, 5.7, 'mariagonzalez'),
((SELECT id_persona FROM personas WHERE rut = '14.567.890-1'), 92.5, 6.0, 'pedroramirez'),
((SELECT id_persona FROM personas WHERE rut = '15.678.901-2'), 97.0, 6.5, 'camilasoto'),
((SELECT id_persona FROM personas WHERE rut = '16.789.012-3'), 84.5, 5.4, 'diegomunoz'),
((SELECT id_persona FROM personas WHERE rut = '17.890.123-4'), 91.0, 6.1, 'valentinarojas'),
((SELECT id_persona FROM personas WHERE rut = '18.901.234-5'), 86.5, 5.8, 'felipecontreras'),
((SELECT id_persona FROM personas WHERE rut = '19.012.345-6'), 98.0, 6.7, 'sofiamartinez'),
((SELECT id_persona FROM personas WHERE rut = '20.123.456-7'), 89.5, 5.9, 'andressilva'),
((SELECT id_persona FROM personas WHERE rut = '21.234.567-8'), 94.0, 6.3, 'javieramorales');


INSERT INTO instructores (info_persona, fecha_contratacion, login_instructor) VALUES
((SELECT id_persona FROM personas WHERE rut = '22.345.678-9'), '2022-03-15', 'sebastiancastillo'),
((SELECT id_persona FROM personas WHERE rut = '23.456.789-0'), '2021-08-20', 'fernandatorres'),
((SELECT id_persona FROM personas WHERE rut = '24.567.890-1'), '2023-01-10', 'nicolasvargas'),
((SELECT id_persona FROM personas WHERE rut = '25.678.901-2'), '2020-06-05', 'danielafuentes'),
((SELECT id_persona FROM personas WHERE rut = '26.789.012-3'), '2022-11-12', 'cristobalespinoza');


INSERT INTO cursos (titulo_curso, descripcion, duracion_dias, cant_evaluacion, asistencia_min, nota_min) VALUES
('Programación Java', 'Fundamentos de Java', 60, 4, 75, 4.0),
('Bases de Datos', 'SQL y modelamiento', 45, 3, 75, 4.0),
('Desarrollo Web', 'HTML CSS y JavaScript', 50, 4, 80, 4.0),
('Python', 'Programación con Python', 55, 4, 75, 4.0),
('Redes', 'Fundamentos de redes', 40, 3, 70, 4.0),
('JavaScript', 'Programación frontend', 45, 4, 75, 4.0),
('Git y GitHub', 'Control de versiones', 30, 2, 70, 4.0),
('Ciberseguridad', 'Seguridad informática', 60, 5, 80, 4.0),
('Linux', 'Administración de Linux', 40, 3, 75, 4.0),
('Algoritmos', 'Estructuras y algoritmos', 50, 4, 80, 4.0);



INSERT INTO especialidades (especialidad) VALUES
('Programación'),
('Bases de Datos'),
('Desarrollo Web'),
('Ciberseguridad'),
('Redes'),
('Inteligencia Artificial'),
('Sistemas Operativos'),
('Ingeniería de Software'),
('Algoritmos'),
('DevOps');



INSERT INTO instructor_cursos (instructor, curso) VALUES
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '22.345.678-9')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Programación Java')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '23.456.789-0')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Bases de Datos')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '24.567.890-1')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Desarrollo Web')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '25.678.901-2')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Python')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '26.789.012-3')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Redes')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '22.345.678-9')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'JavaScript')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '23.456.789-0')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Git y GitHub')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '24.567.890-1')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Ciberseguridad')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '25.678.901-2')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Linux')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '26.789.012-3')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Algoritmos'));



INSERT INTO instructores_especialidades (instructor, especialidad) VALUES
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '22.345.678-9')), (SELECT id_especialidad FROM especialidades WHERE especialidad = 'Programación')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '23.456.789-0')), (SELECT id_especialidad FROM especialidades WHERE especialidad = 'Bases de Datos')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '24.567.890-1')), (SELECT id_especialidad FROM especialidades WHERE especialidad = 'Desarrollo Web')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '25.678.901-2')), (SELECT id_especialidad FROM especialidades WHERE especialidad = 'Programación')),
((SELECT id_instructor FROM instructores WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '26.789.012-3')), (SELECT id_especialidad FROM especialidades WHERE especialidad = 'Redes'));



INSERT INTO inscripciones (estudiante, curso, fecha_inscripcion, avance, nota_final) VALUES
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '12.345.678-9')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Programación Java'), '2025-03-01', 85.5, 6.2),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '13.456.789-0')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Bases de Datos'), '2025-03-02', 78.0, 5.7),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '14.567.890-1')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Desarrollo Web'), '2025-03-03', 92.0, 6.0),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '15.678.901-2')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Python'), '2025-03-04', 95.0, 6.5),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '16.789.012-3')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Redes'), '2025-03-05', 70.0, 5.4),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '17.890.123-4')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'JavaScript'), '2025-03-06', 88.0, 6.1),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '18.901.234-5')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Git y GitHub'), '2025-03-07', 76.5, 5.8),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '19.012.345-6')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Ciberseguridad'), '2025-03-08', 96.0, 6.7),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '20.123.456-7')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Linux'), '2025-03-09', 82.0, 5.9),
((SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '21.234.567-8')), (SELECT id_cursos FROM cursos WHERE titulo_curso = 'Algoritmos'), '2025-03-10', 90.0, 6.3);


INSERT INTO modulos (curso, nombre_modulo) VALUES
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Programación Java'), 'Introducción a Java'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Programación Java'), 'Programación Orientada a Objetos'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Bases de Datos'), 'Modelo Relacional'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Bases de Datos'), 'Consultas SQL'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Desarrollo Web'), 'HTML y CSS'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Desarrollo Web'), 'JavaScript'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Python'), 'Fundamentos de Python'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Python'), 'Funciones y Clases'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Redes'), 'Conceptos de Redes'),
((SELECT id_cursos FROM cursos WHERE titulo_curso = 'Redes'), 'Protocolos');


INSERT INTO contenidos (modulo, descripcion) VALUES
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Introducción a Java'), 'Variables y tipos de datos'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Introducción a Java'), 'Condicionales y ciclos'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Programación Orientada a Objetos'), 'Clases y objetos'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Modelo Relacional'), 'Tablas y relaciones'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Consultas SQL'), 'SELECT y WHERE'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'HTML y CSS'), 'Estructura HTML'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'JavaScript'), 'Variables JavaScript'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Fundamentos de Python'), 'Sintaxis Python'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Funciones y Clases'), 'Funciones Python'),
((SELECT id_modulos FROM modulos WHERE nombre_modulo = 'Conceptos de Redes'), 'Direcciones IP');


INSERT INTO actividades (contenido, nombre, descripcion, evaluacion) VALUES
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Variables y tipos de datos'), 'Actividad Java 1', 'Ejercicios de variables', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Condicionales y ciclos'), 'Actividad Java 2', 'Ejercicios de ciclos', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Clases y objetos'), 'Actividad Java 3', 'Crear clases Java', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Tablas y relaciones'), 'Actividad SQL 1', 'Crear tablas relacionadas', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'SELECT y WHERE'), 'Actividad SQL 2', 'Realizar consultas SQL', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Estructura HTML'), 'Actividad Web 1', 'Crear página HTML', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Variables JavaScript'), 'Actividad Web 2', 'Ejercicios JavaScript', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Sintaxis Python'), 'Actividad Python 1', 'Ejercicios Python', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Funciones Python'), 'Actividad Python 2', 'Crear funciones', TRUE),
((SELECT id_contenidos FROM contenidos WHERE descripcion = 'Direcciones IP'), 'Actividad Redes 1', 'Ejercicios de IP', TRUE);

INSERT INTO notas_actividades (actividad, estudiante, nota_actividad) VALUES
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Java 1'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '12.345.678-9')),
    6.5
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Java 2'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '13.456.789-0')),
    5.8
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Java 3'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '14.567.890-1')),
    6.2
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad SQL 1'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '15.678.901-2')),
    6.7
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad SQL 2'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '16.789.012-3')),
    5.4
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Web 1'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '17.890.123-4')),
    6.1
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Web 2'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '18.901.234-5')),
    5.9
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Python 1'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '19.012.345-6')),
    6.8
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Python 2'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '20.123.456-7')),
    5.7
),
(
    (SELECT id_actividades FROM actividades WHERE nombre = 'Actividad Redes 1'),
    (SELECT id_estudiante FROM estudiantes WHERE info_persona = (SELECT id_persona FROM personas WHERE rut = '21.234.567-8')),
    6.3
);
