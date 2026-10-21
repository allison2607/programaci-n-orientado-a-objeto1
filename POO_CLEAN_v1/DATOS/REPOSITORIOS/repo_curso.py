from DATOS.MODELOS.curso import Curso

def mostrar_cursos(curso:Curso):
    try:
        cursos = curso.select().where(curso.habilitado == 1)
        return cursos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_curso_titulo(titulo_curso):
    try:
        curso = Curso.get(Curso.titulo_curso == titulo_curso)
        return curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_curso(curso:Curso):
    try:
        nuevo_curso = curso.save()
        return nuevo_curso
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

