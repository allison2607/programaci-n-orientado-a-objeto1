from DATOS.MODELOS.inscripciones import Inscripciones

def mostrar_inscripciones(inscripcion:Inscripciones):
    try:
        inscripciones = inscripcion.select().where(inscripcion.habilitado == 1)
        return inscripciones
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_inscripcion(estudiante):
    try:
        inscripcion = Inscripciones.get(Inscripciones.estudiante == estudiante)
        return inscripcion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_inscripcion(inscripcion:Inscripciones):
    try:
        nueva_inscripcion = inscripcion.save()
        return nueva_inscripcion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
