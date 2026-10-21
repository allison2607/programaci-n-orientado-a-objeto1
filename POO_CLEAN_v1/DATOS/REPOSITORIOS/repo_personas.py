from DATOS.MODELOS.persona import Persona

def mostrar_personas():
    try:
        personas = Persona.select().where(Persona.habilitado == 1)
        return personas
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_persona_rut(rut):
    try:
        persona = Persona.get(Persona.rut == rut)
        return persona
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_persona(persona:Persona):
    try:
        nueva_persona = persona.save()
        return nueva_persona 
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")



