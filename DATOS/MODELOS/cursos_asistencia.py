from peewee import Model, AutoField, ForeignKeyField, FloatField
from DATOS.conexion import conectar
from DATOS.MODELOS.cursos import Curso
from DATOS.MODELOS.estudiantes import Estudiantes

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class CursosAsistencias(BaseModel):
    id_asistencia = AutoField()
    asistencia = FloatField(null=True)
    curso = ForeignKeyField(column='curso', field='id_cursos', model=Curso, null=True)
    estudiante = ForeignKeyField(column='estudiante', field='id_estudiante', model=Estudiantes, null=True)


    class Meta:
        table_name = 'cursos_asistencias'
