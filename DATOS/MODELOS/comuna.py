from peewee import Model, AutoField, CharField, BooleanField, SQL
from datos.conexion import conectar
from auxiliar.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Comuna(BaseModel):
    id_comuna = AutoField(primary_key=True)
    comuna = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'comunas'