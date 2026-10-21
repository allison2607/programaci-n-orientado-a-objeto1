from DATOS.REPOSITORIOS.repo_personas import (mostrar_personas, 
                                              obtener_persona_rut,
                                              guardar_persona)
from DATOS.REPOSITORIOS.repo_direcciones import (mostrar_direcciones,
                                                 obtener_direccion_calle_numero,
                                                 guardar_direccion)
from DATOS.REPOSITORIOS.repo_comunas import (mostrar_comunas,
                                             obtener_comuna_nombre,
                                             guardar_comuna)
from DATOS.REPOSITORIOS.repo_paises import (mostrar_paises,
                                            obtener_pais_nombre,
                                            guardar_pais)
from DATOS.MODELOS.personas import Personas
from DATOS.MODELOS.direcciones import Direcciones
from DATOS.MODELOS.comunas import Comunas
from DATOS.MODELOS.paises import Paises


def crear_persona(persona:Personas,
                  direccion:Direcciones,
                  comunas:Comunas,
                  paises:Paises,
                  nombre,
                  rut, 
                  apellido,
                  celular,
                  correo,
                  fecha_nacimiento,
                  calle,
                  comuna,
                  numero, 
                  pais):
    try:
        if nombre == "":
            return "La persona debe tener nombre!"
        else:
            persona.nombre = nombre
        if rut == "":
            return "La persona debe tener RUT!"
        else:
            persona.rut = rut
        if apellido == "":
            return "La persona debe tener apellido!"
        else:
            persona.apellido = apellido
        if celular == "":
            return "La persona debe tener celular asociado!"
        else:
            persona.celular = celular
        if correo == "":
            return "La persona debe tener correo asociado!"
        else:
            persona.correo = correo
        if fecha_nacimiento == "":
            return "La persona debe tener fecha de nacimiento!" 
        else:
            persona.fecha_nacimiento = fecha_nacimiento
        if calle == "":
            return "La persona debe tener una calle!"
        else:
            direccion.calle = calle
        if comuna == "":
            return "La persona debe tener una comuna!"
        else:
            comunas.comuna = comuna
        if numero == "":
            return "La calle debe tener numero!"
        else:
            direccion.numero = numero
        if pais == "":
            return "La persona debe tener un pais!"
        else:
            paises.pais = pais

        nuevo_pais = guardar_pais(paises)
        nueva_comuna = guardar_comuna(comunas)
        direccion.comuna = nueva_comuna
        direccion.pais = nuevo_pais
        nueva_direccion = guardar_direccion(direccion)
        persona.direccion = nueva_direccion
        nueva_persona_exito = guardar_persona(persona)
        return nueva_persona_exito

    
    except Exception as error:
        print(f"Error al guardar la persona!: {error}")     

def lista_personas():
    lista_personas = mostrar_personas()
    if lista_personas == 1:
        return lista_personas
    else:
        return "No hay personas ingresadas!" 

def editar_persona(rut, nombre,
                   apellido, celular,
                   correo, fecha_nacimiento,
                   calle, comuna,
                   numero, pais):
    try:
        persona = obtener_persona_rut(rut)
        if not persona:
            print("Persona no encontrada")
        persona.nombre = nombre
        persona.apellido = apellido
        persona.celular = celular
        persona.correo = correo
        persona.fecha_nacimiento = fecha_nacimiento
        persona.calle = calle
        persona.comuna = comuna
        persona.numero = numero
        persona.pais = pais

        guardar_persona(persona)
        return "Persona actualizada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def eliminar_persona(rut):
    try:
        persona = obtener_persona_rut(rut)
        if not persona:
            print("Esa persona no existe!")

        persona.habilitado = 0
        guardar_persona(persona)
        return "Persona Eliminada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
