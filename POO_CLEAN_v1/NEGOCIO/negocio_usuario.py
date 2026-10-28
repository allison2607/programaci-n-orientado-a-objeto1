from DATOS.REPOSITORIOS.repo_usuarios import (mostrar_usuario, 
                                              obtener_usuario_nombre,
                                              guardar_usuario)
from DATOS.REPOSITORIOS.repo_direcciones import (mostrar_direcciones,
                                                 obtener_direccion_calle_numero,
                                                 guardar_direccion)
from DATOS.REPOSITORIOS.repo_comunas import (mostrar_comunas,
                                             obtener_comuna_nombre,
                                             guardar_comuna)
from DATOS.REPOSITORIOS.repo_paises import (mostrar_paises,
                                            obtener_pais_nombre,
                                            guardar_pais)
from DATOS.MODELOS.persona import Persona
from DATOS.MODELOS.direccion import Direccion
from DATOS.MODELOS.comuna import Comuna
from DATOS.MODELOS.pais import Pais


def crear_usuario(usuario:Usuario,
                  direccion:Direccion,
                  comunas:Comuna,
                  paises:Pais,
                  nombre,
                  rut, 
                  apellido,
                  celular,
                  correo,
                  fecha_nacimiento,
                  calle,
                  comuna,
                  numero, 
                  pais):
    try:
        if nombre == "":
            return "La usuarios debe tener nombre!"
        else:
            usuarios.nombre = nombre
        if rut == "":
            return "La usuarios debe tener RUT!"
        else:
            usuarios.rut = rut
        if apellido == "":
            return "La usuarios debe tener apellido!"
        else:
            usuarios.apellido = apellido
        if celular == "":
            return "La usuarios debe tener celular asociado!"
        else:
            usuarios.celular = celular
        if correo == "":
            return "La usuarios debe tener correo asociado!"
        else:
            usuarios.correo = correo
        if fecha_nacimiento == "":
            return "La usuarios debe tener fecha de nacimiento!" 
        else:
            usuarios.fecha_nacimiento = fecha_nacimiento
        if calle == "":
            return "La usuarios debe tener una calle!"
        else:
            direccion.calle = calle
        if comuna == "":
            return "La usuarios debe tener una comuna!"
        else:
            comunas.comuna = comuna
        if numero == "":
            return "La calle debe tener numero!"
        else:
            direccion.numero = numero
        if pais == "":
            return "La usuarios debe tener un pais!"
        else:
            paises.pais = pais

        nuevo_pais = guardar_pais(paises)
        nueva_comuna = guardar_comuna(comunas)
        direccion.comuna = nueva_comuna
        direccion.pais = nuevo_pais
        nueva_direccion = guardar_direccion(direccion)
        usuarios.direccion = nueva_direccion
        nueva_usuarios_exito = guardar_usuarios(usuarios)
        return nueva_usuarios_exito

    
    except Exception as error:
        print(f"Error al guardar la usuarios!: {error}")     

def lista_usuarioss():
    lista_usuarios = mostrar_usuarios()
    if lista_usuarios == 1:
        return lista_usuarios
    else:
        return "No hay usuarioss ingresadas!" 

def editar_usuarios(rut, nombre,
                   apellido, celular,
                   correo, fecha_nacimiento,
                   calle, comuna,
                   numero, pais):
    try:
        usuarios = obtener_usuarios_rut(rut)
        if not usuarios:
            print("usuarios no encontrada")
        usuarios.nombre = nombre
        usuarios.apellido = apellido
        usuarios.celular = celular
        usuarios.correo = correo
        usuarios.fecha_nacimiento = fecha_nacimiento
        usuarios.calle = calle
        usuarios.comuna = comuna
        usuarios.numero = numero
        usuarios.pais = pais

        guardar_usuarios(usuarios)
        return "usuarios actualizada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def eliminar_usuarios(rut):
    try:
        usuarios = obtener_usuarios_rut(rut)
        if not usuarios:
            print("Esa usuarios no existe!")

        usuarios.habilitado = 0
        guardar_usuarios(usuarios)
        return "usuarios Eliminada con exito!"
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
