from DATOS.MODELOS.contenidos import Contenido

def mostrar_contenidos(contenido:Contenido):
    try:
        contenidos = contenido.select().where(contenido.habilitado == 1)
        return contenidos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_contenido_modulo(modulo):
    try:
        contenido_modulo = Contenido.get(Contenido.modulo == modulo)
        return contenido_modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_contenido(contenido:Contenido):
    try:
        contenido_nuevo = contenido.save()
        return contenido_nuevo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

