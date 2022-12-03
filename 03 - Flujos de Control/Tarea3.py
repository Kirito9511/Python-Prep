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

#8) Crear un ciclo while dentro de un ciclo for
#9) Imprimir los números primos existentes entre 0 y 30
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
min=100
max=300
cont=1
i=1
while(cont<=12):
    for i in range(min,max):
        min=min+1
        if (min%12==0):
            cont=cont+1
            print(min)
            continue
        else:
            break
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
min=100
max=300
cont=1
i=1
while(cont<=1):
    for i in range(min,max):
        min=min+1
        if (min%6==0)&(min%3==0):
            cont=cont+1
            print(min)
            continue
        else:
            break