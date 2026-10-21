from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL, DateField
from DATOS.conexion import conectar
from DATOS.MODELOS.persona import Persona
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Instructor(BaseModel):
    id_instructor = AutoField()
    login_instructor = CharField(max_length=50, null=True)
    info_persona = ForeignKeyField(column_name='info_persona', field='id_persona', model=Persona, null=True)
    fecha_contratacion = DateField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'instructores'