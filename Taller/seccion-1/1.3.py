# Crear un programa que verifique que un correo electrónico contenga los caracteres "@" y "." en posiciones válidas.

correo = input("Ingresa tu correo electrónico: ")

if "@" in correo and "." in correo:
    if correo.index("@") > 0 and correo.index(".") > correo.index("@"):
        print("Correo válido")
    else:
        print("Correo inválido")
else:
    print("Correo inválido")