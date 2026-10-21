from DATOS.MODELOS.modulos import Modulos

def mostrar_modulos(modulo:Modulos):
    try:
        modulos = modulo.select().where(modulo.habilitado == 1)
        return modulos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_modulo(nombre_modulo):
    try:
        modulo = Modulos.get(Modulos.nombre_modulo == nombre_modulo)
        return modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_modulo(modulo:Modulos):
    try:
        nuevo_modulo = modulo.save()
        return nuevo_modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

