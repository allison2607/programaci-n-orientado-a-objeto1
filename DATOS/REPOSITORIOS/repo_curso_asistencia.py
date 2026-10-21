from DATOS.MODELOS.cursos_asistencia import CursosAsistencias

def mostrar_cursos_asistencia(cursoasis:CursosAsistencias):
    try:
        asistencias_cursos = cursoasis.select()
        return asistencias_cursos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_curso_asistencia_curso(curso):
    try:
        asistencia_curso = CursosAsistencias.get(CursosAsistencias.curso == curso)
        return asistencia_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_asistencia_curso(curso:CursosAsistencias):
    try:
        nueva_asistencia = curso.save()
        return nueva_asistencia
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        