from DATOS.MODELOS.actividades import Actividades

def mostrar_actividades(actividad:Actividades):
    try:
        actividades = actividad.select().where(Actividades.habilitado == 1)
        return actividades
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def guardar_actividades(actividad:Actividades):
    try:
        nueva_actividad = actividad.save()
        return nueva_actividad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_actividad(nombre_actividad):
    try:
        actividades = Actividades.get(Actividades.actividades == nombre_actividad)
        if actividades:
            return actividades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
