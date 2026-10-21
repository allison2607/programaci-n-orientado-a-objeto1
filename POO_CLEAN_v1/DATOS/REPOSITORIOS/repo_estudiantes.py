from DATOS.MODELOS.estudiante import Estudiante

def mostrar_estudiantes(estudiante:Estudiante):
    try:
        estudiantes = estudiante.select().where(estudiante.habilitado == 1)
        return estudiantes
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_estudiante_nombre(nombre_estudiante):
    try:
        estudiante = Estudiante.get(Estudiante.nombre == nombre_estudiante)
        return estudiante
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        
def guardar_estudiante(estudiante:Estudiante):
    try:
        nuevo_estudiante = estudiante.save()
        return nuevo_estudiante
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
