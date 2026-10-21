from DATOS.MODELOS.contenidos import Contenidos

def mostrar_contenidos(contenido:Contenidos):
    try:
        contenidos = contenido.select().where(contenido.habilitado == 1)
        return contenidos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_contenido_modulo(modulo):
    try:
        contenido_modulo = Contenidos.get(Contenidos.modulo == modulo)
        return contenido_modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_contenido(contenido:Contenidos):
    try:
        contenido_nuevo = contenido.save()
        return contenido_nuevo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

