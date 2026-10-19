from DATOS.MODELOS.comunas import Comunas

def mostrar_comunas(comuna:Comunas):
    try:
        comunas = comuna.select().where(Comunas.habilitado == 1)
        return comunas
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def guardar_comuna(comuna:Comunas):
    try:
        nueva_comuna = comuna.save()
        return nueva_comuna
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def editar_comuna(comuna:Comunas):
    try:
        comuna_editada = comuna.save()
        return comuna_editada
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def deshabilitar_comuna(comuna:Comunas):
    try:
        comuna.habilitado = 0
        comuna.save()
        return comuna
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")


