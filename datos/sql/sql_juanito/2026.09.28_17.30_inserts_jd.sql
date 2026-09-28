# Inserts creados por mi amiga Gemini
USE plataforma_clases;

-- 1. Inserción de Países
INSERT INTO paises (id_pais, pais, habilitado) VALUES 
(1, 'Chile', TRUE),
(2, 'Argentina', TRUE);

-- 2. Inserción de Comunas
INSERT INTO comunas (id_comuna, comuna, habilitado) VALUES 
(1, 'Santiago', TRUE),
(2, 'Providencia', TRUE),
(3, 'Las Condes', TRUE);

-- 3. Inserción de Direcciones
INSERT INTO direcciones (id_direcciones, comuna, pais, calle, numero, habilitado) VALUES 
(1, 1, 1, 'Av. Libertador Bernardo O''Higgins', 1234, TRUE),
(2, 2, 1, 'Av. Providencia', 2150, TRUE),
(3, 3, 1, 'Apoquindo', 4500, TRUE);

-- 4. Inserción de Personas (Mezcla de futuros estudiantes e instructores)
INSERT INTO personas (id_persona, nombre, apellido, rut, correo, celular, fecha_nacimiento, direccion, habilitado) VALUES 
(1, 'Carlos', 'Pérez', '12.345.678-9', 'carlos.perez@email.com', '+56911223344', '1995-05-12', 1, TRUE),
(2, 'Ana', 'Gómez', '98.765.432-1', 'ana.gomez@email.com', '+56999887766', '1998-08-20', 2, TRUE),
(3, 'Roberto', 'Soto', '15.432.109-K', 'roberto.soto@email.com', '+56955443322', '1985-03-15', 3, TRUE),
(4, 'María', 'Rojas', '16.789.012-3', 'maria.rojas@email.com', '+56966778899', '1990-11-05', 1, TRUE);

-- 5. Inserción de Estudiantes (Personas 1 y 2 - Nota: sin asistencia ni promedio por cambios de esquema)
INSERT INTO estudiantes (id_estudiante, info_persona, login_estudiante, habilitado) VALUES 
(1, 1, 'cperez95', TRUE),
(2, 2, 'agomez98', TRUE);

-- 6. Inserción de Instructores (Personas 3 y 4)
INSERT INTO instructores (id_instructor, info_persona, fecha_contratacion, login_instructor, habilitado) VALUES 
(1, 3, '2022-03-01', 'rsoto_dev', TRUE),
(2, 4, '2023-06-15', 'mrojas_tech', TRUE);

-- 7. Inserción de Cursos (Nota: sin cant_evaluacion por modificación de esquema)
INSERT INTO cursos (id_cursos, titulo_curso, descripcion, duracion_dias, asistencia_min, nota_min, habilitado) VALUES 
(1, 'Introducción a Python', 'Curso básico de programación en Python', 30, 75.0, 4.0, TRUE),
(2, 'Bases de Datos SQL', 'Diseño y consultas avanzadas en MySQL', 45, 80.0, 4.0, TRUE);

-- 8. Asociación Instructor - Cursos
INSERT INTO instructor_cursos (id_ins_cursos, instructor, curso, habilitado) VALUES 
(1, 1, 1, TRUE),
(2, 2, 2, TRUE);

-- 9. Inserción de Especialidades
INSERT INTO especialidades (id_especialidad, especialidad, habilitado) VALUES 
(1, 'Desarrollo de Software', TRUE),
(2, 'Administración de Bases de Datos', TRUE);

-- 10. Asociación Instructores - Especialidades
INSERT INTO instructores_especialidades (id_ins_esp, instructor, especialidad, habilitado) VALUES 
(1, 1, 1, TRUE),
(2, 2, 2, TRUE);

-- 11. Inserción de Inscripciones
INSERT INTO inscripciones (id_inscripcion, estudiante, curso, fecha_inscripcion, avance, nota_final, habilitado) VALUES 
(1, 1, 1, '2026-03-01', 50.0, NULL, TRUE),
(2, 2, 2, '2026-03-05', 100.0, 6.5, TRUE);

-- 12. Inserción de Módulos
INSERT INTO modulos (id_modulos, curso, nombre_modulo, habilitado) VALUES 
(1, 1, 'Fundamentos de Python', TRUE),
(2, 1, 'Estructuras de Control', TRUE),
(3, 2, 'Modelado Relacional', TRUE);

-- 13. Inserción de Contenidos
INSERT INTO contenidos (id_contenidos, modulo, descripcion, habilitado) VALUES 
(1, 1, 'Variables, tipos de datos y operadores básicos', TRUE),
(2, 2, 'Sentencias condicionales y bucles', TRUE),
(3, 3, 'Normalización y creación de tablas', TRUE);

-- 14. Inserción de Actividades
INSERT INTO actividades (id_actividades, contenido, nombre, descripcion, evaluacion, habilitado) VALUES 
(1, 1, 'Quiz 1: Tipos de datos', 'Evaluación corta sobre variables en Python', TRUE, TRUE),
(2, 3, 'Taller SQL Práctico', 'Creación de esquemas relacionales y restricciones', TRUE, TRUE);

-- 15. Inserción de Notas de Actividades
INSERT INTO notas_actividades (id_notas_act, actividad, estudiante, nota_actividad, habilitado) VALUES 
(1, 1, 1, 6.0, TRUE),
(2, 2, 2, 7.0, TRUE);

-- 16. Inserción de Asistencias por Curso (Tabla auxiliar nueva)
INSERT INTO cursos_asistencias (id_asistencia, estudiante, curso, asistencia) VALUES 
(1, 1, 1, 85.5),
(2, 2, 2, 92.0);

-- 17. Inserción de Promedios por Curso (Tabla auxiliar nueva)
INSERT INTO cursos_promedios (id_promedio, estudiante, curso, promedio) VALUES 
(1, 1, 1, 5.8),
(2, 2, 2, 6.5);