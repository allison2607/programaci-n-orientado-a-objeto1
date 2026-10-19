from datos.modelos import curso
from datos.modelos.curso import Curso

def listado_cursos():
    Cursos = curso.select()
    if Cursos:
        return Cursos

def guardar_Curso(curso:curso):
    curso.save()

