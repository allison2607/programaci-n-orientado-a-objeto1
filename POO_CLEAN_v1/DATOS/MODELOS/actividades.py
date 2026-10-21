from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.contenidos import Contenidos
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Actividades(BaseModel):
    id_actividades = AutoField()
    contenido = ForeignKeyField(column_name='contenido', field='id_contenidos', model=Contenidos, null=True)
    descripcion = CharField(max_length=50)
    evaluacion = BooleanField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    nombre = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'actividades'
