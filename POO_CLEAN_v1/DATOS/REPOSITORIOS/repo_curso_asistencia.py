from DATOS.MODELOS.cursos_asistencia import CursosAsistencia

def mostrar_cursos_asistencia(cursoasis:CursosAsistencia):
    try:
        asistencias_cursos = cursoasis.select()
        return asistencias_cursos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_curso_asistencia_curso(curso):
    try:
        asistencia_curso = CursosAsistencia.get(CursosAsistencia.curso == curso)
        return asistencia_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_asistencia_curso(curso:CursosAsistencia):
    try:
        nueva_asistencia = curso.save()
        return nueva_asistencia
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        