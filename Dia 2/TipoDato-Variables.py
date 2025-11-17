##Variables
nombre = "Tony Soprano"
edad = 51

#Concatenacion
nombrej = "Julia"
apellido = "Roberts"
nombrecompleto = nombrej + ' ' + apellido

#Print
curso = "Python"
print ('Estás tomando un curso de '+curso )

##Integers
num_entero = 14
print(type(num_entero))

##Floats
num_decimal = 14.14
print(type(num_decimal))

#Operaciones
num1 = 7.5
num2 = 2.5
num3 = num1+num2
print(type(num3))

##Conversiones de datos
num1 = 7.5
num1 = int(num1)
print(type(num1))

num2 = 10
num2=float(num2)
print(type(num2))

num1 = "7.5"
num2 = "10"
print(float(num1) + int(num2))


##Formateo de cadenas
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

puntos_nuevos = 350
puntos_totales = 1225
print (f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores+puntos_nuevos
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')

##Operadores
print(874//27) #cociente
print(456%33) #resto
print(783**0.5) #raíz cuadrada

##Redondeo
num = 10/3
print(round(num,2))

valor = 10.676767
print(round(valor))

num = 5 ** 0.5
print(round(num,4))