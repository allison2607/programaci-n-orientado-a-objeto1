from DATOS.MODELOS.notas_actividades import NotasActividades

def mostrar_notas(notas:NotasActividades):
    try:
        notas_actividades = notas.select().where(notas.habilitado == 1)
        return notas_actividades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_notas(actividad):
    try:
        nota_actividad = NotasActividades.get(NotasActividades.actividad == actividad)
        return nota_actividad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_nota(notas:NotasActividades):
    try:
        nueva_nota = notas.save()
        return nueva_nota
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")