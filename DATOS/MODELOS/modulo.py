from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from datos.conexion import conectar
from datos.modelos.curso import Curso
from auxiliar.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Modulo(BaseModel):
    id_modulos = AutoField()
    nombre_modulo = CharField(max_length=50)
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Curso, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'modulos'