from peewee import Model, AutoField, CharField, FloatField, IntegerField, BooleanField, SQL
from DATOS.conexion import conectar
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Curso(BaseModel):
    id_cursos = AutoField()
    asistencia_min = FloatField()
    descripcion = CharField(max_length=50)
    duracion_dias = IntegerField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    nota_min = FloatField()
    titulo_curso = CharField(max_length=50)

    class Meta:
        table_name = 'cursos'
        