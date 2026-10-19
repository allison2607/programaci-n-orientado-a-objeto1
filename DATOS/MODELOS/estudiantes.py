from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.personas import Personas
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Estudiantes(BaseModel):
    id_estudiante = AutoField()
    login_estudiante = CharField(max_length=50)
    info_persona = ForeignKeyField(column_name='info_persona', field='id_persona', model=Personas, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'estudiantes'

