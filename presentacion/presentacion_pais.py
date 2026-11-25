from prettytable import PrettyTable
from datos.modelos.pais import Pais
from negocio.negocio_pais import (crear_pais,
                                  lista_paises,
                                  eliminar_pais,
                                  editar_pais,
                                  activar_pais)

def menu_crear_pais():
    print("[***" + "INGRESA EL PAIS A CREAR".center(80) + "***]")
    print()
    nombre = input("Ingresa el nombre del pais\n"
                   ).strip().capitalize()

    resultado = crear_pais(nombre)
    if isinstance(resultado, str):
        print(f"[Alerta de sistema!]: {resultado}")
    else:
        print("Pais guardado con exito!")

def menu_editar_pais():
    print("[***" + "EDITAR PAIS".center(80) + "***]")
    print()
    nombre = input("Ingresa el nombre del pais: ")
    nombre_nuevo = input("Ingresa el nuevo nombre: ")
    resultado = editar_pais(nombre, nombre_nuevo)
    if isinstance(resultado, str):
        print(f"[Alerta de sistema!]: {resultado}")
    else:
        print("Pais editado con exito!")

def listado_paises():
    resultado = lista_paises()
    if not resultado:
        print("No hay paises ingresados!")
        return
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'PAIS']
    for p in resultado:
        tabla.add_row([p.id_pais, p.pais])
    print(tabla)

def menu_eliminar_pais():
    print("[***" + "ELIMINAR PAIS".center(80) + "***]")
    print()
    nombre = input("Ingrese el nombre del pais a eliminar: ")
    resultado = eliminar_pais(nombre)
    print(f"Eliminacion exitosa!: {resultado}")

def menu_activar_pais():
    print("[***" + "ACTIVAR PAIS".center(80) + "***]")
    print()
    nombre = input("Ingrese el nombre del pais a activar: ")
    resultado = activar_pais(nombre)
    print(f"Activacion exitosa!: {resultado}")