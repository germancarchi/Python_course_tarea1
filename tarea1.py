#Ejercicio 1
"""primerNumero = int(input("Ingrese primer número: "))
segundoNumero = int(input("Ingrese segundo número: "))
i = 1
total = 0
while i <= segundoNumero :
    total = total + primerNumero
    #primerNumero += primerNumero
    i += 1
print("El total de la multipicación es: ",total)"""

#Ejercicio 2
"""nombre = input("Ingrese nombre: ")
apellido = input("Ingrese Apellido: ")
nombreCompleto = [nombre, apellido]
nombreCompleto.reverse()
print (nombreCompleto)"""

#Ejercicio 3
# Crear un script que encuentre el elemento menor de una lista
"""numero1 = int(input("Ingrese primer número: "))
numero2 = int(input("Ingrese segundo número: "))
numero3 = int(input("Ingrese tercer número: "))
numero4 = int(input("Ingrese cuarto número: "))
lista = [numero1, numero2, numero3, numero4]
lista.sort()
print("El menor elemento es: ",lista[0])"""

#Ejercicio 4
#Crear un script que imprima el volumen de una esfera por su radio 4/3*pi*r*3
"""r = int(input("Ingrese el valor del radio de la esfera: "))
v = 4/3*3.1416354905*r**3
print ("El volumne de la esfera es: ", v)"""

#Ejercicio 5
#Crear un script que indique si el usuario es mayor de edad
"""edad = input("Ingrese la edad del usuario: ")
try:
    chequeo = int(edad)
except:
    chequeo = "error"

if chequeo == "error":
    print("Ingresó un dato erroneo, por favor ingrese solo números")
else:  
    if chequeo >=18 :
        print ("El usuario es MAYOR de edad")
    else:
        print ("El usuario es MENOR de edad")"""

#Ejercicio 6
#Crear un script que permita calcular si un numero es par o impar
"""numero = input("Ingrese un número: ")
try:
    chequeo = int(numero)
except:
    chequeo = "error"

if chequeo == "error":
    print("Ingresó un dato erroneo, por favor ingrese solo números")
else:  
    if chequeo %2 == 0 :
        print ("El número es PAR")
    elif chequeo %2 ==1 :
        print ("El número es IMPAR")"""

#Ejercicio 7
#Crear un script que indique cuantas vocales tiene una palabra
"""palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
i = 0
for x in vocales:
    for j in palabra:
        if x == j:
            i+=1
print ("El número de vocales es: ",i)"""

#Ejercicio 8
#Crear un script que reciba una cantidad infinita de numeros hasta decir basta, luego que impirma la suma de los numeros ingresados
"""numeros = 0
lista = []
serie = lista
while numeros != "basta":
    numeros = input("Ingrese los número ha ser sumados (para dejar de ingresar números ingrese la palabra 'basta'): ")
    if numeros == "basta":
        break
    else :
        serie = int(numeros)
        lista.append(numeros)
print(lista)
total = 0
for i in lista :
    j = int(i)
    total = (j + total)
print (total)"""

#Ejercicio 9
# Sistema de calificaciones
"""nota = input("Ingrese el valor obtenido por el estudiante (entre 1 a 10): ")
calificacion = int(nota)
if calificacion >=9 and calificacion <=10:
    print ("Su nota es A")
elif calificacion >=8 and calificacion <9 :
    print ("Su nota es B")
elif calificacion >=7 and calificacion <8 :
    print ("Su nota es C")
elif calificacion >=6 and calificacion <7 :
    print ("Su nota es D")
elif calificacion >=0 and calificacion <6 :
    print ("Su nota es F")
else :
    print ("Valor desconocido")"""

#Ejercicio 10
#imprimir numeros descendente
"""lista = ["1", "2", "3", "4", "5"]
lista.reverse()
print (lista)"""

#Ejercicio 11
#Imprimir numeros naturales del 0 al 10 utilizando un ciclo while
"""i = 0
while i <= 10 :
    print (i)
    i += 1"""


#Ejercicio 12
#Calcular area y perimetro de un rectangulo
"""print ("Cálculo del área y el perímetro de un rectángulo")
alto = int(input("Ingrese el alto del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))
area = alto * ancho
perimetro = alto + ancho
print ("El área del rectangulo es:", area)
print ("El perímetro del rectangulo es:", perimetro)"""

#Ejercicio 13
#Iterar un rango de 0 a 10 e imprimir solo los numeros divisibles entre 3
"""for i in range(0,10):
    if i %3 == 0:
        print(i)"""

#Ejercicio 14
"""titulo = {
    "libro" : input("Ingrese el nombre del Libro: "),
    "autor" : input("Ingrese el nombre del Autor: ")
}
#libro = input("Ingrese el nombre del Libro: ")
#autor = input("Ingrese el nombre del Autor: ")
print (titulo["libro"] , titulo["autor"])"""

#Ejercicio 15
"""num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
if num1 >= num2:
    print ("El número mayor es:", num1)
else:
    print ("El número mayor es:", num2)"""

#Ejercicio 16
"""tupla = (13,1,8,3,2,5,8)
lista = []
for i in tupla :
    if i < 5 :
        lista.append(i)
print (lista)"""

#Ejercicio 17
#Crear un script que encuentre la potencia de un numero ingresado por el teclado
"""num = input("Ingrese un número entero: ")
try:
    chequeo = int(num)
except:
    chequeo = "error"

if chequeo == "error":
    print("Ingresó un dato erroneo, por favor ingrese solo números")
else:
    numero = int(num)
    potencia = (input("A qué potencia quiere elevarlo?: "))
    factor = int(potencia)
    total = numero**factor
    print ("El total es: ", total)"""

#Ejercicio 18
#Encontrar la suma de 2 numeros
"""num1 = (input("Ingrese el primer número entero: "))
try:
    chequeo1 = int(num1)
except:
    chequeo1 = "error"

num2 = (input("Ingrese el segundo número entero: "))
try:
    chequeo2 = int(num2)
except:
    chequeo2 = "error"

if chequeo1 == "error" or chequeo2 == "error":
    print("Ingresó un dato erroneo, por favor ingrese solo números")
else:
    numero1 = int(num1)
    numero2 = int(num2)
    total = numero1 + numero2
    print ("El total es: ", total)"""


#Ejercicio 19
#Devolver el numero en orden inverso
"""print("Ingrese un número de 5 dígitos")
lista = []
i = 1
while i <= 5 :
    print("Dígito", i,":")
    digito = input(" ")
    lista.append(digito)
    i+=1
print ("Dígito ingresado es: ",lista)
lista.reverse()
print ("Dígito invertido es: ",lista)
"""

#Ejercicio 20
#Crear un script para saludar desde python
nombre = input("Ingrese su nombre: ")
print ("Hola {}, bienvenido al curso de Python".format(nombre))

