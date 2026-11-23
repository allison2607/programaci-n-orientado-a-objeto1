from PRESENTACION.presentacion_comuna import (menu_crear_comuna,
                                              listado_comunas,
                                              menu_eliminar_comuna,
                                              menu_activar_comuna,
                                              menu_editar_comuna)
from PRESENTACION.presentacion_pais import (menu_crear_pais,
                                            listado_paises,
                                            menu_eliminar_pais,
                                            menu_activar_pais,
                                            menu_editar_pais)
from PRESENTACION.presentacion_direccion import (menu_crear_direccion,
                                                 listado_direcciones,
                                                 menu_eliminar_direccion,
                                                 menu_editar_direccion,
                                                 menu_activar_direccion)
from PRESENTACION.presentacion_persona import (menu_crear_persona, menu_editar_persona,
                                               listado_personas, menu_eliminar_persona,
                                               menu_activar_persona)
from PRESENTACION.presentacion_especialidad import (menu_activar_especialidad, menu_crear_especialidad,
                                                    menu_editar_especialidad, menu_eliminar_especialidad,
                                                    listado_especialidades)
from PRESENTACION.presentacion_instructor import (menu_asignar_instructor, menu_editar_login,
                                                listado_instructores, menu_eliminar_instructor, 
                                                menu_activar_instructor)
from PRESENTACION.presentacion_estudiante import (menu_asignar_estudiante, menu_editar_login_e,
                                                  listado_estudiantes, menu_eliminar_estudiante,
                                                  menu_activar_estudiante)
from PRESENTACION.presentacion_instructor_especialidad import (menu_asignar_especialidad_instructor,
                                                               listado_especialidades_instructores,
                                                               menu_editar_asociacion,
                                                               menu_eliminar_asociacion,
                                                               menu_activar_asociacion)



def menu():
    flag = True
    while flag:
        try:
            print("""              Que deseas hacer?

            1.- Gestion de Comunas
            2.- Gestion de Paises
            3.- Gestion de Direcciones
            4.- Gestion de Personas
            5.- Gestion de Especialidades
            6.- Gestion de Instructores
            7.- Gestion de Estudiantes
            0.- Salir""")
            decision = int(input(""))
            if decision == 1:
                menu_comunas()
                
            elif decision == 2:
                menu_paises()

            elif decision == 3:
                menu_direcciones()

            elif decision == 4:
                menu_personas()

            elif decision == 5:
                menu_especialidad()

            elif decision == 6:
                menu_instructores()

            elif decision == 7:
                menu_estudiantes()
            
            elif decision == 0:
                print("Adios!")
                flag = False 
            else: 
                print("Esa no es una opcion Valida!")   
        except ValueError:
            print("No funciona asi!")



def menu_comunas():
    print("[***" + "GESTION COMUNAS".center(80) + "***]")
    print("""                1.- Ingresar Comuna
                2.- Editar Comuna
                3.- Mostrar Comunas
                4.- Eliminar Comuna
                5.- Activar Comuna
                6.- Volver""")
    decision = int(input(""))
    if decision == 1:
        menu_crear_comuna()
    elif decision == 2:
        menu_editar_comuna()
    elif decision == 3:
        listado_comunas()
    elif decision == 4:
        menu_eliminar_comuna()
    elif decision == 5:
        menu_activar_comuna()
    elif decision == 6:
        return

def menu_paises():
    print("[***" + "GESTION PAISES".center(80) + "***]")
    print("""                1.- Ingresar Pais
                2.- Editar Pais
                3.- Mostrar Paises
                4.- Eliminar Pais
                5.- Activar Pais
                6.- Volver""")
    decision = int(input(""))
    if decision == 1:
        menu_crear_pais()
    elif decision == 2:
        menu_editar_pais()
    elif decision == 3:
        listado_paises()
    elif decision == 4:
        menu_eliminar_pais()
    elif decision == 5:
        menu_activar_pais()
    elif decision == 6:
        return
