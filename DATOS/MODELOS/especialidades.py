from peewee import Model, AutoField, CharField, BooleanField, SQL
from DATOS.conexion import conectar
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Especialidades(BaseModel):
    id_especialidad = AutoField()
    especialidad = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'especialidades'
