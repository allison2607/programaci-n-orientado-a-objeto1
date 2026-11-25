from peewee import Model, AutoField, ForeignKeyField, BooleanField, SQL
from datos.conexion import conectar
from datos.modelos.instructor import Instructor
from datos.modelos.curso import Curso
from auxiliar.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class InstructorCurso(BaseModel):
    id_ins_cursos = AutoField()
    instructor = ForeignKeyField(column_name='instructor', field='id_instructor', model=Instructor, null=True)
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Curso, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'instructor_cursos'
