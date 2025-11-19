##Index

#quinta posición
palabra = "ordenador"
resul = palabra[4]
print(resul)

#primera aparición
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
result = frase.index('práctica')
print(result)

#última aparición
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resu=frase.rindex('práctica')
print(resu)

##SubStrings

frase = "Controlar la complejidad es la esencia de la programación"
resu = frase[:9]
print(resu)

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resu = frase[8::3]
print(resu)

#Invierte la posición de todos los caracteres de la siguiente frase
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resu = frase[ : :-1]
print(resu)

##Metodos String

#Upper
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

#Junta los string de la lista
lista_palabras = ["La","legibilidad","cuenta."]
aux = ' '.join(lista_palabras)
print(aux)

#Cambia las palabras seleccionadas
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
aux = frase.replace('difícil','fácil')
aux2 = aux.replace('mala','buena')
print(aux2)

##Propidedades de strings
#Repite el texto n cantidad de veces
texto = 'Repetición'
print(texto*15)

#Busca que la palabra no se encuentre en el texto
texto = '''Tierra mojada
mis recuerdos de viaje,
entre las lluvias'''
print ('agua' not in texto)

#Ve el largo de la cadena
tecto = 'electroencefalografista'
resu = len(tecto)
print(resu)

##Listas
mi_lista = [1, 2, 3, 4, 5]

#Agrega una cadena
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')

#Quita una cadena
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado = frutas.pop(2)

##Diccionarios

mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

#imprime el valor 300 del diccionario
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

#Tuple
#contar la cantidad de veces que aparece el valor 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Convierte a lista la siguiente tupla
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

##Sets
#Une los siguientes sets en uno
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

#Elimina un elemento al azar
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()