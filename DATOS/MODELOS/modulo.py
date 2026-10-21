from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.curso import Curso
from AUXILIAR.datos_app import default 

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