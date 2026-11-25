from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from datos.conexion import conectar
from datos.modelos.modulo import Modulo
from auxiliar.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Contenido(BaseModel):
    id_contenido = AutoField()
    descripcion = CharField(max_length=50)
    modulo = ForeignKeyField(column_name='modulo', field='id_modulos', model=Modulo, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'contenidos'