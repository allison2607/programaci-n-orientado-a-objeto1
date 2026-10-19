from DATOS.MODELOS.personas import Personas

def mostrar_personas(persona:Personas):
    try:
        personas = persona.select().where(persona.habilitado == 1)
        return personas
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_persona(persona:Personas):
    try:
        nueva_persona = persona.save()
        return nueva_persona
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def editar_persona(persona:Personas):
    try:
        persona_editada = persona.save()
        return persona_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def deshabilitar_persona(persona:Personas):
    try:
        persona.habilitado = 0
        persona.save()
        return persona
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")