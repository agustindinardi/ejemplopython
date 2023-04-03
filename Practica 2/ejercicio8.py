palabra = input("Ingrese una palabra o frase: ")
letras = []

# Convertir la palabra o frase en una lista de letras
for letra in palabra:
    if letra.isalpha() and letra not in letras:
        letras.append(letra.lower())

# Verificar si la lista de letras es igual a la palabra original
if len(letras) == len(palabra) - palabra.count(" "):
    print("La palabra o frase es un heterograma")
else:
    print("La palabra o frase NO es un heterograma")