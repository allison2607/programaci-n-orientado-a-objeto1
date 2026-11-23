from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, BooleanField, SQL
from datos.conexion import conectar
from datos.modelos.pais import Pais
from datos.modelos.comuna import Comuna
from auxiliar.datos_app import default 

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

