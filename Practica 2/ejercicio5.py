frase = input("Ingresa una frase: ")
palabra = input("Ingresa una palabra: ")

# Convertimos la frase a minúsculas y la separamos por palabras
palabras = frase.lower().split()

# Contamos cuántas veces aparece la palabra (también en minúsculas)
cantidad = palabras.count(palabra.lower())

print("La cantidad de veces que aparece la palabra en la frase es:", cantidad)
