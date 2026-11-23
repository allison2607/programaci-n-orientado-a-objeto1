from datos.modelos.especialidad import Especialidad

def mostrar_especialidades():
    try:
        especialidades = Especialidad.select().where(Especialidad.habilitado == 1)
        return especialidades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_especialidad(nombre_especialidad):
    try:
        especialidad = Especialidad.get_or_none(Especialidad.especialidad == nombre_especialidad)
        return especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_especialidad(especialidad:Especialidad):
    try:
        nueva_especialidad = especialidad.save()
        return nueva_especialidad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")    