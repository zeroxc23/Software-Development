# Las listas se utilizan para almacenar 
# múltiples elementos en una sola variable
# y contienen todos los tipos de variables.

#Ejemplo


List=["Manzana","Pera","Guayaba"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(List)
print(list2)
print(list3)

#En esta sección aqui se mostrara como acceder al contenido de la lista y 
# como usarlo, por ejemplo al utilizar [] se podra imprimir la variable 
# que requeramos dependiendo de la ubicación de la lista que se agrega en
#[] por ejeemplo:

listx=[1, 5, 7, 9, 5,5]
print(listx[1])
# Al utilizar [1] la respuesta sera 5 en vez de 1 dentro de la lista
# debido a que el orden de las variables que
# empieza desde cero por ejemplo 0,1,2,3,4,5, etc.

#Aqui otro ejemplo 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])# Al usar [2:5] el print mostrara las variables desde la posición 2 hasta la 5 osea ['cherry', 'orange', 'kiwi']
print(thislist[:4])# Al usar [:4] el print mostrara desde la posición 0 hasta 4
print(thislist[2:])# Al usar [:4] el print mostrara desde la posición 2 hasta el final de la lista
print(thislist[-1])# Nota tambien para mostrar por ubicación al usar - se llama a la inversa el orden
#Al usar [-1] el print mostrara el variable de la ultima posición 

#Ahora mostraremos como cambiar valores dentro de la lista
lista= ["apple", "banana", "cherry"]
lista[2]="Kiwi" # La función de este codigo se basa en nombrar la ubicación
# luego agregar el nuevo valor en la lista
print(lista)


# Tambien en las listas se puede agregar y eliminar variables
ListA=["Manzana","Pera","Kiwi"]
ListA.append("Mora") # La función de append es agregar al final de la lista la variable que escojamos
print(ListA)

#Segundo ejemplo de agregación de variables 
ListB=["Manzana","Pera","Kiwi"]
ListB.insert(1,"Lulo") # La función de insert es agregar la variable en la ubicación que deseemos
print(ListB)

#Otro ejemplo

ListC=["Maracuya","Mora","Manzana"]
ListD=["Lulo","Kiwi","Mango"]
ListC.extend(ListD) # La función de extend es agregar las variables de una lista a otra
print(ListC)

#Ahora vamos con los ejemplos de eliminar variables
ListE=["Manzana","Pera","Kiwi","Mango"]
ListE.remove("Pera") # La función de remove es eliminar la variable que deseemos
print(ListE)

# Ejemplo #2

ListF=["Manzana","Pera","Kiwi","Mango"]
ListF.pop(1)# Al usar el pop se elimina la variable utilizando su posición y al dejarlo vacio se eliminara el ultimo variable
print(ListF) 

ListG=["Carne","Pollo","Bistec"]
del ListG[0] # La función de del es eliminar la variable utilizando su posición y 
# al dejar vacio[] la lista se eliminara completamente 
print(ListG)

ListH=["Mañana","Tarde","Noche"]
ListH.clear() # La función de clear es eliminar todas las variables de la lista pero aun permaneciendo la lista
print(ListH)

#Para finalizar aqui mas funciones que se utilizan en las listas
ListI=["34","22","124"]
ListI.sort() # La función de sort es ordenar las variables de la lista de menor a mayor
ListI.reverse()#La función de reverse es ordenar las variables a la inversa de su orden original
ListJ=[]
ListJ.copy(ListI)# La función copy es copiar el contenido de una lista a otra vacia 


#Entonces para considerar aqui se anotaran los metodos que usan las listas

"""
append() Añade un elemento al final de la lista
clear() Elimina todos los elementos de la lista
copy() Devuelve una copia de la lista
count() Devuelve el número de elementos con el valor especificado
extend() Añade los elementos de una lista (o cualquier iterable), al final de la lista actual
index() Devuelve el índice del primer elemento con el valor especificado
insert() Añade un elemento en la posición especificada
pop() Elimina el elemento en la posición especificada
remove() Elimina el elemento con el valor especificado
reverse() Invierte el orden de la lista
sort() Ordena la lista
"""
