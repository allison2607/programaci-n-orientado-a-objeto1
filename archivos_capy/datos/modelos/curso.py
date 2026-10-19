from peewee import SQL,AutoField, BooleanField, CharField, DecimalField, IntegerField 
from datos.conexion import conectar
from auxiliares.datos_app_capy import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Curso(BaseModel):
    id_cursos = AutoField()
    titulo_curso = CharField(max_length=50)
    descripcion = CharField(max_length=50)
    duracion_dias = IntegerField()
    asistencia_min = IntegerField()
    nota_min = DecimalField()
    habilitado = BooleanField(constraints=[SQL(defecto)], null=True)

    class Meta:
        table_name = 'cursos'