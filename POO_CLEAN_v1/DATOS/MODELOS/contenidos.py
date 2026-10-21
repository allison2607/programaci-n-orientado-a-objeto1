from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.modulo import Modulo
from AUXILIAR.datos_app import default 

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