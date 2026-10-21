from peewee import Model, AutoField, FloatField, ForeignKeyField
from DATOS.conexion import conectar
from DATOS.MODELOS.curso import Curso
from DATOS.MODELOS.estudiante import Estudiante
base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database= base_datos

class CursosPromedio(BaseModel):
    id_promedio = AutoField()
    promedio = FloatField(null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Curso, null=True)
    cursos = ForeignKeyField(column_name='curso', field='id_curso', model=Curso, null=True)


    class Meta:
        table_name = 'cursos_promedios'

