from peewee import Model
from archivos_capy.datos.conexion import conectar

base_datos = conectar()


class BaseModel(Model):
    class Meta:
        database = base_datos