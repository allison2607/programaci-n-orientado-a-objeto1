from DATOS.MODELOS.instructores import Instructores

def mostrar_instructores(instructor:Instructores):
    try:
        instructores = instructor.select().where(instructor.habilitado == 1)
        return instructores
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_instructor(instructor:Instructores):
    try:
        instructor_nuevo = instructor.save()
        return instructor_nuevo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def editar_instructor(instructor:Instructores):
    try:
        instructor_editado = instructor.save()
        return instructor_editado
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def deshabilitar_instructor(instructor:Instructores):
    try:
        instructor.habilitado = 0
        instructor.save()
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")