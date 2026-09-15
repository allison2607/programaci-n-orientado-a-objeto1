CREATE DATABASE IF NOT EXISTS plataforma_clases;
USE plataforma_clases;

CREATE TABLE IF NOT EXISTS paises (
    id_pais INT(11) AUTO_INCREMENT PRIMARY KEY,
    pais VARCHAR(50) NOT NULL,
    habilitado TINYINT(1) DEFAULT 1
);

CREATE TABLE IF NOT EXISTS comunas (
    id_comuna INT(11) AUTO_INCREMENT PRIMARY KEY,
    comuna VARCHAR(50) NOT NULL,
    habilitado TINYINT(1) DEFAULT 1
);

CREATE TABLE IF NOT EXISTS especialidades (
    id_especialidad INT(11) AUTO_INCREMENT PRIMARY KEY,
    especialidad VARCHAR(50) NOT NULL,
    habilitado TINYINT(1) DEFAULT 1
);

CREATE TABLE IF NOT EXISTS cursos (
    id_cursos INT(11) AUTO_INCREMENT PRIMARY KEY,
    titulo_curso VARCHAR(50) NOT NULL,
    descripcion VARCHAR(50),
    duracion_dias INT(11),
    cant_evaluacion INT(11),
    asistencia_min FLOAT,
    nota_min FLOAT,
    habilitado TINYINT(1) DEFAULT 1
);

CREATE TABLE IF NOT EXISTS direcciones (
    id_direcciones INT(11) AUTO_INCREMENT PRIMARY KEY,
    comuna INT(11),
    pais INT(11),
    calle VARCHAR(50),
    numero INT(11),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (comuna) REFERENCES comunas(id_comuna),
    FOREIGN KEY (pais) REFERENCES paises(id_pais)
);

CREATE TABLE IF NOT EXISTS personas (
    id_persona INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(11) UNIQUE,
    correo VARCHAR(255),
    celular VARCHAR(50),
    fecha_nacimiento DATE,
    direccion INT(11),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (direccion) REFERENCES direcciones(id_direcciones)
);

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT(11) AUTO_INCREMENT PRIMARY KEY,
    info_persona INT(11),
    asistencia FLOAT,
    promedio FLOAT,
    login_estudiante VARCHAR(50),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (info_persona) REFERENCES personas(id_persona)
);

CREATE TABLE IF NOT EXISTS instructores (
    id_instructor INT(11) AUTO_INCREMENT PRIMARY KEY,
    info_persona INT(11),
    fecha_contratacion DATE,
    login_instructor VARCHAR(50),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (info_persona) REFERENCES personas(id_persona)
);

CREATE TABLE IF NOT EXISTS instructores_especialidades (
    id_ins_esp INT(11) AUTO_INCREMENT PRIMARY KEY,
    instructor INT(11),
    especialidad INT(11),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (instructor) REFERENCES instructores(id_instructor),
    FOREIGN KEY (especialidad) REFERENCES especialidades(id_especialidad)
);

CREATE TABLE IF NOT EXISTS instructor_cursos (
    id_ins_cursos INT(11) AUTO_INCREMENT PRIMARY KEY,
    instructor INT(11),
    curso INT(11),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (instructor) REFERENCES instructores(id_instructor),
    FOREIGN KEY (curso) REFERENCES cursos(id_cursos)
);

CREATE TABLE IF NOT EXISTS inscripciones (
    id_inscripcion INT(11) AUTO_INCREMENT PRIMARY KEY,
    estudiante INT(11),
    curso INT(11),
    fecha_inscripcion DATE,
    avance FLOAT,
    nota_final FLOAT,
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (curso) REFERENCES cursos(id_cursos)
);

CREATE TABLE IF NOT EXISTS modulos (
    id_modulos INT(11) AUTO_INCREMENT PRIMARY KEY,
    curso INT(11),
    nombre_modulo VARCHAR(50),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (curso) REFERENCES cursos(id_cursos)
);

CREATE TABLE IF NOT EXISTS contenidos (
    id_contenidos INT(11) AUTO_INCREMENT PRIMARY KEY,
    modulo INT(11),
    descripcion VARCHAR(50),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (modulo) REFERENCES modulos(id_modulos)
);

CREATE TABLE IF NOT EXISTS actividades (
    id_actividades INT(11) AUTO_INCREMENT PRIMARY KEY,
    contenido INT(11),
    nombre VARCHAR(50),
    descripcion VARCHAR(50),
    evaluacion TINYINT(1),
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (contenido) REFERENCES contenidos(id_contenidos)
);

CREATE TABLE IF NOT EXISTS notas_actividades (
    id_notas_act INT(11) AUTO_INCREMENT PRIMARY KEY,
    actividad INT(11),
    estudiante INT(11),
    nota_actividad FLOAT,
    habilitado TINYINT(1) DEFAULT 1,
    FOREIGN KEY (actividad) REFERENCES actividades(id_actividades),
    FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante)
);