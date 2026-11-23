from datos.modelos.estudiante import Estudiante
from datos.modelos.persona import Persona

def mostrar_estudiantes():
    try:
        estudiantes = Estudiante.select(Estudiante, Persona).join(Persona).where(Estudiante.habilitado == 1)
        return estudiantes
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_estudiante_rut(rut):
    try:
        estudiante = Estudiante.select().join(Persona).where(Persona.rut == rut).get()
        return estudiante
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        
def guardar_estudiante(estudiante:Estudiante):
    try:
        nuevo_estudiante = estudiante.save()
        return nuevo_estudiante
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
