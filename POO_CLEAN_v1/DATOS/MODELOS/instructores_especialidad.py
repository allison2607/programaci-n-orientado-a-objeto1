from peewee import Model, AutoField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.instructor import Instructor
from DATOS.MODELOS.especialidad import Especialidad
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class InstructoresEspecialidad(BaseModel):
    id_ins_esp = AutoField()
    instructor = ForeignKeyField(column_name='instructor', field='id_instructor', model=Instructor, null=True)
    especialidad = ForeignKeyField(column_name='especialidad', field='id_especialidad', model=Especialidad, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'instructores_especialidades'

