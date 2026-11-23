from DATOS.MODELOS.direccion import Direccion

def mostrar_direcciones(direccion:Direccion):
    try:
        direcciones = direccion.select().where(direccion.habilitado == 1)
        return direcciones
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_direccion_calle_numero(calle_direccion, numero_direccion):
    try:
        direccion = Direccion.get(Direccion.calle == calle_direccion, Direccion.numero == numero_direccion)
        return direccion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_direccion(direccion:Direccion):
    try:
        nueva_direccion = direccion.save()
        return nueva_direccion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

