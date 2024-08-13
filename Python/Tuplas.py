# Las tuplas se utilizan para almacenar múltiples elementos en una sola variable.

mi_tupla=(1,"Hola",23,)
mi_tupla2=(1,55,"Adios")

#Casi parecido a las listas se puede llamar a los elementos por su ubicación y acceso
print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla2.index("Adios"))# Con esta función es lo contrario es decir con el elemento se imprime la ubicación

print(mi_tupla2.count(1))# Con esta función se imprime cuantas veces
# se repite el elemento en la tupla.
#Tambien puede concatenarentre tuplas
print(mi_tupla+mi_tupla2) 
# Las tuplas son inmutables, es decir no se pueden modificar una vez creadas.
# Las tuplas se pueden crear con diferentes tipos de datos. Por ejemplo, se pueden crear 
# con números enteros, flotantes, cadenas de texto, booleanos, etc.
#Ahora veremos la conversión de tupla a lista.
tupla=list(mi_tupla)
print(type(tupla))

#Subtuplas
tupla=(1,2,3,4,5,6,7,8,)
print(tupla[2:5])#Imprime los elementos de la posición 2 al 4


#Eliminación

tupla2=(1,2,3,4,5,6,7,8)
del tupla2
print(tupla2)

#Cambiar los valores de las tuplas
tupla3=(1,2,3,4,5,6,7,8)
cambio= list(tupla3)
cambio[1]="Hola"
x=tuple(cambio)
print(x) #Imprime la tupla con el cambio realizado.

# Extracción de valores de nuevos variables
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)