import bcrypt 
from datos.modelos.instructor import Instructor
from datos.repositorios.repo_instructores import (mostrar_instructores,
                                                  obtener_instructor_rut,
                                                  guardar_instructor)
from datos.repositorios.repo_personas import (obtener_persona_rut)

def asignar_como_instructor(rut, fecha_contratacion,
                            contrasenia):
    try:
        rut = rut.strip()
        contrasenia = contrasenia.strip()

        persona = obtener_persona_rut(rut)

        if not persona:
            return "Persona no Registrada!"


        instructor_existente = Instructor.get_or_none(Instructor.info_persona == persona.id_persona)
        if instructor_existente:
            return f"La persona con RUT {rut} ya se encuentra registrada como instructor!"

        nuevo_instructor = Instructor()
        nuevo_instructor.info_persona = persona.id_persona
        nuevo_instructor.fecha_contratacion = fecha_contratacion
        nuevo_instructor.login_instructor = contrasenia

        instructor_save = guardar_instructor(nuevo_instructor)

        return instructor_save
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"
    
def editar_login(rut, contrasenia_antigua, contrasenia_nueva):
    try:
        rut = rut.strip()
        contrasenia_antigua = contrasenia_antigua.strip()
        contrasenia_nueva = contrasenia_nueva.strip()

        persona = obtener_persona_rut(rut)

        if not persona:
            return "Persona no Registrada!"

        instructor_existente = Instructor.get_or_none(Instructor.info_persona == persona.id_persona)

        if not instructor_existente:
            return "La persona no esta registrada como Instructor!"

        contrania_antigua_valida = bcrypt.checkpw(
            contrasenia_antigua.encode('utf-8'),
            instructor_existente.login_instructor.encode('utf-8')
        )

        if contrania_antigua_valida:
            nuevo_hash = bcrypt.hashpw(contrasenia_nueva.encode('utf-8'), bcrypt.gensalt())
            instructor_existente.login_instructor = nuevo_hash.decode('utf-8')

            resultado = guardar_instructor(instructor_existente)
            return f"Contraseña Actualizada con Exito!: {resultado}"
        else:
            return "Contraseña Incorrecta"
    except Exception as error:
        return f"Ha ocurrido un error: {error}"

def lista_instructores():
    instructores = mostrar_instructores()

    if not instructores:
        return "No hay instructores Registrados!"
    return instructores

def eliminar_instructor(rut):
    try:
        rut = rut.strip()
        instructor = obtener_instructor_rut(rut)
        if not instructor:
            print("Ese instructor no existe!")
        instructor.habilitado = 0
        guardar_instructor(instructor)
        return "Instructor eliminado con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_instructor(rut):
    try:
        rut = rut.strip()
        instructor = obtener_instructor_rut(rut)
        if not instructor:
            print("Ese instructor no existe!")
        instructor.habilitado = 1
        guardar_instructor(instructor)
        return "Instructor Activado con Exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")