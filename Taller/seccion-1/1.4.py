# Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

contraseña = input("Ingresa una contraseña: ")

errores = []


if len(contraseña) < 8:
    errores.append("Debe tener al menos 8 caracteres.")


if not any(c.isupper() for c in contraseña):
    errores.append("Debe contener al menos una letra mayúscula.")


if not any(c.isdigit() for c in contraseña):
    errores.append("Debe contener al menos un número.")


especiales = "!@#$%^&*"
if not any(c in especiales for c in contraseña):
    errores.append("Debe contener al menos un carácter especial (!@#$%^&*).")


if len(errores) == 0:
    print("Contraseña segura ✅")
else:
    print("La contraseña no cumple con lo siguiente:")
    for error in errores:
        print("-", error)