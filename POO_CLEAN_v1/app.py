from PRESENTACION.presentacion_persona import menu_crear_persona, listado_personas, menu_editar_persona, menu_eliminar_persona

def menu():
    print("***" + "Bienvenido al Sistema de Clases Online!".center(80) + "***")
    print()
    print("Que deseas hacer?".center(80))
    print()
    print("""             1.- Gestionar Personas
             2.- Gestionar Estudiantes [Proximamente]
             3.- Gestionar Instructores [Proximanente]
             4.- Gestionar Cursos [Proximanente]
             5.- Gestionar Direccioness [Proximamente]
             6.- Salir!""".center(80))
    desarrollo = "[EN DESARROLLO...]"
    flag = True
    while flag:
        try:
            decision = int(input(""))
            if decision == 1:
                gestionar_personas()
                return
            elif decision == 2:
                print(desarrollo)
            elif decision == 3:
                print(desarrollo)
            elif decision == 4:
                print(desarrollo)
            elif decision == 5:
                print(desarrollo)
            elif decision == 6:
                print("Adios!")
                flag = False
            else: 
             print("Elige una opcion valida!")
        except ValueError:
            print("No funciona asi!")        


def gestionar_personas():
    print("***" + "GESTION DE PERSONAS".center(80) + "***")
    print()
    print("Que deseas hacer?".center(80))
    print()
    print("""             1.- Ingresar Persona
             2.- Mostrar la lista de personas ingresadas
             3.- Editar persona
             4.- Eliminar persona
             5.- Regresar al Menu""".center(80))
             
    desarrollo = "[EN DESARROLLO...]"
    flag = True
    while flag:
        try:
            decision = int(input())
            if decision == 1:
                menu_crear_persona()
            elif decision == 2:
                listado_personas()
            elif decision == 3:
                menu_editar_persona()
            elif decision == 4:
                menu_eliminar_persona()
            elif decision == 5:
                print("Volviendo...")
                menu()
                flag = False
            else:
                print("Esa no es una opcion!")
        except ValueError:
            print("Asi no funciona!")
            


if __name__ == "__main__":
    menu()






