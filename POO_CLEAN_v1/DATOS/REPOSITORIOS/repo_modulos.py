from DATOS.MODELOS.modulo import Modulo

def mostrar_modulos(modulo:Modulo):
    try:
        modulos = modulo.select().where(modulo.habilitado == 1)
        return modulos
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_modulo(nombre_modulo):
    try:
        modulo = Modulo.get(Modulo.nombre_modulo == nombre_modulo)
        return modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_modulo(modulo:Modulo):
    try:
        nuevo_modulo = modulo.save()
        return nuevo_modulo
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

