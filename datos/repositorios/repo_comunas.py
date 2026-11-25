from datos.modelos.comuna import Comuna

def mostrar_comunas():
    try:
        comunas = Comuna.select().where(Comuna.habilitado == 1)
        return comunas
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def obtener_comuna_nombre(nombre_comuna):
    try:
        comuna = Comuna.get_or_none(Comuna.comuna == nombre_comuna)
        return comuna
    except Exception as error:
        print(f"Ha Ocurritod un error!: {error}")

def guardar_comuna(comuna:Comuna):
    try:
        nueva_comuna = comuna.save()
        return nueva_comuna
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")




