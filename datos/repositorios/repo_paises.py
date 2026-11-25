from datos.modelos.pais import Pais

def mostrar_paises():
    try:
        paises = Pais.select().where(Pais.habilitado == 1)
        return paises
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_pais_nombre(nombre_pais):
    try:
        pais = Pais.get_or_none(Pais.pais == nombre_pais)
        return pais
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_pais(pais:Pais):
    try:
        nuevo_pais = pais.save()
        return nuevo_pais
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

