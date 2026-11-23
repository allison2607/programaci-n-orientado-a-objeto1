from prettytable import PrettyTable
from datos.modelos.comuna import Comuna
from negocio.negocio_comuna import (crear_comuna,
                                    lista_comunas,
                                    eliminar_comuna,
                                    editar_comuna,
                                    activar_comuna)

def menu_crear_comuna():
    print("[***" + "INGRESAR COMUNA".center(80) + "***]")
    print()
    nombre = input("Ingresa el nombre de la comuna\n"
                   ).strip().capitalize()

    resultado = crear_comuna(nombre)
    if isinstance(resultado, str):
        print(f"[Alerta del Sistemma!]: {resultado}")
    else:
        print("Comuna guardada con exito!")

def listado_comunas():
    resultado = lista_comunas()
    if not resultado:
        print("No hay comunas ingresadas!")
        return
    tabla = PrettyTable()
    tabla.field_names = ["ID", "COMUNA"]
    for c in resultado:
        tabla.add_row([c.id_comuna, c.comuna])
    print(tabla)

def menu_eliminar_comuna():
    print("[***" + "ELIMINAR COMUNA".center(80) + "***]")
    print()
    nombre = input("Ingrese el nombre de la comuna a eliminar: ")
    resultado = eliminar_comuna(nombre)
    print(f"Eliminacion exitosa!: {resultado}")

def menu_activar_comuna():
    print("[***" + "ACTIVAR COMUNA".center(80) + "***]")
    print()
    nombre = input("Ingrese el nombre de la comuna a activar: ").strip().capitalize()
    resultado = activar_comuna(nombre)
    print(f"Activacion exitosa!: {resultado}")

def menu_editar_comuna():
    print("[***" + "INGRESA LA COMUNA A EDITAR".center(80) + "***]")
    print()
    nombre = input("Ingresa el nombre de la comuna: ").strip().capitalize()
    nombre_nuevo = input("Ingresa el nuevo nombre de la comuna: ").strip().capitalize()
    resultado = editar_comuna(nombre, nombre_nuevo)
    print(f"Edicion exitosa!: {resultado}")