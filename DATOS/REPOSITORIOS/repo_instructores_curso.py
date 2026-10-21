from DATOS.MODELOS.instructor_cursos import InstructorCursos

def mostrar_curso_instructores(cursosinstructor:InstructorCursos):
    try:
        cursos_instructor = cursosinstructor.select().where(cursosinstructor.habilitado == 1)
        return cursos_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_cursos_instructor(instructor):
    try:
        curso_instructor = InstructorCursos.get(InstructorCursos.instructor == instructor)
        return curso_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_curso_instructor(cursoinstructor:InstructorCursos):
    try:
        nuevo_curso_instructor = cursoinstructor.save()
        return nuevo_curso_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
