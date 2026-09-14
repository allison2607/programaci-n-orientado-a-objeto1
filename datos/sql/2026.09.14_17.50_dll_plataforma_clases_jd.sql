-- Active: 1786741319663@@127.0.0.1@3306@mysql

-- Base de Datos de Plataforma de Clases por Juan de Dios


CREATE DATABASE plataforma_clases;
-- Creacion de Base de Datos

USE plataforma_clases;
-- Usar Base de Datos

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


