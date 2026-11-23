import bcrypt
from datos.modelos.estudiante import Estudiante
from datos.repositorios.repo_estudiantes import (mostrar_estudiantes,
                                                 obtener_estudiante_rut,
                                                 guardar_estudiante)
from datos.repositorios.repo_personas import (obtener_persona_rut)

def asignar_como_estudiante(rut, contasenia):
    try:
        rut = rut.strip()
        contrasenia = contasenia.strip()

        persona = obtener_persona_rut(rut)

        if not persona:
            return "Persona no Registrada!"

        estudiante_existente = Estudiante.get_or_none(Estudiante.info_persona == persona.id_persona)
        if estudiante_existente:
            return f"La persona con RUT {rut} ya se encuentra registrada como estudiante!"

        nuevo_estudiante = Estudiante()
        nuevo_estudiante.info_persona = persona.id_persona
        nuevo_estudiante.login_estudiante = contrasenia

        estudiante_save = guardar_estudiante(nuevo_estudiante)

        return estudiante_save

    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def editar_login(rut, contrasenia_antigua, contrasenia_nueva):
    try:
        rut = rut.strip()
        contrasenia_antigua = contrasenia_antigua.strip()
        contrasenia_nueva = contrasenia_nueva.strip()

        persona = obtener_persona_rut(rut)

        if not persona:
            return "Persona no registrada!"

        estudiante_existe = Estudiante.get_or_none(Estudiante.info_persona == persona.id_persona)

        if not estudiante_existe:
            return "La persona no esta registrada como Estudiante!"

        contrasenia_antigua_valida = bcrypt.checkpw(
            contrasenia_antigua.encode('utf-8'),
            estudiante_existe.login_estudiante.encode('utf-8')
        )

        if contrasenia_antigua_valida:
            nuevo_hash = bcrypt.hashpw(contrasenia_nueva.encode('utf-8'), bcrypt.gensalt())
            estudiante_existe.login_estudiante = nuevo_hash.decode('utf-8')

            resultado = guardar_estudiante(estudiante_existe)
            return f"Contraseña Actualizada con Exito!: {resultado}"
        else:
            return "Contraseña Incorrecta"
    except Exception as error:
        return f"Ha ocurrido un error: {error}"

def lista_estudiantes():
    estudiantes = mostrar_estudiantes()

    if not estudiantes:
        return "No hay estudiantes"
    return estudiantes

def eliminar_estudiante(rut):
    try:
        rut = rut.strip()
        estudiante = obtener_estudiante_rut(rut)
        if not estudiante:
            print("Este estudiante no existe!")
        estudiante.habilitado = 0
        guardar_estudiante(estudiante)
        return "Estudiante Eliminado con Exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_estudiante(rut):
    try:
        rut = rut.strip()
        estudiante = obtener_estudiante_rut(rut)
        if not estudiante:
            print("Ese estudiante no existe!")
        estudiante.habilitado = 1
        guardar_estudiante(estudiante)
        return "Estudiante Activado con Exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")