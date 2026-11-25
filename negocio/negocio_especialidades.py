from datos.modelos.especialidad import Especialidad
from datos.repositorios.repo_especialidades import (mostrar_especialidades,
                                                    guardar_especialidad,
                                                    obtener_especialidad)

def crear_especialidad(especialidad):
    try:
        especialidad = especialidad.strip().title()
        if especialidad == "":
            return "Debes ingresar el nombre de la especialidad!"

        especialidad_existente = obtener_especialidad(especialidad)
        if especialidad_existente:
            return f"La especialidad '{especialidad}' ya esta registrada!"

        especialidad_nueva = Especialidad()
        especialidad_nueva.especialidad = especialidad
        nueva_especialidad = guardar_especialidad(especialidad_nueva)
        return nueva_especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def editar_especialidad(especialidad, especialidad_nueva):
    try:
        especialidad = especialidad.strip().capitalize()
        especialidad_nueva = especialidad_nueva.strip().title()

        if especialidad == "":
            return "Debes ingresar una especialidad!"

        especialidad_existente = obtener_especialidad(especialidad)
        if not especialidad_existente:
            return f"La especialidad '{especialidad}' no esta registrada!"

        especialidad_existente.especialidad = especialidad_nueva
        especialidad_editada = guardar_especialidad(especialidad_existente)
        return especialidad_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
        return None

def lista_especialidad():
    lista_especialidad = mostrar_especialidades()
    if lista_especialidad == 1:
        return lista_especialidad
    else:
        return "No hay especialidades ingresadas!"

def eliminar_especialidad(especialidad):
    try:
        especialidad = especialidad.strip().title()
        especialidad_eliminar = obtener_especialidad(especialidad)
        if not especialidad_eliminar:
            print("Esa especialidad no existe!")
        especialidad_eliminar.habilitado = 0
        guardar_especialidad(especialidad_eliminar)
        return f"La especialidad '{especialidad_eliminar.especialidad}' eliminada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def activar_especialidad(especialidad):
    try:
        especialidad = especialidad.strip().title()
        especialidad_activar = obtener_especialidad(especialidad)
        if not especialidad_activar:
            return f"La comuna '{especialidad_activar}' no existe!"
        especialidad_activar.habilitado = 1
        guardar_especialidad(especialidad_activar)
        return f"La especialidad '{especialidad}' activada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
