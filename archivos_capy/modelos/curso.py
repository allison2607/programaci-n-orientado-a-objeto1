from peewee import AutoField, BooleanField, CharField, FloatField, IntegerField, SQL
from archivos_capy.auxiliar import default
from archivos_capy.modelos.base import BaseModel


class Curso(BaseModel):
    id_cursos = AutoField()
    titulo_curso = CharField(max_length=50)
    descripcion = CharField(max_length=50)
    duracion_dias = IntegerField()
    asistencia_min = FloatField()
    nota_min = FloatField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'cursos'