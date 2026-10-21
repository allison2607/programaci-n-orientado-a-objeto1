from DATOS.MODELOS.comunas import Comunas

def mostrar_comunas(comuna:Comunas):
    try:
        comunas = comuna.select().where(Comunas.habilitado == 1)
        return comunas
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def obtener_comuna_nombre(nombre_comuna):
    try:
        comuna = Comunas.get(Comunas.comuna == nombre_comuna)
        return comuna
    except Exception as error:
        print(f"Ha Ocurritod un error!: {error}")

def guardar_comuna(comuna:Comunas):
    try:
        nueva_comuna = comuna.save()
        return nueva_comuna
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")




