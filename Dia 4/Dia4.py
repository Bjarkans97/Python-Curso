##Operadores de comparacion

num1 = 36
num2 = 17
mi_bool = bool(num1 >= num2)

from math import sqrt

num1 = sqrt(25)
num2 = 5
mi_bool = bool(num1==num2)

num1 = 64 * 3
num2 = 24 * 8
mi_bool = bool(num1 != num2)

##Operadores logicos
num1 =  36
num2 = 72/2
num3 = 48
mi_bool = bool((num1 > num2) and (num1 < num3))

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = bool((num1 > num2) or (num1 < num3))

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = bool ((palabra1 and palabra2 not in frase) )

##Control de flujos

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
elif num1==num2:
    print(f"{num1} y {num2} son iguales")

##Bucle FOR
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print("Hola "+nombre)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for suma in lista_numeros:
    suma_numeros = suma_numeros + suma

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for suma in lista_numeros:
    if suma % 2 == 0:
        suma_pares = suma_pares + suma
    else:
        suma_impares = suma_impares + suma

##While
numero = 10
aux = 0
while numero >= aux:
    print(numero)
    numero = numero - 1

##Range
mi_lista = list(range(2500,2586))

suma_cuadrados = 0
lista = list(range(1,16))

for i in lista:
    i = i * i
    suma_cuadrados = suma_cuadrados + i

##Enumerador

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

my_tupla = tuple("Python")

lista_indices = list(tuple(enumerate(my_tupla)))

##Zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

todo = list(zip(capitales,paises))

for i in todo:
    print(f'La capital de {i[1]} es {i[0]}')


marcas = ["nike", "lenovo", "mistral"]
productos = ["ropa", "tecnologia", "alcohol"]

mi_zip = zip(marcas,productos)

esp = ["uno", "dos", "tres", "cuatro", "cinco"]
port =["um", "dois", "três", "quatro", "cinco"]
ingl = ["one", "two", "three", "four", "five"]

numeros = list(zip(esp, port, ingl))

print(numeros)

##Min y Max
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = (max(lista_numeros)) - (min(lista_numeros))

#Random
from random import *

aleatorio = randint(1,10)