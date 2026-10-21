from prettytable import PrettyTable
from DATOS.MODELOS.persona import Persona
from DATOS.MODELOS.direccion import Direccion
from DATOS.MODELOS.comuna import Comuna
from DATOS.MODELOS.pais import Pais
from NEGOCIO.negocio_persona import (crear_persona,
                                     editar_persona,
                                     lista_personas,
                                     eliminar_persona)

def menu_crear_persona():
    print("*" + "INGRESA DATOS DE LA NUEVA PERSONA".center(80) + "*")
    nombre = input("Ingresa el nombre de la persona\n"
                   ).strip().capitalize()
    rut = input("Ingresa el rut de la persona\n"
                ).strip()
    apellido = input("Ingresa el apellido de la persona\n"
                     ).strip().capitalize()
    celular = input("Ingresa el celular de la persona\n"
                    ).strip()
    correo = input("Ingresa el correo de la persona\n"
                   ).strip()
    fecha_nacimiento = input("""Ingresa la fecha de nacimiento de la persona
    (Ejemplo: 2001-08-29)\n""").strip()
    calle = input("Ingresa el nombre de la Calle de la Persona\n"
                  ).strip()
    comuna = input("Ingresa la Comuna de la Persona\n"
                   ).strip()
    
    numero = int(input("Ingresa el numero de la calle\n"
                   ))
    pais = input("Ingresa el pais de la persona\n"
                 ).strip()


    persona_crear = Persona()
    direccion_crear = Direccion()
    comunas_crear = Comuna()
    paises_crear = Pais()


    resultado = crear_persona(
        persona_crear,
        direccion_crear,
        comunas_crear,
        paises_crear,
        nombre,
        rut,
        apellido,
        celular,
        correo,
        fecha_nacimiento,
        calle,
        comuna,
        numero,
        pais
    )

    if isinstance(resultado, str):
        print(f"[Alerta del Sistema!]: {resultado}")
    else:
        print("Persona guardada con exito!")

def listado_personas():
    resultado = lista_personas()
    if not resultado:
        print("No hay personas ingresadas!")
        return
    tabla = PrettyTable()
    tabla.field_names = ['RUT', 'NOMBRE',
                         'APELLIDO', 'CORREO']
    for p in resultado:
        tabla.add_row([p.rut, p.nombre,
                       p.apellido, p.correo])
    print(tabla)

def menu_editar_persona():
    print("***" + "EDITAR PERSONA".center(80) + "***")
    print()

    rut = input("Ingrese el rut de persona a editar: ")

    print("Ingrese los datos a actualizar\n(Si no hay que editar, dejar en blanco)")

    nuevo_nombre = input("Nuevo nombre\n").strip().capitalize()
    nuevo_apellido = input("Nuevo apellido\n").strip().capitalize()
    nuevo_celular = input("Nuevo celular\n").strip()
    nuevo_correo = input("Nuevo correo\n").strip()
    nueva_fecha = input("Nueva fecha\n").strip()
    nueva_calle = input("Nueva calle\n").strip()
    nueva_comuna = input("Nueva comuna\n").strip()
    nuevo_numero = input("Nuevo numero\n").strip()
    nuevo_pais = input("Nuevo pais\n").strip()

    resultado = editar_persona(
        rut=rut,
        nombre=nuevo_nombre,
        apellido=nuevo_apellido,
        celular=nuevo_celular,
        correo=nuevo_correo,
        fecha_nacimiento=nueva_fecha,
        calle=nueva_calle,
        comuna=nueva_comuna,
        numero=nuevo_numero,
        pais=nuevo_pais
    )
     
    print(f"Actualizacion exitosa!\n{resultado}")

def menu_eliminar_persona():
    print("***" + "ELIMINAR PERSONA" + "***")
    print()
    rut = input("Ingrese rut de la persona a eliminar: ")
    resultado = eliminar_persona(rut)
    print(f"Eliminacion exitosa!: {resultado}")

if __name__ == "__main__":
    menu_crear_persona()