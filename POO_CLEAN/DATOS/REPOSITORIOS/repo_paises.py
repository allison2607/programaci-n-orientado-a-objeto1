from DATOS.MODELOS.paises import Paises

def mostrar_paises(pais:Paises):
    try:
        paises = pais.select().where(pais.habilitado == 1)
        return paises
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_pais(pais:Paises):
    try:
        nuevo_pais = pais.save
        return nuevo_pais
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

