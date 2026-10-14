from archivos_capy.modelos.curso import Curso


def listado_cursos():
    return list(Curso.select())