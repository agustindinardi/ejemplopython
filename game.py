from random import choice, randrange
from datetime import datetime

#Operadores posibles
operators = ["+", "-", "*", "/"]

#Cantidad de cuentas a resolver
times = 5

#Contador inicial de tiempo
#Esto toma la fecha y hora actual
init_time = datetime.now()
correcta = 0
incorrecta = 0
print(f"Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range (0, times):
#Se eligen numeros y operadores al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    #Se imprime la cuenta
    print(f"{i+1} - ¿Cuanto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    if operator == "+":
        resultado = number_1 + number_2
    elif operator == "-":
        resultado = number_1 - number_2
    elif operator == "*":
        resultado = number_1 * number_2
    else:
        if number_2 == 0: # Para evitar divisiones por 0
            print("Error: No se puede dividir por cero")
            continue
        resultado = number_1 / number_2

    result = int(input("resultado: "))   
    if (resultado == result):
        print("El resultado es correcto")
        correcta += 1
    else:
        print("El resultado es incorrecto")
        incorrecta += 1

#Al terminar todo la cantidad de cuentas por resolver
#Se vuelve a tomar la fecha y hora.
end_time = datetime.now()

#Restando las fechas obtenemos el tiempo transcurrido
total_time = end_time - init_time

#Mostramos ese tiempo en segundos.
print(f"/n Tardaste {total_time.seconds} segundos.")
print(f"Obtuviste {correcta} respuestas correctas")
print(f"Obtuviste {incorrecta} respuestas incorrectas")
 #pruebagithub