from DATOS.MODELOS.inscripcion import Inscripcion

def mostrar_inscripciones(inscripcion:Inscripcion):
    try:
        inscripciones = inscripcion.select().where(inscripcion.habilitado == 1)
        return inscripciones
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_inscripcion(estudiante):
    try:
        inscripcion = Inscripcion.get(Inscripcion.estudiante == estudiante)
        return inscripcion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_inscripcion(inscripcion:Inscripcion):
    try:
        nueva_inscripcion = inscripcion.save()
        return nueva_inscripcion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
