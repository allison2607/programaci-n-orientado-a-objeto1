from DATOS.MODELOS.usuario import Usuario

def mostrar_usuario(usuario:Usuario):
    try:
        usuarioes = usuario.select().where(usuario.habilitado == 1)
        return usuarioes
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_usuario_nombre(nombre_usuario):
    try:
        usuario = Usuario.get(Usuario.usuario == nombre_usuario)
        return usuario
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def guardar_usuario(usuario:Usuario):
    try:
        nuevo_usuario = usuario.save()
        return nuevo_usuario
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")

def obtener_usuario_rut(rut_usuario):
    try:
        usuario = Usuario.get(Usuario.rut == rut_usuario)
        if usuario:
            return usuario
    except Exception as error:
        print(f"Ha ocurrido un error!: {error}")