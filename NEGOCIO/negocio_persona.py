from auxiliar.aux_validacion import (validar_correo,
                                     validar_fecha,
                                     validar_celular,
                                     validar_rut)
from datos.modelos.persona import Persona
from datos.modelos.direccion import Direccion
from datos.modelos.comuna import Comuna
from datos.modelos.pais import Pais
from datos.repositorios.repo_personas import (guardar_persona,
                                              mostrar_personas,
                                              obtener_persona_rut)
from datos.repositorios.repo_comunas import obtener_comuna_nombre
from datos.repositorios.repo_paises import obtener_pais_nombre
from datos.repositorios.repo_direcciones import (obtener_direccion_calle_numero,
                                                 guardar_direccion)

def crear_persona(nombre, apellido,
                  rut, celular,
                  correo, calle,
                  numero, comuna,
                  pais, fecha_nacimiento):
    try:
        nombre = nombre.strip().capitalize()
        apellido = apellido.strip().capitalize()
        rut = rut.strip()
        celular = celular.strip()
        correo = correo.strip()
        calle = calle.strip().capitalize()
        numero = str(numero).strip()
        comuna = comuna.strip().capitalize()
        pais = pais.strip().capitalize()
        fecha_nacimiento = fecha_nacimiento.strip()
        if nombre == "":
            return "Debes ingresar nombre!"
        elif apellido == "":
            return "Debes ingresar apellido!"
        elif rut == "":
            return "Debes ingresar rut!"
        elif not validar_rut(rut):
            return "Formato de Rut no Valido!"
        elif celular == "":
            return "Debes ingresar celular!"
        elif correo == "":
            return "Debes ingresar correo!"
        elif not validar_correo(correo):
            return "El formato del correo no es valido!"
        elif calle == "":
            return "Debes ingresar una calle!"
        elif numero == "":
            return "Debes ingresar un numero!"
        elif comuna == "":
            return "Debes ingresar una comuna!"
        elif pais == "":
            return "Debes ingresar un pais!"
        elif fecha_nacimiento == "":
            return "Debes ingresar una fecha de nacimiento!"
        elif not validar_fecha(fecha_nacimiento):
            return "El formato de fecha no es valido!"
        direccion_existente = obtener_direccion_calle_numero(calle, numero)
        if not direccion_existente:
            comuna_obj = obtener_comuna_nombre(comuna)
            if not comuna_obj:
                return f"La comuna '{comuna}' no esta registrada"
            pais_obj = obtener_pais_nombre(pais)
            if not pais_obj:
                return f"El pais '{pais}' no esta registrado!"
            nueva_dir = Direccion()
            nueva_dir.calle = calle
            nueva_dir.numero = int(numero)
            nueva_dir.comuna = comuna_obj.id_comuna
            nueva_dir.pais = pais_obj.id_pais
            direccion_existente = guardar_direccion(nueva_dir)
        persona = Persona()
        persona.direccion = direccion_existente.id_direcciones
        persona.nombre = nombre
        persona.apellido = apellido
        persona.rut = rut
        persona.celular = celular
        persona.correo = correo
        persona.fecha_nacimiento = fecha_nacimiento
        nueva_persona = guardar_persona(persona)
        return nueva_persona
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def editar_persona(nombre, apellido,
                   rut, celular,
                   correo, calle,
                   numero, comuna,
                   pais, fecha_nacimiento):
    try:
        nombre = nombre.strip().capitalize()
        apellido = apellido.strip().capitalize()
        rut = rut.strip()
        celular = celular.strip()
        correo = correo.strip()
        calle = calle.strip().capitalize()
        numero = str(numero).strip()
        comuna = comuna.strip().capitalize()
        pais = pais.strip().capitalize()
        fecha_nacimiento = fecha_nacimiento.strip()
        persona_existente = obtener_persona_rut(rut)
        if not persona_existente:
            return f"No hay una persona ingresada con el rut '{rut}'"
        if nombre != "":
            persona_existente.nombre = nombre
        if apellido != "":
            persona_existente.apellido = apellido
        if celular != "":
            persona_existente.celular = celular
        if correo != "":
            if not validar_correo(correo):
                return "El formato del correo no es valido!"
            persona_existente.correo = correo
        if fecha_nacimiento != "":
            persona_existente.fecha_nacimiento = fecha_nacimiento

        if calle !="" or numero !="":
            if calle == "" or numero =="":
                return "Para actualizar la direccion debes ingresar nombre de calle y numero!"

            direccion_existente = obtener_direccion_calle_numero(calle, numero)

            if not direccion_existente:
                if comuna == "" or pais == "":
                    return "La direccion no esta registrada!"
            comuna_obj = obtener_comuna_nombre(comuna)
            if not comuna_obj:
                return f"La comuna '{comuna}' no esta registrada!" 

            pais_obj = obtener_pais_nombre(pais)
            if not pais_obj:
                return f"El pais '{pais}' no esta registrado!"

            nueva_dir = Direccion()
            nueva_dir.calle = calle
            nueva_dir.numero = int(numero)
            nueva_dir.comuna = comuna_obj.id_comuna
            nueva_dir.pais = pais_obj.id_pais
            direccion_existente = guardar_direccion(nueva_dir)

            persona_existente.direccion = direccion_existente

        persona_editada = guardar_persona(persona_existente)
        return persona_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def lista_persona():
    lista_persona = mostrar_personas()
    if lista_persona == 1:
        return lista_persona
    else:
        return "No hay personas ingresadas!"

def eliminar_persona(rut):
    try:
        rut = rut.strip()
        persona = obtener_persona_rut(rut)
        if not persona:
            print("Esa persona no existe!")

        persona.habilitado = 0
        guardar_persona(persona)
        return "Persona eliminada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_persona(rut):
    try:
        rut = rut.strip()
        persona = obtener_persona_rut(rut)
        if not persona:
            print("Esa persona no existe!")

        persona.habilitado = 1
        guardar_persona(persona)
        return "Persona Activada con Exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")    
        

        