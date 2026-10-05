from peewee import *
from datos.conexion import conectar


default = "DEFAULT 1"

database = conectar()

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Cursos(BaseModel):
    asistencia_min = FloatField()
    descripcion = CharField(max_length=50)
    duracion_dias = IntegerField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_cursos = AutoField()
    nota_min = FloatField()
    titulo_curso = CharField(max_length=50)

    class Meta:
        table_name = 'cursos'

class Modulos(BaseModel):
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Cursos, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_modulos = AutoField()
    nombre_modulo = CharField(max_length=50)

    class Meta:
        table_name = 'modulos'

class Contenidos(BaseModel):
    descripcion = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_contenidos = AutoField()
    modulo = ForeignKeyField(column_name='modulo', field='id_modulos', model=Modulos, null=True)

    class Meta:
        table_name = 'contenidos'

class Actividades(BaseModel):
    contenido = ForeignKeyField(column_name='contenido', field='id_contenidos', model=Contenidos, null=True)
    descripcion = CharField(max_length=50)
    evaluacion = BooleanField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_actividades = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'actividades'

class Comunas(BaseModel):
    comuna = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_comuna = AutoField()

    class Meta:
        table_name = 'comunas'

class Paises(BaseModel):
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_pais = AutoField()
    pais = CharField(max_length=50)

    class Meta:
        table_name = 'paises'

class Direcciones(BaseModel):
    calle = CharField(max_length=50, null=True)
    comuna = ForeignKeyField(column_name='comuna', field='id_comuna', model=Comunas, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_direcciones = AutoField()
    numero = IntegerField()
    pais = ForeignKeyField(column_name='pais', field='id_pais', model=Paises, null=True)

    class Meta:
        table_name = 'direcciones'

class Personas(BaseModel):
    apellido = CharField(max_length=50)
    celular = CharField(max_length=50, unique=True)
    correo = CharField(unique=True)
    direccion = ForeignKeyField(column_name='direccion', field='id_direcciones', model=Direcciones, null=True)
    fecha_nacimiento = DateField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_persona = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=50, unique=True)

    class Meta:
        table_name = 'personas'

class Estudiantes(BaseModel):
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_estudiante = AutoField()
    info_persona = ForeignKeyField(column_name='info_persona', field='id_persona', model=Personas, null=True)
    login_estudiante = CharField(max_length=50)

    class Meta:
        table_name = 'estudiantes'

class CursosAsistencias(BaseModel):
    asistencia = FloatField(null=True)
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Cursos, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiantes, null=True)
    id_asistencia = AutoField()

    class Meta:
        table_name = 'cursos_asistencias'

class CursosPromedios(BaseModel):
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Cursos, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiantes, null=True)
    id_promedio = AutoField()
    promedio = FloatField(null=True)

    class Meta:
        table_name = 'cursos_promedios'

class Especialidades(BaseModel):
    especialidad = CharField(max_length=50)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_especialidad = AutoField()

    class Meta:
        table_name = 'especialidades'

class Inscripciones(BaseModel):
    avance = FloatField()
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Cursos, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiantes, null=True)
    fecha_inscripcion = DateField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_inscripcion = AutoField()
    nota_final = FloatField(null=True)

    class Meta:
        table_name = 'inscripciones'

class Instructores(BaseModel):
    fecha_contratacion = DateField()
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_instructor = AutoField()
    info_persona = ForeignKeyField(column_name='info_persona', field='id_persona', model=Personas, null=True)
    login_instructor = CharField(max_length=50)

    class Meta:
        table_name = 'instructores'

class InstructorCursos(BaseModel):
    curso = ForeignKeyField(column_name='curso', field='id_cursos', model=Cursos, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_ins_cursos = AutoField()
    instructor = ForeignKeyField(column_name='instructor', field='id_instructor', model=Instructores, null=True)

    class Meta:
        table_name = 'instructor_cursos'

class InstructoresEspecialidades(BaseModel):
    especialidad = ForeignKeyField(column_name='especialidad', field='id_especialidad', model=Especialidades, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_ins_esp = AutoField()
    instructor = ForeignKeyField(column_name='instructor', field='id_instructor', model=Instructores, null=True)

    class Meta:
        table_name = 'instructores_especialidades'

class NotasActividades(BaseModel):
    actividad = ForeignKeyField(column_name='actividad', field='id_actividades', model=Actividades, null=True)
    estudiante = ForeignKeyField(column_name='estudiante', field='id_estudiante', model=Estudiantes, null=True)
    habilitado = BooleanField(constraints=[SQL(default)], null=True)
    id_notas_act = AutoField()
    nota_actividad = FloatField(null=True)

    class Meta:
        table_name = 'notas_actividades'

