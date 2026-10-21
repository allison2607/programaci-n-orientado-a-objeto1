from DATOS.MODELOS.pais import Pais

def mostrar_paises(pais:Pais):
    try:
        paises = pais.select().where(pais.habilitado == 1)
        return paises
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_pais_nombre(nombre_pais):
    try:
        pais = Pais.get(Pais.pais == nombre_pais)
        return pais
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_pais(pais:Pais):
    try:
        nuevo_pais = pais.save()
        return nuevo_pais
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

