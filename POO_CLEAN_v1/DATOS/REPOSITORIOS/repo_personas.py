from DATOS.MODELOS.personas import Personas

def mostrar_personas():
    try:
        personas = Personas.select().where(Personas.habilitado == 1)
        return personas
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_persona_rut(rut):
    try:
        persona = Personas.get(Personas.rut == rut)
        return persona
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_persona(persona:Personas):
    try:
        nueva_persona = persona.save()
        return nueva_persona 
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")



