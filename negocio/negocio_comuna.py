from prettytable import PrettyTable
from datos.modelos.comuna import Comuna
from datos.repositorios.repo_comunas import (mostrar_comunas,
                                             obtener_comuna_nombre,
                                             guardar_comuna)

def crear_comuna(nombre):
    try:
        nombre = nombre.strip().title()
        if nombre == "":
            return "Debes ingresar una comuna!"

        comuna_existente = obtener_comuna_nombre(nombre)
        if comuna_existente:
            return f"La comuna '{nombre}' ya esta registrada!"
       
        comuna = Comuna()
        comuna.comuna = nombre
        nueva_comuna = guardar_comuna(comuna)
        return nueva_comuna

    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def editar_comuna(nombre, nombre_nuevo):
    try:
        nombre = nombre.strip().title()
        nombre_nuevo.strip().title()
        if nombre == "":
            return "Debes ingresar una comuna!"
        comuna_existente = obtener_comuna_nombre(nombre)
        if not comuna_existente:
            return f"La comuna '{nombre}' no esta registrada!"
        comuna_existente.comuna = nombre_nuevo
        comuna_editada = guardar_comuna(comuna_existente)
        return comuna_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def lista_comunas():
    lista_comunas = mostrar_comunas()
    if lista_comunas == 1:
        return lista_comunas
    else:
        return "No hay comunas ingresadas!"

def eliminar_comuna(nombre):
    try:
        nombre = nombre.strip().title()
        comuna = obtener_comuna_nombre(nombre)
        if not comuna:
            print("Esa comuna no existe!")
        comuna.habilitado = 0
        guardar_comuna(comuna)
        return f"Comuna '{comuna.comuna}' eliminada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_comuna(nombre):
    try:
        nombre = nombre.strip().title()
        comuna = obtener_comuna_nombre(nombre)
        if not comuna:
            return f"La comuna '{nombre}' no existe!"
        comuna.habilitado = 1
        guardar_comuna(comuna)
        return f"La comuna '{nombre}' activada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")


    