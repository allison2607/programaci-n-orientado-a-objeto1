from DATOS.MODELOS.actividades import Actividades

def mostrar_actividades(actividad:Actividades):
    try:
        actividades = actividad.select().where(actividad.habilitado == 1)
        return actividades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_actividad_nombre(nombre_actividad):
    try:
        actividad = Actividades.get(Actividades.nombre == nombre_actividad)
        return actividad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_actividad(actividad:Actividades):
    try:
        nueva_actividad = actividad.save()
        return nueva_actividad 
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")


