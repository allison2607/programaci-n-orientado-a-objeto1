from DATOS.MODELOS.cursos_promedios import CursosPromedios

def mostrar_cursos_promedios(promedio:CursosPromedios):
    try:
        promedios_curso = promedio.select()
        return promedios_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_curso_promedio(curso):
    try:
        promedio_curso = CursosPromedios.get(CursosPromedios.cursos == curso)
        return promedio_curso
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_promedio_curso(promedio:CursosPromedios):
    try:
        nuevo_promedio = promedio.save()
        return nuevo_promedio
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        