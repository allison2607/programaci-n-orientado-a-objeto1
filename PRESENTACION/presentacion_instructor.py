import maskpass
import bcrypt
from prettytable import PrettyTable
from datos.repositorios.repo_instructores import (obtener_instructor_rut)
from negocio.negocio_instructor import (asignar_como_instructor,
                                        editar_login,
                                        lista_instructores,
                                        eliminar_instructor,
                                        activar_instructor)
from datos.repositorios.repo_personas import (obtener_persona_rut)
from auxiliar.aux_validacion import (validar_rut, validar_fecha,
                                     validar_contrasenia)


def menu_asignar_instructor():
    print("[***" + "ASIGNAR PERSONA COMO INSTRUCTOR".center(80) + "***]")
    print()
    try:
        rut = fecha = contrasenia = ""
        while rut == "":
            rut_user = input("RUT de la Persona\nEj: 11.111.111-5: ")
            valido = validar_rut(rut_user)
            if valido: 
                rut = rut_user
            else: 
                print("Formato de RUT Invalido!")
                rut = ""
        while fecha == "":
            fecha_user = input("Fecha de Contratacion\nEj AAAA-MM-DD: ")
            valido = validar_fecha(fecha_user)
            if valido:
                fecha = fecha_user
            else:
                print("Formato de Fecha no valido!")
                fecha = ""
        while contrasenia == "":
            print("Ingresar Contraseña!")
            print("Debe tener minimo 8 caracteres")
            print("Debe incluir al menos una letra minuscula y mayuscula")
            print("Debe incluir un numero")
            print("Debe incluir al menos un caracter especial")
            contrasenia_user = maskpass.askpass(prompt="Contraseeña: ", mask="*")
            valido, errores = validar_contrasenia(contrasenia_user)
            if valido:
                print("Contraseña Creada con Exito!")
                contrasenia = contrasenia_user
                contrasenia_hash = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())
                contrasenia_encriptada = contrasenia_hash.decode('utf-8')
            else: 
                print("Contraseña no Segura!")
                for error in errores:
                    print(f"- {error}")
                print()
        persona = obtener_persona_rut(rut)
        resultado = asignar_como_instructor(rut, fecha, contrasenia_encriptada)

        if isinstance(resultado, str):
            print(f"Error: {resultado}")
        else:
            print(f"Rol de Instructor Asignado con exito a {persona.nombre}!")
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")        

def menu_editar_login():
    print("[***" + "CAMBIAR CLAVE INSTRUCTORES" + "***]")
    print()
    try:
        rut = clave_antigua = clave_nueva = ""
        while rut == "":
            rut_user = input("Ingrese RUT del Instructor\nEj: 11.111.111-1: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("Formato de RUT no valido!")
                rut = ""
        while clave_antigua == "":
            clave_antigua = maskpass.askpass(prompt="Contraseña Antigua: ", mask='*')
        while clave_nueva == "":
            clave_user = maskpass.askpass(prompt="Contraseña Nueva: ", mask='*')
            valido, errores = validar_contrasenia(clave_user)
            if valido:
                clave_nueva = clave_user
            else:
                print("Contraseña no Segura!")
                for error in errores:
                    print(f"- {error}")
                print()
        resultado = editar_login(rut, clave_antigua, clave_nueva)

        print(f"{resultado}")
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def listado_instructores():
    resultado = lista_instructores()
    if not resultado:
        print("No hay instructores ingresados!")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID', 'NOMBRE', 'APELLIDO',
                         'RUT', 'CELULAR', 'CORREO',
                         'DIRECCION', 'FECHA NACIMIENTO']
    for i in resultado:
        tabla.add_row([i.id_instructor, i.info_persona.nombre,
                       i.info_persona.apellido, i.info_persona.rut,
                       i.info_persona.celular, i.info_persona.correo,
                       i.info_persona.direccion, i.info_persona.fecha_nacimiento])
    print(tabla)

def menu_eliminar_instructor():
    print("[***" + "ELIMINAR INGRESO INSTRUCTOR" + "***]")
    print()
    rut = input("Ingrese el rut del instructor a eliminar\nEj 11.111.111-1: ")
    valido = validar_rut(rut)
    if valido: 
       resultado = eliminar_instructor(rut)
       print(f"Eliminacion exitosa!: {resultado}")
    else:
        print("Formato de rut Invalido! ")

def menu_activar_instructor():
    print("[***" + "ACTIVAR INGRESO INSTRUCTOR" + "***]")
    print()
    rut = input("Ingrese el rut de instructor a activar\nEj: 11.111.111-1: ")
    valido = validar_rut(rut)
    if valido:
        resultado = activar_instructor(rut)
        print(f"Activacion Exitosa!: {resultado}")
    else:
        print("Formtado de rut Invalido! ")
