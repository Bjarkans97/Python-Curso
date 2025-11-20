#Funcion sin entrada
def saludar():
    print('¡Hola mundo!')

#Funcion con variable de entrada
nombre_persona =''
def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')

un_numero = 0
def cuadrado(un_numero):
    print(un_numero**2)

#Funcion que retorna un valor
def potencia(val1, val2):
    result = val1**val2
    return result

resul = potencia(2,3)
print(resul)


def usd_a_eur(num1):
    dol = num1 * 0.9
    return dol

dolares = usd_a_eur(8)
print(dolares)


def invertir_palabra(palabra):
    cadenaInvertida = palabra[::-1]
    cadenaInvertida = cadenaInvertida.upper()
    return cadenaInvertida

palabra = invertir_palabra("python")
print(palabra)

#Funcion dimanica
def cantidad_pares(lista):
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares = pares + 1
    return pares


lista_numeros = [2, 5, 3, 67, 5, 3, 34, 4]

#Interaccion entre funciones
from random import randint

dado = []

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

def evaluar_jugada(uno, dos):
    suma_dados = uno + dos
    if suma_dados <= 6:
        return (f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        return (f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    elif suma_dados >= 10:
        return (f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')

dado = lanzar_dados()
dado1 = dado[0]
dado2 = dado[1]
evaluar_jugada(dado1, dado2)


##----
lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lsita):
    sin_repetidos = list(set(lsita))
    mas_alto = max(sin_repetidos)
    sin_repetidos.remove(mas_alto)
    return sin_repetidos

def promedio(lista):
    suma = 0
    promedio = 0
    cantidad = len(lista)
    for i in lista:
        suma = suma + i

    promedio = suma / cantidad
    return promedio

redu = reducir_lista(lista_numeros)
promedio(redu)


#--
from random import randint

lista_numeros = [2, 6, 4, 67, 8, 4, 2, 3]


def lanzar_moneda():
    valor = randint(1, 2)
    moneda = ''
    if valor == 1:
        moneda = 'Cara'
    elif valor == 2:
        moneda = 'Cruz'

    return moneda

def probar_suerte(mon, lista):
    if mon == 'Cara':
        print('La lista se autodestruirá')
        lista = []
    elif mon == 'Cruz':
        print('La lista fue salvada')
    return lista

suerte = lanzar_moneda()
print(probar_suerte(suerte, lista_numeros))

#Args (Permite poner la cantidad de datos que uno necesite)
def suma_cuadrados (*args):
    suma = 0
    for i in args:
        suma = suma + (i**2)
    return suma

print(suma_cuadrados(1, 2, 3, 4, 5, 6, 7, 8, 9))

#Kwargs (Similar al args, pero
def cantidad_atributos(**kwargs):
    suma = 0
    for clave, valor in kwargs.items():
        suma = suma + 1
    return (suma)

cantidad_atributos(a=1, z=2, c=3)


def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

print(lista_atributos(k=2, x=1, e=3))