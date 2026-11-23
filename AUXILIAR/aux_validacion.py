import re 
from datetime import datetime


def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))

def validar_fecha(fecha):
    patron = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if not re.match(patron, fecha):
        return False

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_rut(rut):
    patron = r"^\d{1,2}\.\d{3}\.\d{3}-[\dKk]$"
    if re.match(patron, rut):
        rut_limpio = rut.replace('.', '').replace('-','')
        digito_verificador = rut_limpio[-1].upper()
        numero_rut = rut_limpio[:-1]
        rut_invertido = numero_rut[::-1]

        multiplicador = 2
        suma = 0

        for caracter in rut_invertido:
            suma += int(caracter) * multiplicador
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2

        resto = suma % 11
        digito_calculado = 11 - resto

        if digito_calculado == 11:
            digito_calculado = '0'
        elif digito_calculado == 10:
            digito_calculado = 'K'
        else:
            digito_calculado = str(digito_calculado)

        if digito_calculado == digito_verificador:
            return True
        else:
            print("RUT Invalido")
            return False
    else:
        return False

def validar_celular(celular):
    patron = r"^9\d{8}$"
    if re.match(patron, celular):
        return True
    else: 
        return False

def validar_contrasenia(contrasenia):
    errores = []
    
    if len(contrasenia) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    if not re.search(r"[a-z]", contrasenia):
        errores.append("Debe incluir al menos una letra minúscula.")

    if not re.search(r"[A-Z]", contrasenia):
        errores.append("Debe incluir al menos una letra mayúscula.")

    if not re.search(r"\d", contrasenia):
        errores.append("Debe incluir al menos un número.")

    if not re.search(r"[@$!%*?&._-]", contrasenia):
        errores.append("Debe incluir al menos un carácter especial (ej: @, $, !, %, *, ?, &, ., -).")
    if errores:
        return False, errores
    
    return True, []
    