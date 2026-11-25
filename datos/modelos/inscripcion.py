from peewee import Model, AutoField, FloatField, ForeignKeyField, BooleanField, SQL, DateField
from datos.conexion import conectar
from datos.modelos.curso import Curso
from datos.modelos.estudiante import Estudiante
from auxiliar.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Inscripcion(BaseModel):
    id_inscripcion = AutoField()
    avance = FloatField()
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Curso, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiante, null=True)
    fecha_inscripcion = DateField()
    nota_final = FloatField(null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)

    class Meta:
        table_name = 'inscripciones'