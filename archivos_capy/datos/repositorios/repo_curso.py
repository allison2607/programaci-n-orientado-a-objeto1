from datos.modelos.curso import Curso

def listado_cursos():
    Cursos = Curso.select()
    if Cursos:
        return Cursos

def guardar_curso(curso:Curso):
    curso.save()

