
from archivos_capy.modelos.curso import Curso


def listado_cursos():
    return list(Curso.select())


def obtener_curso(id_curso):
    return Curso.get_or_none(
        Curso.id_cursos == id_curso
    )


def guardar_curso(curso: Curso):
    curso.save()
    return curso


def actualizar_curso(id_curso, **datos):
    return (
        Curso.update(**datos)
        .where(Curso.id_cursos == id_curso)
        .execute()
    )


def eliminar_curso(id_curso):
    return (
        Curso.delete()
        .where(Curso.id_cursos == id_curso)
        .execute()
    )

