from peewee import Model, AutoField, CharField, BooleanField, SQL
from DATOS.conexion import conectar
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Comuna(BaseModel):
    id_comuna = AutoField()
    comuna = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'comunas'