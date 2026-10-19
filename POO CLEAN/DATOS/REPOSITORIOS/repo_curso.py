from DATOS.MODELOS.cursos import Curso

def mostrar_cursos(curso:Curso):
    try:
        cursos = curso.select().where(curso.habilitado == 1)
        return cursos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_curso(curso:Curso):
    try:
        nuevo_curso = curso.save()
        return nuevo_curso
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def editar_curso(curso:Curso):
    try:
        curso_editado = curso.save()
        return curso_editado
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def deshabilitar_curso(curso:Curso):
    try:
        curso.habilitado = 0
        curso.save()
        return curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
