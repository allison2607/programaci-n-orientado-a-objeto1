from DATOS.MODELOS.cursos import Curso
from DATOS.REPOSITORIOS.repo_curso import guardar_curso, editar_curso, deshabilitar_curso, mostrar_cursos

def logica_cursos(titulo, descripcion, duracion, 
                  asistencia_min, nota_min):

    if titulo == "":
        print("Error! El titulo no puede estar vacio!")
    if duracion <= 0:
        print("Error! La duracion del curso no puede ser menor a 0!")
    if asistencia_min <= 49:
        print("Error! La asistencia minima no puede ser menor al 49%!")
    if nota_min <= 3.9:
        print("Error! la nota minima no puede ser menor a 4.0!")

    nuevo_curso = Curso(
        titulo_curso = titulo,
        descripcion = descripcion,
        duracion_dias = duracion,
        asistencia_min = asistencia_min,
        nota_min = nota_min,
        habilitado = 1
    )

    return guardar_curso(nuevo_curso)