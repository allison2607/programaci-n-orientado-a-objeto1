from prettytable import PrettyTable
from datos.modelos.direccion import Direccion
from datos.repositorios.repo_direcciones import (mostrar_direcciones,
                                                 obtener_direccion_calle_numero,
                                                 guardar_direccion)
from datos.repositorios.repo_comunas import (obtener_comuna_nombre)
from datos.repositorios.repo_paises import (obtener_pais_nombre)

def crear_direccion(calle, numero,
                    comuna, pais):
   try:
        calle = calle.strip().title()
        comuna = comuna.strip().title()
        if calle == "":
            return "Debes ingresar una calle!"
        elif numero == "":
            return "Debes ingresar un numero de calle!"
        elif comuna == "":
                return "Debes ingresar una comuna!"
        elif pais == "":
                    return "Debes ingresar un pais!"

        direccion_existente = obtener_direccion_calle_numero(calle, numero)
        if direccion_existente:
            return f"La direccion '{calle}, {numero}' ya esta registrada!"
        
        id_comuna = obtener_comuna_nombre(comuna)
        if not id_comuna:
              return print(f"La comuna {id_comuna} aun no esta ingresada!")
        direccion = Direccion()
        direccion.comuna = id_comuna.id_comuna
        
        id_pais = obtener_pais_nombre(pais)
        if not id_pais:
              return print(f"El pais {id_pais} aun no esta registrado!")
        direccion.pais = id_pais.id_pais
        direccion.calle = calle
        direccion.numero = numero
        nueva_direccion = guardar_direccion(direccion)
        return nueva_direccion
   except Exception as error:
       print(f"Ha ocurrido un error!: {error}")
       return None

def editar_direccion(calle, numero, calle_nueva, numero_nuevo, comuna_nueva=None, pais_nuevo=None):
      try:
            calle = calle.strip().title()
            calle_nueva = calle_nueva.strip().title()
            comuna_nueva = comuna_nueva.strip().title()
            pais_nuevo = pais_nuevo.strip().title()
            if calle == "" or numero == "":
                  return "Debes ingresar la calle y numero a editar!"
            direccion_existente = obtener_direccion_calle_numero(calle, numero)
            if not direccion_existente:
                  return f"La direccion '{calle}, {numero}' no esta registrada!"
            if calle_nueva != "":
                  direccion_existente.calle = calle_nueva
            if numero_nuevo != "":
                  direccion_existente.numero = numero_nuevo
            if comuna_nueva:
                  comuna = obtener_comuna_nombre(comuna_nueva)
                  direccion_existente.comuna = comuna.id_comuna
            if pais_nuevo:
                  pais = obtener_pais_nombre(pais_nuevo)
                  direccion_existente.pais = pais.id_pais
            direccion_editada  = guardar_direccion(direccion_existente)
            return direccion_editada
      except Exception as error:
            print(f"Ha ocurrido un error!: {error}")
            return None


def lista_direccion():
      lista_direccion = mostrar_direcciones()
      if lista_direccion == 1:
            return lista_direccion
      else:
            return "No hay direcciones ingresadas!"

def eliminar_direccion(calle, numero):
      try:
            calle = calle.strip().title()
            direccion = obtener_direccion_calle_numero(calle, numero)
            if not direccion:
                  print("Esa direccion no existe!")

            direccion.habilitado = 0
            guardar_direccion(direccion)
            return "Direccion eliminada con exito!"
      except Exception as error:
            print(f"Ha ocurrido un error!: {error}")

def activar_direccion(calle, numero):
      try:
            calle = calle.strip().title()
            direccion = obtener_direccion_calle_numero(calle, numero)
            if not direccion:
                  print("Esa direccion no esta ingresada!")
            direccion.habilitado = 1
            guardar_direccion(direccion)
            return "Direccion Activada con exito!"
      except Exception as error:
            print(f"Ha ocurrido un error!: {error}")
            