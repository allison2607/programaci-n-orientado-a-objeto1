from prettytable import PrettyTable
from datos.modelos.pais import Pais
from datos.repositorios.repo_paises import (mostrar_paises,
                                            obtener_pais_nombre,
                                            guardar_pais)

def crear_pais(nombre):
    try:
        nombre = nombre.strip().title()
        if nombre == "":
            return "Debes ingresar un pais!"

        pais_existente = obtener_pais_nombre(nombre)
        if pais_existente:
            return f"El pais '{nombre}' ya esta registrada!"

        pais = Pais()
        pais.pais = nombre
        nuevo_pais = guardar_pais(pais)
        return nuevo_pais

    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def editar_pais(nombre, nombre_nuevo):
    try:
        nombre = nombre.strip().title()
        nombre_nuevo = nombre_nuevo.strip().title()
        if nombre == "":
            return "Debes ingresar un pais!"
        if nombre_nuevo == "":
            return "Debes ingresar el nuevo nombre!"
        pais_existente = obtener_pais_nombre(nombre)
        if not pais_existente:
            return f"El pais '{nombre}' no esta registrado!"
        pais_existente.pais = nombre_nuevo
        pais_editado = guardar_pais(pais_existente)
        return pais_editado
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def lista_paises():
    lista_paises = mostrar_paises()
    if lista_paises == 1:
        return lista_paises
    else:
        return "No hay paises ingresados!"

def eliminar_pais(nombre):
    try:
        nombre = nombre.strip().title()
        pais = obtener_pais_nombre(nombre)
        if not pais:
            print("Ese pais no existe!")
        pais.habilitado = 0
        guardar_pais(pais)
        return f"Pais '{pais.pais}' eliminado con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_pais(nombre):
    try:
        nombre = nombre.strip().title()
        pais = obtener_pais_nombre(nombre)
        if not pais:
            print("Ese pais no esta registrado!")
        pais.habilitado = 1
        guardar_pais(pais)
        return f"Pais '{pais}' ha sido activado con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")


    

