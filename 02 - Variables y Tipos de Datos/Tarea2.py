#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a= 8
print(a)
#2) Imprimir el tipo de dato de la constante 8.5
type(8.5)
#3) Imprimir el tipo de dato de la variable creada en el punto 1
type(a)
#4) Crear una variable que contenga tu nombre
name='Andres Felipe'
#5) Crear una variable que contenga un número complejo
comp= 5 + 9j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
type(name)
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
type(comp)
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
Val1='True'
Val2=True
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
type(Val1)
type(Val2)
#10) Asignar a una variable, la suma de un número entero y otro decimal
Sum1 = float(10) + 10.58 
#11) Realizar una operación de suma de números complejos
A1= 8+9j
A2= 6 -36j
sum2 = A1 + A2
#12) Realizar una operación de suma de un número real y otro complejo
Sum3= a+ A1
print(Sum3)
#13) Realizar una operación de multiplicación
print(A1*A2)
#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
Div=27/4  
print(Div)
#16) De la división anterior solamente mostrar la parte entera
print(24//4)  #Devuelve el COCIENTE pilas !!!!
#17) De la división de 27 entre 4 mostrar solamente el resto
print(24%4)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6*4 + 3)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('buenas'+ ' '+'Hola')
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
2=='2'
#Falso porq uno es texto y el otro es numero
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
2 == int('2')
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# ValueError: could not convert string to float: '3,8'
a = float('3.8')
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
AX=3
AX -= 2
print(AX)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1<<2
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(2 + int('2'))
#26) Realizar una operación válida entre valores de tipo entero y string
print('burro '*3)