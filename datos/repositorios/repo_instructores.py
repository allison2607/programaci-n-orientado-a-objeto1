from datos.modelos.instructor import Instructor
from datos.modelos.persona import Persona

def mostrar_instructores():
    try:
        instructores =Instructor.select(Instructor, Persona).join(Persona).where(Instructor.habilitado == 1)
        return instructores
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_instructor_rut(rut):
    try:
        instructor = Instructor.select().join(Persona).where(Persona.rut == rut).get()
        return instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_instructor_correo(correo):
    try:
        instructor = Instructor.select(Instructor, Persona).join(Persona).where((
            Persona.correo == correo) &
            (Instructor.habilitado == 1) &
            (Persona.habilitado == 1)).first()
        return instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_instructor(instructor:Instructor):
    try:
        instructor_nuevo = instructor.save()
        return instructor_nuevo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
