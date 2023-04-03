# texto
texto = """título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing 
resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures."""

# ---------------------------------------------------------------------------------------------------------- #

#titulo

partes = texto.split("resumen: ")
titulo = partes[0].strip()  
resumen = partes[1].strip()

palabras_titulo = titulo.split()
if len(palabras_titulo) <= 10:
    print("titulo: ok")
else:
    print("titulo: not ok")

# ---------------------------------------------------------------------------------------------------------- #

#resumen
facil_de_leer = 0
aceptable_para_leer = 0
dificil_de_leer = 0
muy_dificil_de_leer = 0

oraciones = resumen.split(".")
for oracion in oraciones:
    palabras = oracion.split(" ")
    longitud = len(palabras)
    if longitud > 1:
        if longitud <= 12:
            facil_de_leer += 1
        elif longitud <= 17:
            aceptable_para_leer += 1
        elif longitud <= 25:
            dificil_de_leer += 1
        else:
            muy_dificil_de_leer += 1


# imprimir los resultados
print(f"Cantidad de oraciones fáciles de leer: {facil_de_leer}, aceptables para leer: {aceptable_para_leer}, difíciles de leer: {dificil_de_leer}, muy difíciles de leer: {muy_dificil_de_leer}")
