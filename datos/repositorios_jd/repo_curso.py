from datos.modelos.curso import Curso

def listado_cursos():
    cursos = Curso.select()
    if cursos:
        for curso in cursos:
            print(curso)
