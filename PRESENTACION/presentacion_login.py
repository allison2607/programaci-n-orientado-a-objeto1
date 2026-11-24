import maskpass
from auxiliar.aux_validacion import validar_correo
from negocio.negocio_login import inicio_sesion

def menu_inicio_sesion():
    try:
        correo = contrasena = ""
        while correo == "":
            correo_user = input("Correo: ")
            valido = validar_correo(correo_user)
            if valido:
                correo = correo_user
                
            else:
                print("Formato de Correo Incorrecto!")
        while contrasena == "":
            contrasena = maskpass.askpass(prompt="Contraseña: ", mask="*" )
        credenciales_validas = inicio_sesion(correo, contrasena)
        if isinstance(credenciales_validas, str):
            print(f"[Alerta de Sistema!]: {credenciales_validas}")
        elif credenciales_validas:
            print("Bienvenido!")
            return credenciales_validas
    except Exception as error:
        return f"Ha ocurrido un error!: {error}"
    

            
        
