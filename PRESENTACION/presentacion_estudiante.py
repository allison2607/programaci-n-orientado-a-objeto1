import maskpass
import bcrypt
from prettytable import PrettyTable
from datos.repositorios.repo_estudiantes import (obtener_estudiante_rut)
from datos.repositorios.repo_personas import (obtener_persona_rut)
from negocio.negocio_estudiante import (asignar_como_estudiante,
                                        editar_login,
                                        lista_estudiantes,
                                        eliminar_estudiante,
                                        activar_estudiante)
from auxiliar.aux_validacion import (validar_rut, validar_fecha,
                                     validar_contrasenia)

def menu_asignar_estudiante():
    print("[***" + "ASIGNAR PERSONA COMO ESTUDIANTE".center(80) + "***]")
    print()
    try:
        rut = contrasenia = ""
        while rut == "":
            rut_user = input("RUT de la Persona\nEj: 11.111.111-5: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("Formato de RUT Invalido!")
                rut = ""
        while contrasenia == "":
            print("Ingresar Contraseña!")
            print("Debe tener minimo 8 caracteres")
            print("Debe incluir al menos una letra minuscula y mayuscula")
            print("Debe incluir un numero")
            print("Debe incluir al menos un caracter especial")
            contrasenia_user = maskpass.askpass(prompt='Contraseña: ', mask='*')
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
            resultado = asignar_como_estudiante(rut, contrasenia_encriptada)

            if isinstance(resultado, str):
                print(f"Error: {resultado}")
            else:
                print(f"Rol de Estudiante asignado con exito a {persona.nombre}!")
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def menu_editar_login_e():
    print("[***" + "CAMBIAR CLAVE ESTUDIANTE".center(80) + "***]")
    print()
    try:
        rut = clave_antigua = clave_nueva = ""
        while rut == "":
            rut_user = input("Ingrese RUT del Estudiante\nEj: 11.111.111-1: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("Formato de RUT no valido!")
                rut = ""
        while clave_antigua == "":
            clave_antigua = maskpass.askpass(prompt="Contraseña Antigua: ", mask="*")
        while clave_nueva == "":
            clave_user = maskpass.askpass(prompt="Nueva Contraseña: ", mask="*")
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

def listado_estudiantes():
    resultado = lista_estudiantes()
    if not resultado:
        return "No hay estudiantes ingresados!"

    tabla = PrettyTable()
    tabla.field_names = ['ID', 'NOMBRE', 'APELLIDO',
                         'RUT', 'CELULAR', 'CORREO',
                         'DIRECCION', 'FECHA NACIMIENTO']

    for e in resultado:
        tabla.add_row([e.id_estudiante, e.info_persona.nombre,
                       e.info_persona.apellido, e.info_persona.rut,
                       e.info_persona.celular, e.info_persona.correo,
                       e.info_persona.direccion, e.info_persona.fecha_nacimiento])

    print(tabla)

def menu_eliminar_estudiante():
    print("[***" + "ELIMINAR INGRESO ESTUDIANTE".center(80) + "***]")
    print()
    rut = input("Ingrese el RUT del estudiante a eliminar\nEj: 11.111.111-1: ")
    valido = validar_rut(rut)
    if valido:
        resultado = eliminar_estudiante(rut)
        print(f"Eliminacion Exitosa!: {resultado}")
    else:
        print("Formato de RUT invalido! ")

def menu_activar_estudiante():
    print("[***" + "ACTIVAR INGRESO ESTUDIANTE".center(80) + "***]")
    print()
    rut = input("Ingrese el RUT del estudiante a Activar\nEj: 11.111.111-1: ")
    valido = validar_rut(rut)
    if valido:
        resultado = activar_estudiante(rut)
        print(f"Activacion Exitosa!: {resultado}")
    else:
        print("Formato de Rut Invalido! ")
