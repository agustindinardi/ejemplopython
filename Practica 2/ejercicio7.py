texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

# Identificar mayúsculas, minúsculas y caracteres no letras
mayusculas = 0
minusculas = 0
caracteres_no_letras = 0
for letra in texto:
    if letra.isalpha():
        if letra.isupper():
            mayusculas += 1
        else:
            minusculas += 1
    else:
        caracteres_no_letras += 1

print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("caracteres_no_letras:", caracteres_no_letras)
#------------------------------#
print("Cantidad de palabras:", len(texto.split()))