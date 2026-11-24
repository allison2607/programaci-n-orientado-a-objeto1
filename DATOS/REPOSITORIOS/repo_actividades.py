from datos.modelos.actividad import Actividad

def mostrar_actividades():
    try:
        actividades = actividad.select().where(actividad.habilitado == 1)
        return actividades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_actividad_nombre(nombre_actividad):
    try:
        actividad = Actividad.get(Actividad.nombre == nombre_actividad)
        return actividad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_actividad(actividad:Actividad):
    try:
        nueva_actividad = actividad.save()
        return nueva_actividad 
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")


