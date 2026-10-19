from DATOS.MODELOS.instructores import Instructores

def mostrar_instructores(instructor:Instructores):
    try:
        instructores = instructor.select().where(instructor.habilitado == 1)
        return instructores
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_instructor_nombre(nombre_instructor):
    try:
        instructor = Instructores.get(Instructores.nombre == nombre_instructor)
        return instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_instructor(instructor:Instructores):
    try:
        instructor_nuevo = instructor.save()
        return instructor_nuevo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
