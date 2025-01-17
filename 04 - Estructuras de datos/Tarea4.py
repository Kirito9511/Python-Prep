#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
A=['paris','colombia','ecuador','chile','suiza','rusia']
print(A)
#2)Imprimir por pantalla el segundo elemento de la lista
print(A[1])
#3)Imprimir por pantalla del segundo al cuarto elemento
print(A[1:4])
#4)Visualizar el tipo de dato de la lista
print(type(A))
#5)Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(A[2:])
#6)Visualizar los primeros 4 elementos de la lista
print(A[:4])
#7)Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
A.insert(2,'colombia')
print(A)  #Si el dato ya existe igual lo va a meter 
#si uso .append lo deja al final
A.append("Mexico")
print(A)
#8)Agregar otra ciudad, pero en la cuarta posición
A.insert(3,"cANDAA")
print(A)
#9)Concatenar otra lista a la ya creada
B=["Estados unidos", "Suiza", "Catar"]
A.extend(B)
print(A)
#Tambien se puede hace como A.extend([..., ..., ...])


#10)Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(A.index('colombia'))  
# Solo va a mostrar la posicion de la primera palabra, sin importar 
#si hay mas...

#11)¿Qué pasa si se busca un elemento que no existe?
print(A.index('Error'))
#Va a mostrar eror, ya que la palabra no esta en la lista

#12)Eliminar un elemento de la lista
A.remove("colombia")
print(A)

#13)¿Qué pasa si el elemento a eliminar no existe?
A.remove("italia")
print(A)
#Va a  mostrar error ya que no va a eliminar lo que 
# no existe

#14)Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
A.pop()
print(A)
#15)Mostrar la lista multiplicada por 4
print(A*4)

#16)Crear una tupla que contenga los números enteros del 1 al 20
Tu=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#17)Imprimir desde el índice 10 al 15 de la tupla
print(Tu[9:15])
#18)Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in Tu)  #devuelve TRUE
print(30 in Tu)  #devuelve FALSE

#19)Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print(A)
print(A.index("colombia"))
palabra="belgica"
if(not(palabra in A)):
    print(palabra,"no esta")
    A.append(palabra)
    print(A)
 
else:
    print("esta en la posicion,",A.index(palabra))

#20)Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(A.count("colombia"))
print(Tu.count(20))
#21)Convertir la tupla en una lista
Tu1=list(Tu)
print(Tu1)
#22)Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
print(Tu1[0])
print(Tu1[1])
print(Tu1[2])
#23)Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
dictionary={"ciudad": A,"pais":Tu,"Continente":Tu1}
print(dictionary)
#24)Imprimir las claves del diccionario
print(dictionary.keys())
#25)Imprimir las ciudades a través de su clave
print(dictionary["Continente"])
print(dictionary["ciudad"])