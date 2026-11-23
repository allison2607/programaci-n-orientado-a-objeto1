USE plataforma_clases;

ALTER TABLE instructores
MODIFY COLUMN login_instructor VARCHAR(255) NOT NULL;

ALTER TABLE estudiantes
MODIFY COLUMN login_estudiante VARCHAR(255) NOT NULL; 