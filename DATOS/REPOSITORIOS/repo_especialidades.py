from DATOS.MODELOS.especialidades import Especialidades

def mostrar_especialidades(especialidad:Especialidades):
    try:
        especialidades = especialidad.select().where(especialidad.habilitado == 1)
        return especialidades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_especialidad(nombre_especialidad):
    try:
        especialidad = Especialidades.get(Especialidades.especialidad == nombre_especialidad)
        return especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_especialidad(especialidad:Especialidades):
    try:
        nueva_especialidad = especialidad.save()
        return nueva_especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")    