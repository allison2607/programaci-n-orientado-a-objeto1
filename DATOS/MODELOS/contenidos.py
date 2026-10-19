from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.modulos import Modulos
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Contenidos(BaseModel):
    id_contenido = AutoField()
    descripcion = CharField(max_length=50)
    modulo = ForeignKeyField(column_name='modulo', field='id_modulos', model=Modulos, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'contenidos'