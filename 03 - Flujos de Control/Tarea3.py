#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
Num = 8
if Num <0:
    print("mayor")
else:
    print("menor")
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
Val1=8
Val2=65

if (type(Val1)==type(Val2)):
    print('Iguales')
else:
    print('Diferentes')

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
i=0
for i in range(1,21):
    if i%2==0:
        print( int(i) , 'Es par')
    else:
        print(int(i) , 'Es impar')
#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(1,6):
    print('El resultado de elevar', i ,'lo a la potencia 3 es igual a', i**3)
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
A23=5
for i in range(0, A23):
    print(i)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
Num2= -5
if (type(Num2)==int):
    if (Num2>0):
        Valor=Num2
        while(Num2>2):
            Num2=Num2-1
            Valor=Valor*Num2
        print(Valor)
    else:
        print('loco')    
else:
    print('No es entero')
#7) Crear un ciclo for dentro de un ciclo while
N=0
while(N<30):
    N+=6
    for i in range(1,N):
        print(N)
        print(i)