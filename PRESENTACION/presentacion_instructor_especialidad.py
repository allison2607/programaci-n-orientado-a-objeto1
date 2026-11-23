from prettytable import PrettyTable
from datos.repositorios.repo_instructores import obtener_instructor_rut
from auxiliar.aux_validacion import (validar_rut)
from negocio.negocio_instructores_especialidad import (asignar_especialidad_instructor,
                                                       lista_especialidades_instructores,
                                                       editar_especialidad,
                                                       eliminar_especialidad_instructor,
                                                       activar_especialidad_instructor)

def menu_asignar_especialidad_instructor():
    try:
        print("[***" + "[ASIGNAR ESPECIALIDAD A INSTRUCTOR]" + "***]")
        print()
        rut = especialidad = ""
        while rut == "":
            rut_user = input("Ingresa RUT del Instructor: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else: 
                print("RUT Invalido!")
                rut == ""
        while especialidad == "":
            especialidad_user = input("Ingresa la Especialidad a Asignar: ")
            especialidad = especialidad_user

        instructor = obtener_instructor_rut(rut)
        resultado = asignar_especialidad_instructor(rut, especialidad)

        if isinstance(resultado, str):
            print(f"[Alerta de Sistema!]: {resultado}")
        else:
            print(f"Especialidad '{especialidad}' asignada con exito a {instructor.info_persona.nombre}")
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def listado_especialidades_instructores():
    resultado = lista_especialidades_instructores()
    if not resultado:
        return "No hay especialidades asignadas!"
    
    tabla = PrettyTable()
    tabla.field_names = ['NOMBRE', 'APELLIDO', 'ESPECIALIDAD']

    for e in resultado:
       tabla.add_row([
          e.instructor.info_persona.nombre,
          e.instructor.info_persona.apellido,
          e.especialidad.especialidad
       ])

    print(tabla)

def menu_editar_asociacion():
    try:
        print("[***" + "[EDITAR ESPECIALIDAD]".center(80) + "***]")
        rut = especialidad = nueva_especialidad = ""
        while rut == "":
            rut_user = input("Ingrese el RUT: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("RUT No valido!")
                rut = ""

        while especialidad == "":
            especialidad_user = input("Especialidad: ")
            especialidad = especialidad_user

        while nueva_especialidad == "":
            especialidad_n_user = input("Nueva Especialidad: ")
            nueva_especialidad = especialidad_n_user

        resultado = editar_especialidad(rut, especialidad, nueva_especialidad)
        return resultado
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def menu_eliminar_asociacion():
    try:
        print("[***" + "ELIMINAR ASOCIACION" + "***]")
        print()
        rut = especialidad = ""
        while rut == "":
            rut_user = input("Ingrese RUT: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("RUT Invalido!")
                rut = ""
        while especialidad == "":
            especialidad_user = input("Especialidad: ")
            especialidad = especialidad_user

        resultado = eliminar_especialidad_instructor(rut, especialidad)
        return print(resultado)
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def menu_activar_asociacion():
    try:
        print("[***" + "ACTIVAR ASOCIACION" + "***]")
        print()
        rut = especialidad = ""
        while rut == "":
            rut_user = input("Ingrese RUT: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("RUT Invalido!")
                rut = ""
        while especialidad == "":
            especialidad_user = input("Especialidad: ")
            especialidad = especialidad_user

        resultado = activar_especialidad_instructor(rut, especialidad)
        return print(resultado)
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"