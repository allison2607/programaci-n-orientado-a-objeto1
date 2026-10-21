from DATOS.MODELOS.instructor_curso import InstructorCurso

def mostrar_curso_instructores(cursosinstructor:InstructorCurso):
    try:
        cursos_instructor = cursosinstructor.select().where(cursosinstructor.habilitado == 1)
        return cursos_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_cursos_instructor(instructor):
    try:
        curso_instructor = InstructorCurso.get(InstructorCurso.instructor == instructor)
        return curso_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_curso_instructor(cursoinstructor:InstructorCurso):
    try:
        nuevo_curso_instructor = cursoinstructor.save()
        return nuevo_curso_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
