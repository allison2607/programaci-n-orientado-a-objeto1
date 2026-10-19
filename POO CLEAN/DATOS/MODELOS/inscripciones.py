from peewee import Model, AutoField, FloatField, ForeignKeyField, BooleanField, SQL, DateField
from DATOS.conexion import conectar
from DATOS.MODELOS.cursos import Curso
from DATOS.MODELOS.estudiantes import Estudiantes
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Inscripciones(BaseModel):
    id_inscripcion = AutoField()
    avance = FloatField()
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Curso, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiantes, null=True)
    fecha_inscripcion = DateField()
    nota_final = FloatField(null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'inscripciones'