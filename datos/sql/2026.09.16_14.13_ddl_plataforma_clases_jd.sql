-- Arreglando unos errores jeje
USE plataforma_clases;

CREATE TABLE cursos_asistencias(
    id_asistencia INT AUTO_INCREMENT,
    estudiante INT,
    curso INT,
    asistencia FLOAT,

    CONSTRAINT pk_asistencia PRIMARY KEY (id_asistencia),
    CONSTRAINT fk_estudiante_asistencia FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante),
    CONSTRAINT fk_curso_asistencia FOREIGN KEY (curso) REFERENCES cursos(id_cursos)
) COMMENT = 'ASIGNARLE UNA ASISTENCIA A UN ESTUDIANTE REFERENTE A UN CURSO';
-- Un estudiante puede tener muchas asistencias a diversos cursos

CREATE TABLE cursos_promedios(
    id_promedio INT AUTO_INCREMENT,
    estudiante INT,
    curso INT,
    promedio FLOAT,

    CONSTRAINT pk_promedio PRIMARY KEY (id_promedio),
    CONSTRAINT fk_estudiante_promedio FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante),
    CONSTRAINT fk_curso_promedio FOREIGN KEY (curso) REFERENCES cursos(id_cursos) 
) COMMENT = 'ASIGNARLE UN PROMEDIO A UN ESTUDIANTE REFERENTE A UN CURSO';
-- Un estudiante puede tener muchos promedios a diversos cursos

ALTER TABLE estudiantes
    DROP COLUMN asistencia;
-- Eliminar el atributo asistencia (Creamos una tabla auxiliar para eso)

ALTER TABLE estudiantes
    DROP COLUMN promedio;
-- Eliminar el atributo promedio (Creamos una tabla auxiliar para eso)

ALTER TABLE cursos
    DROP COLUMN cant_evaluacion;
-- Eliminar el atributo cantidad de evaluaciones, ya que los datos calculables no deben ser atributos 
-- Prueba

ALTER TABLE personas
    MODIFY rut VARCHAR(50) NOT NULL UNIQUE;
-- Agregarle mas caracteres al rut