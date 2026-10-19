from DATOS.MODELOS.estudiantes import Estudiantes

def mostrar_estudiantes(estudiante:Estudiantes):
    try:
        estudiantes = estudiante.select().where(estudiante.habilitado == 1)
        return estudiantes
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_estudiante(estudiante:Estudiantes):
    try:
        nuevo_estudiante = estudiante.save()
        return nuevo_estudiante
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
