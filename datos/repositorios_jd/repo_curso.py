from datos.modelos.curso import Curso

def listado_cursos():
    cursos = Curso.select()
    if cursos:
        return Curso

def guardar_curso(curso:Curso):
    curso.save()