-- Active: 1786741319663@@127.0.0.1@3306@mysql

-- Base de Datos de Plataforma de Clases por Juan de Dios


CREATE DATABASE plataforma_clases;
-- Creacion de Base de Datos

USE plataforma_clases;
-- Usar Base de Datos

CREATE TABLE paises(
    id_pais INT AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_pais PRIMARY KEY (id_pais)
) COMMENT = 'CREACION TABLA PARA INGRESAR PAISES';

CREATE TABLE comunas(
    id_comuna INT AUTO_INCREMENT,
    comuna VARCHAR(50) NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_comuna PRIMARY KEY (id_comuna)
) COMMENT = 'CREACION DE TABLA PARA INGRESAR COMUNAS';

CREATE TABLE direcciones(
    id_direcciones INT AUTO_INCREMENT,
    comuna INT,
    pais INT,
    calle VARCHAR(50),
    numero INT NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direcciones),
    CONSTRAINT fk_pais_direccion FOREIGN KEY (pais) REFERENCES paises(id_pais), 
    CONSTRAINT fk_comuna_direccion FOREIGN KEY (comuna) REFERENCES comunas(id_comuna)
) COMMENT = 'CREACION DE TABLA DIRECCIONES CONECTADO CON PAISES Y COMUNAS ANASHEI';

CREATE TABLE personas(
    id_persona INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(11) NOT NULL UNIQUE,
    correo VARCHAR(255) NOT NULL UNIQUE,
    celular VARCHAR(50) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    direccion INT,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_personas PRIMARY KEY (id_persona),
    CONSTRAiNT fk_direccion_personas FOREIGN KEY (direccion) REFERENCES direcciones(id_direcciones)
) COMMENT = 'CREACION TABLAS PERSONAS CONECTADO CON DIRECCIONES';

CREATE TABLE estudiantes(
    id_estudiante INT AUTO_INCREMENT,
    info_persona INT,
    asistencia FLOAT NOT NULL,
    promedio FLOAT NOT NULL,
    login_estudiante VARCHAR(50) NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,
    
    CONSTRAINT pk_estudiante PRIMARY KEY (id_estudiante),
    CONSTRAINT fk_persona_estudiante FOREIGN KEY (info_persona) REFERENCES personas(id_persona)
) COMMENT = 'CREACION DE TABLA ESTUDIANTES CONECTADO CON PERSONAS';
-- Una persona puede ser estudiante lol

CREATE TABLE instructores(
    id_instructor INT AUTO_INCREMENT,
    info_persona INT,
    fecha_contratacion DATE NOT NULL,
    login_instructor VARCHAR(50) NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_instructor PRIMARY KEY (id_instructor),
    CONSTRAINT fk_persona_instructor FOREIGN KEY (info_persona) REFERENCES personas(id_persona)
) COMMENT = 'CREACION DE TABLA INSTRUCTOR CONECTADO CON PERSONAS';
-- Una persona puede ser instructor pues. 

CREATE TABLE cursos(
    id_cursos INT AUTO_INCREMENT,
    titulo_curso VARCHAR(50) NOT NULL,
    descripcion VARCHAR(50) NOT NULL,
    duracion_dias INT NOT NULL,
    cant_evaluacion INT NOT NULL,
    asistencia_min FLOAT NOT NULL,
    nota_min FLOAT NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_curso PRIMARY KEY (id_cursos)
) COMMENT = 'CREACION DE TABLA CURSOS';

CREATE TABLE instructor_cursos(
    id_ins_cursos INT AUTO_INCREMENT,
    instructor INT,
    curso INT,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_instructores_cursos PRIMARY KEY (id_ins_cursos),
    CONSTRAINT fk_instructor FOREIGN KEY (instructor) REFERENCES instructores(id_instructor),
    CONSTRAINT fk_curso FOREIGN KEY (curso) REFERENCES cursos(id_cursos)
) COMMENT = 'ASOCIANDO LA TABLA INSTRUCTORES CON CURSOS';
-- Un instructor puede tener muchos cursos


































CREATE TABLE direcciones(
    id_direcciones INT AUTO_INCREMENT,
    direccion VARCHAR(100) NOT NULL,
    habilitado BOOLEAN DEFAULT TRUE,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direcciones)

) COMMENT = 'Tabla para las direcciones de Personas';

CREATE TABLE personas(
    id_personas INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(50) NOT NULL UNIQUE,
    direccion VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL UNIQUE,
    celular VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,

    CONSTRAINT pk_personas PRIMARY KEY (id_personas)
    CONSTRAINT fk_personas_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direcciones)

) COMMENT = 'Tabla para informacion de las Personas'

-- HAY QUE ARREGLAMR MUCHO PIDO DISCULPAS


