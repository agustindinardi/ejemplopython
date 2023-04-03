import string

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

letra = input("Ingrese una letra: ").lower()

if letra in string.ascii_lowercase: # Verifica si se ha ingresado una letra y no un caracter.
    palabras = jupyter_info.split()
    palabras_con_letra = [palabra for palabra in palabras if palabra.lower().startswith(letra)]
    if palabras_con_letra:
        print(f"Palabras que comienzan con la letra {letra}: ")
        print(", ".join(palabras_con_letra))
    else:
        print(f"No hay palabras que comiencen con la letra {letra}.")
else:
    print("Error: debe ingresar una letra.")