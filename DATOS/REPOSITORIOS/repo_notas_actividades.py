from DATOS.MODELOS.notas_actividad import NotasActividad

def mostrar_notas(notas:NotasActividad):
    try:
        notas_actividades = notas.select().where(notas.habilitado == 1)
        return notas_actividades
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_notas(actividad):
    try:
        nota_actividad = NotasActividad.get(NotasActividad.actividad == actividad)
        return nota_actividad
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_nota(notas:NotasActividad):
    try:
        nueva_nota = notas.save()
        return nueva_nota
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")