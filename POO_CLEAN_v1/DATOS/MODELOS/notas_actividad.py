from peewee import Model, AutoField, FloatField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.actividad import Actividad
from DATOS.MODELOS.estudiante import Estudiante
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class NotasActividad(BaseModel):
    id_notas_act = AutoField()
    actividad = ForeignKeyField(column_name='actividad', field='id_actividades', model=Actividad, null=True)
    estudiante= ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiante, null=True)
    notas_actividad = FloatField(null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'notas_actividades'