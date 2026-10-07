from datos.repositorios_jd.repo_curso import listado_cursos, guardar_curso
from prettytable import PrettyTable
from datos.modelos.curso import Curso

tabla_cursos = PrettyTable()
cursos = listado_cursos()

for curso in cursos:
    print(
        f"{curso.id_cursos} - {curso.asistencia_min} -" 
        f"{curso.descripcion} - {curso.duracion_dias} -" 
        f"{curso.nota_min} - {curso.titulo_curso} -"
        f"{curso.habilitado}"
        )


nuevo_curso = Curso()
nuevo_curso.asistencia_min = 50 
nuevo_curso.descripcion = 'Aprender POO'
nuevo_curso.titulo_curso = 'Programacion Orientada a Objetos'
nuevo_curso.duracion_dias = 90
nuevo_curso.nota_min = 4.0

guardar_curso(nuevo_curso) 