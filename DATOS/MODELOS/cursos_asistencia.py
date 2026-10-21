from peewee import Model, AutoField, ForeignKeyField, FloatField
from DATOS.conexion import conectar
from DATOS.MODELOS.curso import Curso
from DATOS.MODELOS.estudiante import Estudiante

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class CursosAsistencia(BaseModel):
    id_asistencia = AutoField()
    asistencia = FloatField(null=True)
    curso = ForeignKeyField(column='curso', field='id_cursos', model=Curso, null=True)
    estudiante = ForeignKeyField(column='estudiante', field='id_estudiante', model=Estudiante, null=True)


    class Meta:
        table_name = 'cursos_asistencias'
