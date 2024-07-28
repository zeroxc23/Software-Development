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
