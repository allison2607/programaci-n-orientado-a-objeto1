CREATE DATABASE plataforma;

CREATE TABLE personas
(   id_estudiantes int auto_increment,
    nombre char(15) not null,
    apellido char(15) not null,
    rut char(9) not null,
    nacimiento date not null,
    correo varchar(20) not null
    habilitado tinyint not null default 1,
    CONSTRAINT pk_personas PRIMARY KEY (id_estudiantes));

ALTER TABLE estados COMMENT="tabla para guardar personas";
