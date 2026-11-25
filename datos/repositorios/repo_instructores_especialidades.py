from datos.modelos.instructores_especialidad import InstructoresEspecialidad
from datos.modelos.instructor import Instructor
from datos.modelos.especialidad import Especialidad
from datos.modelos.persona import Persona

def mostrar_especialidades_instructores():
    try:
        especialidadesinstructores = (InstructoresEspecialidad.select()
                                      .join(Instructor).switch(InstructoresEspecialidad).join(Especialidad)
                                      .where((InstructoresEspecialidad.instructor == Instructor.id_instructor)
                                              & (Instructor.habilitado == 1)
                                                & (InstructoresEspecialidad.especialidad == Especialidad.id_especialidad)
                                                & (Especialidad.habilitado == 1)
                                                & InstructoresEspecialidad.habilitado == 1))
        return especialidadesinstructores
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_especialidades_instructores(rut, especialidad):
    try:
        especialidades_instructor = (InstructoresEspecialidad.select()
                                     .join(Instructor).join(Persona).switch(InstructoresEspecialidad).join(Especialidad)
                                     .where((Persona.rut == rut) &
                                            (Especialidad.especialidad == especialidad)).first())
        return especialidades_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_especialidad_instructor(
        especialidadesinstructor:InstructoresEspecialidad):
    try:
        nueva_especialidad_instructor = especialidadesinstructor.save()
        return nueva_especialidad_instructor
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

