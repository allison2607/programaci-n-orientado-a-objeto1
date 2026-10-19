from presentacion import cargar_menu

#cargar_menu()

from datos.repositorios.repo_curso import listado_cursos, guardar_curso
from prettytable import prettytable
from datos.modelos.curso import Curso

tabla_cursos = PrettyTable()

nuevo_curso = Curso()
nuevo_curso.titulo_curso = 'Python básico'
nuevo_curso.descripcion = 'Introducción a Python'
nuevo_curso.duracion_dias = 30
nuevo_curso.asistencia_min = 75
nuevo_curso.nota_min = 4.0

guardar_curso(nuevo_curso)

cursos = listado_cursos()
for curso in cursos:
    print(f'{curso.id_cursos} - {curso.titulo_curso} - {curso.descripcion} - {curso.duracion_dias} - {curso.asistencia_min} - {curso.nota_min} - {curso.habilitado}')