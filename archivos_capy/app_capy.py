
from archivos_capy.presentacion import cargar_menu
from archivos_capy.datos.repositorios.repo_curso import (
    listado_cursos,
    guardar_curso,
)
from archivos_capy.modelos.curso import Curso


cargar_menu()

for curso in listado_cursos():
    print(curso.id_cursos, curso.titulo_curso)


nuevo_curso = Curso()
nuevo_curso.asistencia_min = 50
nuevo_curso.descripcion = "Aprender POO"
nuevo_curso.titulo_curso = "Programacion Orientada a Objetos"
nuevo_curso.duracion_dias = 90
nuevo_curso.nota_min = 4.0

guardar_curso(nuevo_curso)
