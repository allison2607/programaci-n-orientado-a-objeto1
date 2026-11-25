from prettytable import PrettyTable
from negocio.negocio_direccion import (crear_direccion,
                                       lista_direccion,
                                       eliminar_direccion,
                                       activar_direccion,
                                       editar_direccion)
from negocio.negocio_comuna import (obtener_comuna_nombre)
from negocio.negocio_pais import (obtener_pais_nombre)

def menu_crear_direccion():
    print("[***" + "INGRESAR UNA DIRECCION".center(80) + "***]")
    print()
    calle = input("Ingrese el nombre de la calle: ")
    numero = int(input("Ingrese el numero de la calle: "))
    comuna = input("Ingrese la comuna: ").strip().capitalize()
    pais = input("Ingrese el pais: ").strip().capitalize()

    resultado = crear_direccion(calle, numero,
                                comuna, pais)
    if isinstance(resultado, str):
        print(f"[Alerta de sistema!]: {resultado}")
    else:
        print("Direccion guardada con exito!")

def menu_editar_direccion():
    print("[***" + "EDITAR DIRECCION".center(80) + "***]")
    print()
    print("SI ALGUN DATO NO NECESITA CAMBIO MANTENER DATO VACIO")
    print()
    calle = input("Ingresa la calle a editar: ")
    numero = int(input("Ingresa el numero de la calle a editar: "))
    calle_nuevo = input("Ingrese nueva Calle: ").strip().capitalize()
    numero_nuevo = int(input("Ingrese nuevo numero: "))
    comuna_nueva = input("Ingrese nueva comuna: ").strip().capitalize()
    comuna = None
    if comuna_nueva != "":
        comuna = obtener_comuna_nombre(comuna_nueva)
        if not comuna:
            return f"La comuna '{comuna_nueva}' no existe"
    pais_nuevo = input("Ingrese nuevo pais: ").strip().capitalize()
    pais = None
    if pais_nuevo != "":
        pais = obtener_pais_nombre(pais_nuevo)
        if not pais:
            return f"El pais '{pais_nuevo}' no existe"
    resultado = editar_direccion(calle, numero, calle_nuevo, numero_nuevo, comuna_nueva, pais_nuevo)

    if isinstance(resultado, str):
        print(f"[Alerta de sistema!]: {resultado}")
    elif resultado:
        print("Direccion Actualizada!")
    else: 
        print("Ocurrio un error al actualizar la direccion.")
        
def listado_direcciones():
    resultado = lista_direccion()
    if not resultado:
        print("No hay direcciones ingresadas!")
        return
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'CALLE', 'NUMERO',
                         'COMUNA', 'PAIS']
    for d in resultado:
        tabla.add_row([d.id_direcciones, d.calle,
                       d.numero, d.comuna, d.pais])
    print(tabla)

def menu_eliminar_direccion():
    print("[***" + "ELIMINAR DIRECCION".center(80) + "***]")
    print()
    calle = input("Ingrese el nombre de la Calle: ")
    numero = int(input("Ingrese el numero de la Calle: "))
    resultado = eliminar_direccion(calle, numero)
    print(f"Elinacion exitosa!: {resultado}")

def menu_activar_direccion():
    print("[***" + "ACTIVAR DIRECCION".center(80) + "***]")
    print()
    calle = input("Ingrese el nombre de la Calle: ")
    numero = int(input("Ingrese el numero de la Calle: "))
    resultado = activar_direccion(calle, numero)
    print(f"Activacion exitosa!: {resultado}")