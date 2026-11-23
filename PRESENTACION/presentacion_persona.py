from prettytable import PrettyTable
from auxiliar.aux_validacion import (validar_correo,
                                     validar_fecha,
                                     validar_rut)
from negocio.negocio_persona import (crear_persona,
                                     editar_persona,
                                     lista_persona,
                                     eliminar_persona,
                                     activar_persona)

def menu_crear_persona():
    try:
        nombre = apellido = rut = celular = correo = calle = numero = comuna = pais = fecha = ""
        print("[***" + "INGRESAR DATOS DE PERSONA".center(80) + "***]")
        print()
        while nombre == "":   
            nombre = input("Nombre: ")
        while apellido == "":
            apellido = input("Apellido: ")
        while rut == "":
            rut_user = input("RUT\nEj 11.111.111-1: ")
            valido = validar_rut(rut_user)
            if valido:
                rut = rut_user
            else:
                print("Formato de RUT no valido!")
        while celular == "":
            celular = input("Celular: ")
        while correo == "":
            correo_user = input("Correo: ")
            valido = validar_correo(correo_user)
            if valido:
                correo = correo_user
            else: 
                print("Formato de Correo Invalido!")
        while calle == "":        
            calle = input("Calle: ")
        while numero == "":
            numero = int(input("Numero de Calle: "))
        while comuna == "":
            comuna = input("Comuna: ")
        while pais == "":
            pais = input("Pais: ")
        while fecha == "":
            fecha_user = input("Fecha Nacimiento\nEj: 2001-08-29: ")
            valido = validar_fecha(fecha_user)
            if valido:
                fecha = fecha_user
            else:
                print("Formato de Fecha Invalido!")
        resultado= crear_persona(nombre, apellido,
                                rut, celular,
                                correo, calle,
                                numero, comuna,
                                pais, fecha)
        if isinstance(resultado, str):
            print(f"[Alerta de Sistema!]: {resultado}")
        else:
            print("Persona Guardada con Exito!")
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def menu_editar_persona():
        try:
            print("[***" + "EDITAR DATOS DE PERSONA".center(80) + "***]")
            print()
            print("SI ALGUN DATO NO NECESITA CAMBIO MANTENER DATO VACIO")
            print()
            rut = input("Ingrese el rut de la persona a editar\nEj: 11.111.111-1: ")
            nombre = input("Ingrese nuevo nombre: ")
            apellido = input("Ingrese nuevo apellido: ")
            celular = input("Ingrese nuevo celular: ")
            correo = input("Ingrese nuevo correo: ")
            calle = input("Ingrese nueva calle: ")
            numero = (input("Ingrese nuevo numero de calle: "))
            comuna = input("Ingrese nueva comuna: ")
            pais = input("Ingrese nuevo pais: ")
            fecha = input("Ingrese nueva fecha de nacimiento\nEj: 2001-08-29: ")

            resultado = editar_persona(nombre, apellido,
                                    rut, celular,
                                    correo, calle,
                                    numero, comuna,
                                    pais, fecha)
            if isinstance(resultado, str):
                print(f"[Alerta de Sistema!]: {resultado}")
            else: 
                print("Persona Editada Con exito!")
        except Exception as error:
            print(f"Ha ocurrido un error!: {error}")

def listado_personas():
    resultado = lista_persona()
    if not resultado:
        print("No hay personas ingresadas!")
        return
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'NOMBRE', 'APELLIDO',
                         'RUT', 'CELULAR', 'CORREO',
                         'DIRECCION','NUMERO', 'FECHA NACIMIENTO']
    for p in resultado:
        tabla.add_row([p.id_persona, p.nombre, p.apellido,
                       p.rut, p.celular, p.correo,
                       p.direccion.calle, p.direccion.numero , p.fecha_nacimiento])
    print(tabla)

def menu_eliminar_persona():
    print("[***" + "ELIMINAR INGRESO PERSONA".center(80) + "***]")
    print()
    rut = input("Ingrese el rut de la persona a eliminar: ")
    resultado = eliminar_persona(rut)
    print(f"Eliminacion exitosa!: {resultado}")

def menu_activar_persona():
    print("[***" + "ACTIVAR INGRESO PERSONA".center(80) + "***]")
    print()
    rut = input("Ingrese el rut de la persona a activar: ")
    resultado = activar_persona(rut)
    print(f"Activacion exitosa!: {resultado}")