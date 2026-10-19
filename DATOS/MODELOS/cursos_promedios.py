from peewee import Model, AutoField, FloatField, ForeignKeyField
from DATOS.conexion import conectar
from DATOS.MODELOS.cursos import Curso
from DATOS.MODELOS.estudiantes import Estudiantes
base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database= base_datos

class CursosPromedios(BaseModel):
    id_promedio = AutoField()
    promedio = FloatField(null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Curso, null=True)
    cursos = ForeignKeyField(column_name='curso', field='id_curso', model=Curso, null=True)


    class Meta:
        table_name = 'cursos_promedios'

