from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, SQL, DateField
from DATOS.conexion import conectar
from DATOS.MODELOS.direcciones import Direcciones
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Personas(BaseModel):
    id_persona = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=50, unique=True)
    apellido = CharField(max_length=50)
    celular = CharField(max_length=50, unique=True)
    correo = CharField(unique=True)
    direccion = ForeignKeyField(column_name='direccion', field='id_direcciones', model=Direcciones, null=True)
    fecha_nacimiento = DateField()
    habilitado = BooleanField(constraints=[SQL(default)],null=True)

    class Meta:
        table_name = 'personas'
    