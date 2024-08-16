# Los diccionarios se utilizan para almacenar valores de datos en pares clave:value.

Diccionario={"Nombre": "Jesus",
                 "Apellido": "Garcia", "Edad": 20, 1: "Python"}

#Acceso al diccionario
print(Diccionario["Nombre"])
#Tambien hay otro meodo con get
x=Diccionario.get("Edad")
print(x)

dict = {
    "Nombre": "Luisa",
    "Apellido": "Martinez",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}
#Inserción
dict["Calle"]="Calle Principal"
print(dict)
#Actualización
dict["Nombre"]="Pepe"
print(dict["Nombre"])
#Eliminación
del dict["Calle"]
print(dict)

#Metodos de los diccionarios
#keys() devuelve una lista de las claves del diccionario
print(dict.keys())
#values() devuelve una lista de los valores del diccionario
print(dict.values())
#items() devuelve una lista de los pares clave:valor del diccionario
print(dict.items())
#clear() elimina todos los elementos del diccionario
print(dict.clear())
#copy() devuelve una copia del diccionario
print(dict.copy())
#fromkeys() devuelve un diccionario con las claves especificadas y los valores especificados
print(dict.fromkeys("Python", "Java"))
#get() devuelve el valor para la clave especificada. Si la clave no existe, devuelve el
#valor especificado como segundo argumento
print(dict.get("Nombre", "No existe"))
#items() devuelve una lista de los pares clave:valor del diccionario
print(dict.items())
#keys() devuelve una lista de las claves del diccionario
print(dict.keys())
