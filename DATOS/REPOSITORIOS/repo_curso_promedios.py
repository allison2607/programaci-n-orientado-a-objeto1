from DATOS.MODELOS.cursos_promedio import CursosPromedio

def mostrar_cursos_promedios(promedio:CursosPromedio):
    try:
        promedios_curso = promedio.select()
        return promedios_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_curso_promedio(curso):
    try:
        promedio_curso = CursosPromedio.get(CursosPromedio.cursos == curso)
        return promedio_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_promedio_curso(promedio:CursosPromedio):
    try:
        nuevo_promedio = promedio.save()
        return nuevo_promedio
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        