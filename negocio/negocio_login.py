import bcrypt
from datos.repositorios.repo_instructores import (obtener_instructor_correo)

def inicio_sesion(correo, contrasena):
    try:
        correo = correo.strip().lower()
        contrasena = contrasena.strip()

        if not correo or not contrasena:
            return "Debes Ingresar tu correo y contraseña"

        instructor = obtener_instructor_correo(correo)

        if not instructor:
            return "Acceso denegado: Credenciales Invalidas"
        contasenia_valida = bcrypt.checkpw(contrasena.encode('utf-8'), instructor.login_instructor.encode('utf-8'))
        if not contasenia_valida:
            return "Acceso Denegado: Credenciales Invalidas"
        return instructor
    except Exception as error:
        return f"Ha ocurrido un error al iniciar session!: {error}"