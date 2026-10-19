from DATOS.MODELOS.especialidades import Especialidades

def mostrar_especialidades(especialidad:Especialidades):
    try:
        especialidades = especialidad.select().where(Especialidades.habilitado == 1)
        return especialidades
    except Exception as error:
        print(f"Ha ocurrido un Error!: {error}")

def guardar_actividades(especialidad:Especialidades):
    try:
        nueva_especialidad = especialidad.save()
        return nueva_especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_actividad(nombre_especialidad):
    try:
        especialidades = Especialidades.get(Especialidades.especialidad == nombre_especialidad)
        if especialidades:
            return especialidades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")
