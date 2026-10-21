from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.pais import Pais
from DATOS.MODELOS.comuna import Comuna
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Direccion(BaseModel):
    id_direcciones = AutoField()
    calle = CharField(max_length=50, null=True)
    comuna = ForeignKeyField(column_name='comuna', field='id_comuna', model=Comuna, null=True)
    numero = IntegerField()
    pais = ForeignKeyField(column_name='pais', field='id_pais', model=Pais, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'direcciones'