def menu_direcciones():
    print("[***" + "GESTION DIRECCIONES".center(80) + "***]")
    print("""    1.- Ingresar Direccion
    2.- Editar Direccion
    3.- Mostrar Direcciones
    4.- Eliminar Direccion
    5.- Activar Direccion
    6.- Volver""")
    decision = int(input(""))
    if decision == 1:
        menu_crear_direccion()
    elif decision == 2:
        menu_editar_direccion()
    elif decision == 3:
        listado_direcciones()
    elif decision == 4:
        menu_eliminar_direccion()
    elif decision == 5:
        menu_activar_direccion()
    elif decision == 6:
        return

def menu_personas():
    print("[***" + "GESTION DATOS PERSONAS".center(80) + "***]")
    print("""    1.- Crear Datos Persona 
    2.- Editar Datos Persona
    3.- Mostrar Datos Personas
    4.- Eliminar Datos Persona
    5.- Activar Datos Persona
    6.- Volver""")
    decision = int(input(""))
    if decision == 1:
        menu_crear_persona()
    elif decision == 2:
        menu_editar_persona()
    elif decision == 3:
        listado_personas()
    elif decision == 4:
        menu_eliminar_persona()
    elif decision == 5:
        menu_activar_persona()
    elif decision == 6:
        return    

def menu_especialidad():
    print("[***" + "GESTION ESPECIALIDADES".center(80) + "***]")
    print("""    1.- Crear Especialidad
    2.- Editar Especialidad
    3.- Mostrar Especialidades
    4.- Eliminar Especialidad
    5.- Activar Especialidad
    6.- Asignar Especialidad a Instructor
    7.- Editar Especialidad a Instructor
    8.- Mostrar Instructores y Especialidades
    9.- Eliminar Especialidad a Instructor
    10.- Activar Especialidad a Instructor
    0.- Volver""")

    decision = int(input(""))

    if decision == 1:
        menu_crear_especialidad()
    elif decision == 2:
        menu_editar_especialidad()
    elif decision == 3:
        listado_especialidades()
    elif decision == 4:
        menu_eliminar_especialidad()
    elif decision == 5:
        menu_activar_especialidad()
    elif decision == 6:
        menu_asignar_especialidad_instructor()
    elif decision == 7:
        menu_editar_asociacion()
    elif decision == 8:
        listado_especialidades_instructores()
    elif decision == 9:
        menu_eliminar_asociacion()
    elif decision == 10: 
        menu_activar_asociacion()
    elif decision == 0:
        return

def menu_instructores():
    print("[***" + "GESTION DE INSTRUCTORES".center(80) + "***]")
    print("""    1.- Asignar Rol de Instructor
    2.- Editar Login
    3.- Mostrar Instructores
    4.- Eliminar Instructor
    5.- Activar Instructor
    6.- Asignar Especialidad a Instructor
    7.- Editar Especialidad a Instructor
    8.- Mostrar Instructores y Especialidades
    9.- Eliminar Especialidad a Instructor
    10.- Activar Especialidad a Instructor
    0.- Volver""")

    decision = int(input(""))

    if decision == 1:
        menu_asignar_instructor()
    elif decision == 2:
        menu_editar_login()
    elif decision == 3:
        listado_instructores()
    elif decision == 4:
        menu_eliminar_instructor()
    elif decision == 5:
        menu_activar_instructor()
    elif decision == 6:
        menu_asignar_especialidad_instructor()
    elif decision == 7:
        menu_editar_especialidad()
    elif decision == 8:
        listado_especialidades_instructores()
    elif decision == 9:
        menu_eliminar_asociacion()
    elif decision == 10: 
        menu_activar_asociacion()
    elif decision == 0:
        return

def menu_estudiantes():
    print("[***" + "GESTION DE ESTUDIANTES".center(80) + "***]")
    print("""    1.- Asignar Rol de Estudiante
    2.- Editar Login
    3.- Mostrar Estudiantes
    4.- Eliminar Estudiante
    5.- Activar Estudiante
    6.- Volver""")

    decision = int(input(""))

    if decision == 1:
        menu_asignar_estudiante()
    elif decision == 2:
        menu_editar_login_e()
    elif decision == 3:
        listado_estudiantes()
    elif decision == 4:
        menu_eliminar_estudiante()
    elif decision == 5:
        menu_activar_estudiante()
    elif decision == 6:
        return     


if __name__ == "__main__":
    menu()






