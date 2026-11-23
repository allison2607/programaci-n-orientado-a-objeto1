from prettytable import PrettyTable
from negocio.negocio_especialidades import (crear_especialidad,
                                            lista_especialidad,
                                            eliminar_especialidad,
                                            editar_especialidad,
                                            activar_especialidad)

def menu_crear_especialidad():
    print("[***" + "INGRESAR ESPECIALIDAD".center(80) + "***]")
    print()
    especialidad = input("Ingresa el titulo de la especialidad: ")

    resultado = crear_especialidad(especialidad)

    if isinstance(resultado, str):
        print(f"[Alerta de Sistema!]: {resultado}")
    else:
        print("Especialidad ingresada con exito!")

def menu_editar_especialidad():
    print("[***" + "EDITAR ESPECIALIDAD".center(80) + "***]")
    print()
    especialidad = input("Ingresa el titulo de la especialidad: ")
    especialidad_nueva = input("Ingresa el nuevo titulo de especialidad: ")
    resultado = editar_especialidad(especialidad, especialidad_nueva)
    print(f"Edicion exitosa!: {resultado}")

def listado_especialidades():
    resultado = lista_especialidad()
    if not resultado:
        print("No hay especialidades ingresadas!")
        return
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'ESPECIALIDAD']
    for e in resultado:
        tabla.add_row([e.id_especialidad, e.especialidad])
    print(tabla)

def menu_eliminar_especialidad():
    print("[***" + "ELIMINAR ESPECIALIDAD".center(80) + "***]")
    print()
    especialidad = input("Ingrese el titulo de la especialidad a eliminar: ")
    resultado = eliminar_especialidad(especialidad)
    print(f"Eliminacion exitosa!: {resultado}")

def menu_activar_especialidad():
    print("[***" + "ACTIVAR ESPECIALIDAD".center(80) + "***]")
    print()
    especialidad = input("Ingrese el titulo de la especialidad a activar: ")
    resultado = activar_especialidad(especialidad)
    print(f"Activacion exitosa!: {resultado}")