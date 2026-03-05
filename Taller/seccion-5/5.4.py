import string

def es_palindromo(texto):

    texto = texto.lower()

    for signo in string.punctuation + " ":
        texto = texto.replace(signo, "")

    return texto == texto[::-1]


frase = input("Ingresa una palabra o frase: ")

if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")