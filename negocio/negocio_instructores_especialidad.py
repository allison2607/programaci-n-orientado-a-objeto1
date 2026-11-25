from datos.modelos.instructor import Instructor
from datos.modelos.especialidad import Especialidad
from datos.modelos.instructores_especialidad import InstructoresEspecialidad
from datos.repositorios.repo_instructores import (guardar_instructor,
                                                  obtener_instructor_rut,
                                                  mostrar_instructores)
from datos.repositorios.repo_estudiantes import (guardar_estudiante,
                                                 obtener_estudiante_rut)
from datos.repositorios.repo_personas import (obtener_persona_rut)
from datos.repositorios.repo_especialidades import (guardar_especialidad,
                                                    obtener_especialidad,
                                                    mostrar_especialidades)
from datos.repositorios.repo_instructores_especialidades import (guardar_especialidad_instructor,
                                                                 obtener_especialidades_instructores,
                                                                 mostrar_especialidades_instructores)

def asignar_especialidad_instructor(rut, especialidad):
    try:
        rut = rut.strip()
        especialidad = especialidad.strip().title()

        persona = obtener_persona_rut(rut)
        if not persona:
            return f"La persona con RUT {rut} no esta registrada!"

        instructor = obtener_instructor_rut(rut)
        if not instructor:
            return f"La persona '{persona.nombre}' no esta registrada como Instructor"

        especialidad_asignar = obtener_especialidad(especialidad)
        if not especialidad_asignar:
            return f"La especialidad '{especialidad}' no esta registrada!"

        instructor_especialidad = InstructoresEspecialidad()
        instructor_especialidad.instructor = instructor.id_instructor
        instructor_especialidad.especialidad = especialidad_asignar.id_especialidad

        nueva_asignacion = guardar_especialidad_instructor(instructor_especialidad)    
        return nueva_asignacion
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def lista_especialidades_instructores():
    resultado = mostrar_especialidades_instructores()

    if not resultado:
        return "No hay ninguna Especialidad Asignada!"
    return resultado

def editar_especialidad(rut, antigua_especialidad, nueva_especialidad):
    try:
        rut = rut.strip()
        antigua_especialidad = antigua_especialidad.strip().title()
        nueva_especialidad = nueva_especialidad.strip().title()

        persona = obtener_persona_rut(rut)
        especialidad = obtener_especialidades_instructores(rut, antigua_especialidad)
        if not especialidad:
            return f"{persona.nombre} {persona.apellido} no tiene esa especialidad!"

        especialidad_nueva = obtener_especialidad(nueva_especialidad)
        if not especialidad_nueva:
            return f"Especialidad '{nueva_especialidad}' no esta registrada!"

        especialidad.especialidad = especialidad_nueva.id_especialidad
        resultado = guardar_especialidad_instructor(especialidad)

        return resultado
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def eliminar_especialidad_instructor(rut, especialidad):
    try:
        rut = rut.strip()
        especialidad = especialidad.strip().title()

        persona = obtener_persona_rut(rut)
        relacion = obtener_especialidades_instructores(rut, especialidad)
        if not relacion:
            return f"{persona.nombre} {persona.apellido} no tiene esa especialidad!"

        relacion.habilitado = 0
        guardar_especialidad_instructor(relacion)
        return "Especialidad Eliminada con Exito!"
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"

def activar_especialidad_instructor(rut, especialidad):
    try:
        rut = rut.strip()
        especialidad = especialidad.strip().title()

        persona = obtener_persona_rut(rut)
        relacion = obtener_especialidades_instructores(rut, especialidad)
        if not relacion:
            return f"{persona.nombre} {persona.apellido} no tiene esa especialidad!"

        relacion.habilitado = 1
        guardar_especialidad_instructor(relacion)
        return "Especialidad Actividada con Exito!"
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"


        
        