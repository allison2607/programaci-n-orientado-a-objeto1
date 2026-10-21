from DATOS.MODELOS.instructores_especialidades import InstructoresEspecialidades

def mostrar_especialidades_instructores(
        especialidadesinstructor:InstructoresEspecialidades):
    try:
        especialidadesinstructores = especialidadesinstructor.select().where(
            especialidadesinstructor.habilitado == 1)
        return especialidadesinstructores
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_especialidades_instructores(instructor):
    try:
        especialidades_instructor = InstructoresEspecialidades.get(
            InstructoresEspecialidades.instructor == instructor
        )
        return especialidades_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_especialidad_instructor(
        especialidadesinstructor:InstructoresEspecialidades):
    try:
        nueva_especialidad_instructor = especialidadesinstructor.save()
        return nueva_especialidad_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

