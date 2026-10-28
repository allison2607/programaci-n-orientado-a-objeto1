from peewee import Model, AutoField, CharField, BooleanField, SQL,IntegerField,DateField
from DATOS.conexion import conectar
from AUXILIAR.datos_app import default 

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12,unique=True)
    nombre=CharField(max_length=25,null=False)
    apellido=CharField(max_length=25,null=False)
    correo=CharField(max_length=191)
    pais=IntegerField(Index=True)
    fecha_nacimiento=DateField()
    genero=IntegerField(null=False)
    fecha_incorporacion=DateField(null=False)
    habilitado = BooleanField(constraints=[SQL(default)],null=True)
    password=CharField(max_length=60,null=True)

    class Meta:
        table_name = 'usuarios'