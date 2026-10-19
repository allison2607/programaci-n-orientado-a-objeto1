from peewee import Model, AutoField, ForeignKeyField, BooleanField, SQL
from DATOS.conexion import conectar
from DATOS.MODELOS.instructores import Instructores
from DATOS.MODELOS.cursos import Curso
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class InstructorCursos(BaseModel):
    id_ins_cursos = AutoField()
    instructor = ForeignKeyField(column_name='instructor', field='id_instructor', model=Instructores, null=True)
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Curso, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'instructor_cursos'
