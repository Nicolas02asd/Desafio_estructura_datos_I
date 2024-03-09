import sys

archivo = sys.argv[1]

with open(archivo, "r") as file:
    texto = file.read()

caracteres_distintos = len(set(texto))
palabras_distintas = len(set(texto.split()))

print("El número de caracteres distintos es:", caracteres_distintos)
print("El número de palabras distintas es:", palabras_distintas)
