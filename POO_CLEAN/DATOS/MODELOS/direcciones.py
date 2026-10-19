from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.paises import Paises
from DATOS.MODELOS.comunas import Comunas
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Direcciones(BaseModel):
    id_direcciones = AutoField()
    calle = CharField(max_length=50, null=True)
    comuna = ForeignKeyField(column_name='comuna', field='id_comuna', model=Comunas, null=True)
    numero = IntegerField()
    pais = ForeignKeyField(column_name='pais', field='id_pais', model=Paises, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'direcciones'

