from DATOS.MODELOS.direcciones import Direcciones

def mostrar_direcciones(direccion:Direcciones):
    try:
        direcciones = direccion.select().where(direccion.habilitado == 1)
        return direcciones
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_direccion(direccion:Direcciones):
    try:
        nueva_direccion = direccion.save
        return nueva_direccion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def editar_direecion(direccion:Direcciones):
    try:
        direccion_editada = direccion.ssave
        return direccion_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def deshabilitar_direccion(direccion:Direcciones):
    try:
        direccion.habilitado = 0
        direccion.save()
        return direccion
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
